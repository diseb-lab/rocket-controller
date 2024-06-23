"""Entry point of the application, run with python -m xrpl_controller."""

from xrpl_controller.iteration_type import LedgerBasedIteration
from xrpl_controller.packet_server import serve
from xrpl_controller.strategies import Strategy
from xrpl_controller.strategies.random_fuzzer import RandomFuzzer

if __name__ == "__main__":  # pragma: no cover
    strategy: Strategy = RandomFuzzer(
        iteration_type=LedgerBasedIteration()
    )
    server = serve(strategy)

    server.wait_for_termination()
