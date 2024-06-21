"""Tests for the Iteration Type class and subclasses."""

from concurrent import futures
from datetime import datetime, timedelta
from unittest.mock import MagicMock, Mock, call, patch

import grpc

from protos.ripple_pb2 import TMStatusChange
from xrpl_controller.interceptor_manager import InterceptorManager
from xrpl_controller.iteration_type import (
    LedgerBasedIteration,
    NoneIteration,
    TimeBasedIteration,
)


def test_ledger_based_iteration_init():
    """Tests the initialization of LedgerBasedIteration."""
    iteration = LedgerBasedIteration(5, 10)
    assert iteration._max_iterations == 5
    assert iteration._max_ledger_seq == 10
    assert iteration.cur_iteration == 0

    assert iteration.prev_network_event == 0
    assert iteration.network_event_changes == 0
    assert iteration.ledger_seq == 0
    assert isinstance(iteration.prev_validation_time, datetime)
    assert isinstance(iteration.validation_time, timedelta)
    assert isinstance(iteration._interceptor_manager, InterceptorManager)


def test_time_based_iteration_init():
    """Tests the initialization of TimeBasedIteration."""
    iteration = TimeBasedIteration(5, 10)
    assert iteration._max_iterations == 5
    assert iteration._timeout_seconds == 10
    assert iteration.cur_iteration == 0
    assert isinstance(iteration._interceptor_manager, InterceptorManager)


def test_ledger_based_iteration_add():
    """Tests starting new iteration of LedgerBasedIteration."""
    interceptor_manager = InterceptorManager()
    interceptor_manager.restart = MagicMock()

    iteration = LedgerBasedIteration(5, 10, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    iteration.add_iteration()

    assert iteration.cur_iteration == 1
    interceptor_manager.restart.assert_called_once()


def test_ledger_based_iteration_add_done():
    """Tests whether cleanup is performed properly when iterations reach maximum."""
    interceptor_manager = InterceptorManager()
    interceptor_manager.restart = MagicMock()
    interceptor_manager.stop = MagicMock()
    interceptor_manager.cleanup_docker_containers = MagicMock()

    iteration = LedgerBasedIteration(1, 10, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_server.stop = MagicMock()

    iteration.set_server(grpc_server)
    iteration.add_iteration()
    iteration.add_iteration()

    interceptor_manager.restart.assert_called_once()
    interceptor_manager.stop.assert_called_once()
    interceptor_manager.cleanup_docker_containers.assert_called_once()
    grpc_server.stop.assert_called_once()


def test_ledger_based_iteration_add_done_no_server():
    """Tests whether cleanup is performed properly when iterations reach maximum."""
    interceptor_manager = InterceptorManager()
    interceptor_manager.restart = MagicMock()
    interceptor_manager.stop = MagicMock()
    interceptor_manager.cleanup_docker_containers = MagicMock()

    iteration = LedgerBasedIteration(1, 10, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_server.stop = MagicMock()

    # iteration.set_server(grpc_server)
    iteration.add_iteration()
    iteration.add_iteration()

    interceptor_manager.restart.assert_called_once()
    interceptor_manager.stop.assert_called_once()
    interceptor_manager.cleanup_docker_containers.assert_called_once()
    grpc_server.stop.assert_not_called()


def test_ledger_based_iteration_update():
    """Tests updating LedgerBasedIteration with new status change."""
    status_msg = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 10, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    iteration.start_timeout = MagicMock()

    iteration.update_iteration(status_msg)

    assert iteration.prev_network_event == 1
    assert iteration.network_event_changes == 1
    assert iteration.ledger_seq == 3


def test_ledger_based_iteration_update_complete():
    """Tests updating LedgerBasedIteration with new status change, which should start a new iteration."""
    status_msg_1 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    status_msg_2 = TMStatusChange(
        newStatus=2,
        newEvent=2,
        ledgerSeq=4,
        ledgerHash=b"abcdefg",
        ledgerHashPrevious=b"1234567",
        networkTime=1000,
        firstSeq=0,
        lastSeq=3,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 4, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    iteration.add_iteration = MagicMock()
    iteration.reset_values = MagicMock()

    iteration.update_iteration(status_msg_1)
    iteration.update_iteration(status_msg_2)

    assert iteration.prev_network_event == 2
    assert iteration.network_event_changes == 2
    assert iteration.ledger_seq == 4
    iteration.add_iteration.assert_called_once()


def test_ledger_based_iteration_update_same_status():
    """Tests whether a duplicate status does not cause a new iteration to start."""
    status_msg_1 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    status_msg_2 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1001,
        firstSeq=0,
        lastSeq=2,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 4, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    iteration.add_iteration = MagicMock()
    iteration.reset_values = MagicMock()

    iteration.update_iteration(status_msg_1)
    iteration.update_iteration(status_msg_2)

    assert iteration.prev_network_event == 1
    assert iteration.network_event_changes == 1
    assert iteration.ledger_seq == 3
    iteration.add_iteration.assert_not_called()


def test_ledger_based_iteration_update_diff_status_same_ledger():
    """Tests updating LedgerBasedIteration with new status change, when the ledger seq does not change."""
    status_msg_1 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    status_msg_2 = TMStatusChange(
        newStatus=2,
        newEvent=2,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1001,
        firstSeq=0,
        lastSeq=2,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 4, interceptor_manager)
    iteration.start_timeout_timer = MagicMock()
    iteration.add_iteration = MagicMock()
    iteration.reset_values = MagicMock()

    iteration.update_iteration(status_msg_1)
    iteration.update_iteration(status_msg_2)

    assert iteration.prev_network_event == 2
    assert iteration.network_event_changes == 2
    assert iteration.ledger_seq == 3
    iteration.add_iteration.assert_not_called()


def test_ledger_based_iteration_reset_parameters():
    """Test whether the reset_parameters function, resets the correct parameters."""
    status_msg_1 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 10, interceptor_manager)
    iteration.add_iteration = MagicMock()
    iteration.start_timeout_timer = MagicMock()
    with patch(
        "xrpl_controller.iteration_type.threading.Timer", return_value=Mock()
    ) as mock_timer:
        iteration._timer = mock_timer.return_value
        iteration.update_iteration(status_msg_1)
        iteration.reset_values()

        mock_timer.return_value.cancel.assert_has_calls([call(), call()])

    assert iteration._max_iterations == 5
    assert iteration._max_ledger_seq == 10
    assert iteration.cur_iteration == 0

    assert iteration.prev_network_event == 0
    assert iteration.network_event_changes == 0
    assert iteration.ledger_seq == 0
    assert isinstance(iteration.prev_validation_time, datetime)
    assert isinstance(iteration.validation_time, timedelta)
    assert isinstance(iteration._interceptor_manager, InterceptorManager)


def test_ledger_based_iteration_reset_parameters_no_timer():
    """Test whether the reset_parameters function, resets the correct parameters without a timer defined."""
    status_msg_1 = TMStatusChange(
        newStatus=2,
        newEvent=1,
        ledgerSeq=3,
        ledgerHash=b"abcdef",
        ledgerHashPrevious=b"123456",
        networkTime=1000,
        firstSeq=0,
        lastSeq=2,
    )
    interceptor_manager = InterceptorManager()
    interceptor_manager.start_new = MagicMock()

    iteration = LedgerBasedIteration(5, 10, interceptor_manager)
    iteration.add_iteration = MagicMock()
    iteration.start_timeout_timer = MagicMock()
    with patch(
        "xrpl_controller.iteration_type.threading.Timer", return_value=Mock()
    ) as mock_timer:
        iteration.update_iteration(status_msg_1)
        iteration.reset_values()

        mock_timer.return_value.cancel.assert_not_called()

    assert iteration._max_iterations == 5
    assert iteration._max_ledger_seq == 10
    assert iteration.cur_iteration == 0

    assert iteration.prev_network_event == 0
    assert iteration.network_event_changes == 0
    assert iteration.ledger_seq == 0
    assert isinstance(iteration.prev_validation_time, datetime)
    assert isinstance(iteration.validation_time, timedelta)
    assert isinstance(iteration._interceptor_manager, InterceptorManager)


def test_time_based_iteration_timer():
    """Test whether the timer function calls the add_iteration method."""
    iteration = TimeBasedIteration(5, 0)
    iteration.add_iteration = MagicMock()

    iteration.start_timeout_timer()

    iteration.add_iteration.assert_called_once()


def test_start_timeout_timer_with_existing_timer():
    """Test whether the start_timeout_timer function cancels the existing timer."""
    iteration = TimeBasedIteration(max_iterations=5, timeout_seconds=0)

    with patch(
        "xrpl_controller.iteration_type.threading.Timer", return_value=Mock()
    ) as mock_timer:
        iteration._timer = mock_timer.return_value
        iteration.start_timeout_timer()

        mock_timer.assert_called_once()
        mock_timer.return_value.cancel.assert_called_once()


def test_none_iteration_init():
    """Test initialization of NoneIteration class."""
    iteration = NoneIteration(60)
    assert iteration._max_iterations == 1
    assert iteration.cur_iteration == 0
    assert isinstance(iteration._interceptor_manager, InterceptorManager)


def test_none_iteration_add():
    """Test adding an iteration with NoneIteration class."""
    iteration = NoneIteration(60)
    assert iteration._max_iterations == 1
    assert iteration.cur_iteration == 0
    assert isinstance(iteration._interceptor_manager, InterceptorManager)

    iteration.add_iteration()
    assert iteration._max_iterations == 1
    assert iteration.cur_iteration == 0
    assert isinstance(iteration._interceptor_manager, InterceptorManager)