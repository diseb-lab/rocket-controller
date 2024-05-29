"""This module is responsible for receiving the incoming packets from the interceptor and returning a response."""

from concurrent import futures
from typing import List

import grpc
from xrpl_controller.csv_logger import ActionLogger
from protos import packet_pb2, packet_pb2_grpc
from xrpl_controller.request_ledger_data import store_validator_node_info
from xrpl_controller.validator_node_info import (
    ValidatorNode,
    ValidatorKeyData,
    SocketAddress,
)
from xrpl_controller.strategies.strategy import Strategy

HOST = "localhost"


class PacketService(packet_pb2_grpc.PacketServiceServicer):
    """This class is responsible for receiving the incoming packets from the interceptor and returning a response."""

    def __init__(self, strategy: Strategy, keep_log: bool = True):
        """
        Constructor for the PacketService class.

        Args:
            strategy: the strategy to use while serving packets
            keep_log: whether to keep track of a log containing all actions taken
        """
        self.strategy = strategy
        self.keep_log = keep_log
        if keep_log:
            self.logger = ActionLogger()

    def send_packet(self, request, context):
        """
        This function receives the packet from the interceptor and passes it to the controller.

        Every action taken by the defined strategy will be logged in ../execution_logs.

        Args:
            request: packet containing intercepted data
            context: grpc context

        Returns: the possibly modified packet and an action

        """
        (data, action) = self.strategy.handle_packet(request.data)

        if self.keep_log:
            self.logger.log_action(
                action=action,
                from_port=request.from_port,
                to_port=request.to_port,
                data=data,
            )

        return packet_pb2.PacketAck(data=data, action=action)

    def send_validator_node_info(self, request_iterator, context):
        """
        This function receives the validator node info from the interceptor and passes it to the controller.

        Args:
            request_iterator: iterator of validator node info
            context: grpc context

        Returns: an acknowledgement

        """
        validator_node_list: List[ValidatorNode] = []
        for request in request_iterator:
            validator_node_list.append(
                ValidatorNode(
                    ws_public=SocketAddress(
                        host=HOST,
                        port=request.ws_public_port,
                    ),
                    ws_admin=SocketAddress(
                        host=HOST,
                        port=request.ws_admin_port,
                    ),
                    rpc=SocketAddress(
                        host=HOST,
                        port=request.rpc_port,
                    ),
                    validator_key_data=ValidatorKeyData(
                        status=request.status,
                        validation_key=request.validation_key,
                        validation_private_key=request.validation_private_key,
                        validation_public_key=request.validation_public_key,
                        validation_seed=request.validation_seed,
                    ),
                )
            )
        store_validator_node_info(validator_node_list)
        return packet_pb2.ValidatorNodeInfoAck(status="Received validator node info")


def serve(strategy: Strategy, keep_log: bool = True):
    """
    This function starts the server and listens for incoming packets.

    Returns: None

    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    packet_pb2_grpc.add_PacketServiceServicer_to_server(
        PacketService(strategy, keep_log), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()
