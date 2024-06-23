"""Module that defines certain Iteration Types."""

import threading
from datetime import datetime, timedelta
from typing import List

from grpc import Server
from loguru import logger

from protos import ripple_pb2
from xrpl_controller.ledger_result import LedgerResult
from xrpl_controller.interceptor_manager import InterceptorManager
from xrpl_controller.validator_node_info import ValidatorNode


class TimeBasedIteration:
    """Time Based iteration type, keeps track of time elapsed since network start."""

    def __init__(
        self,
        max_iterations: int,
        timeout_seconds: int = 60,
        ledger_timeout: bool = False,
        max_ledger_seq: int = -1,
    ):
        """Init Iteration Type with an InterceptorManager attached."""
        self.cur_iteration = 1
        self._log_results = LedgerResult()

        self._max_iterations = max_iterations
        self._server: Server | None = None
        self._timer: threading.Timer | None = None
        self._timeout_seconds = timeout_seconds
        self.ledger_timeout = ledger_timeout

        self._interceptor_manager = InterceptorManager()
        self._validator_nodes: List[ValidatorNode] | None = None
        self._log_dir: str | None = None

        self._max_ledger_seq = max_ledger_seq
        self.accept_count = 0
        self.network_event_changes = 0
        self.ledger_seq = 1
        self.prev_validation_time = datetime.now()
        self.validation_time = timedelta()

    def _stop_all(self):
        """Stop the interceptor along with the docker containers."""
        logger.info(
            f"Finished iteration {self.cur_iteration-1}, stopping test process..."
        )
        self._interceptor_manager.stop()
        self._interceptor_manager.cleanup_docker_containers()
        if self._server:
            self._server.stop(grace=1)

    def _start_timeout_timer(self):
        """Starts a timeout timer, which starts a new iteration when the timeout is reached."""
        if self._timer:
            self._timer.cancel()
        self._timer = threading.Timer(self._timeout_seconds, self._timeout_reached)
        self._timer.start()

    def _timeout_reached(self):
        """Function that is called when the timeout is reached."""
        logger.info("Timeout reached.")
        self.add_iteration()

    def set_server(self, server: Server):
        """Set the server variable to the running instance of the gRPC server."""
        self._server = server

    def set_validator_nodes(self, validator_nodes: List[ValidatorNode]):
        """Setter for the validator_nodes list, since it needs to be updated every iteration."""
        self._validator_nodes = validator_nodes

    def set_log_dir(self, log_dir: str):
        """Setter for the log_dir variable, since it needs to be updated every iteration."""
        self._log_dir = log_dir

    def add_iteration(self):
        """Add an iteration to the iteration mechanism, stops all processes when max_iterations is reached."""

        if self.cur_iteration <= self._max_iterations:
            self._interceptor_manager.stop()
            self._log_results.new_result_logger(self._log_dir, self.cur_iteration)
            self._reset_values()
            logger.info(f"Starting iteration {self.cur_iteration}")
            self._interceptor_manager.start_new()

            self._start_timeout_timer()
            self.cur_iteration += 1
        else:
            self._stop_all()

    def _reset_values(self):
        """Reset state variables, called when interceptor is restarted."""
        logger.debug("Iteration complete, Resetting state variables...")
        if self._timer:
            self._timer.cancel()
        self._timer = None

        self.accept_count = 0
        self.network_event_changes = 0
        self.ledger_seq = 1
        self.prev_validation_time = datetime.now()
        self.validation_time = timedelta()

    def on_status_change(self, status: ripple_pb2.TMStatusChange):
        """
        Update the iteration values, called when a TMStatusChange is received.

        Resets the timeout when a new ledger gets validated.

        Args:
            status: The TMStatusChange message received on the network.
        """
        # Check whether the event contains an accepted ledger which is exactly 1 sequence no. more than the prev ledger
        if status.newEvent == 1 and status.ledgerSeq == self.ledger_seq + 1:
            self.accept_count += 1

            # Only when every single node sends neCLOSING_LEDGER to all other nodes, we consider the ledger validated.
            if self._validator_nodes and self.accept_count == (
                    len(self._validator_nodes) * (len(self._validator_nodes) - 1)
            ):
                # New ledger validated, we can reset timeout
                if self.ledger_timeout:
                    self._start_timeout_timer()

                self.validation_time = datetime.now() - self.prev_validation_time
                self.ledger_seq = status.ledgerSeq
                self.accept_count = 0
                self.prev_validation_time = datetime.now()
                logger.info(
                    f"Ledger {self.ledger_seq} validated, time elapsed: {self.validation_time}"
                )
                self._log_results.log_ledger_result(
                    self.ledger_seq,
                    self._max_ledger_seq,
                    self.validation_time.total_seconds(),
                    self._validator_nodes,
                )
        if self.ledger_seq == self._max_ledger_seq:
            self.add_iteration()


class LedgerBasedIteration(TimeBasedIteration):
    """Ledger Based iteration type, able to keep track of validated ledgers."""

    def __init__(self, max_iterations: int, ledger_timeout_seconds: int = 60, max_ledger_seq: int = 10):
        """Init the TimeIteration class with a specified timeout in seconds."""
        super().__init__(max_iterations=max_iterations, timeout_seconds=ledger_timeout_seconds, ledger_timeout=True, max_ledger_seq=max_ledger_seq)


class NoneIteration(TimeBasedIteration):
    """
    Iteration Type used for local testing purposes.

    It starts the controller as its separate entity without iterations,
    so you could run the interceptor separately as well.
    """

    def __init__(self, timeout_seconds: int = 300):
        """Init the NoneIteration class with a specified timeout in seconds."""
        super().__init__(max_iterations=1, timeout_seconds=timeout_seconds)

    def _timeout_reached(self):
        """Overrides _timeout_reached to stop the whole process after timeout completes."""
        logger.info("Final time reached.")
        self._stop_all()

    def add_iteration(self, max_ledger_seq: int = -1):
        """Override the add_iteration function to prevent the interceptor subprocess from starting."""
        self._start_timeout_timer()
        self.cur_iteration += 1

    def _reset_values(self):
        """Do nothing when called, needed to satisfy abstract base class constraints."""
        pass

    def on_status_change(self, status: ripple_pb2.TMStatusChange):
        """Override the method since none iteration does not need to keep track of ledgers."""
        pass
