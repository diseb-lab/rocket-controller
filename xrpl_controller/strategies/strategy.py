"""This module is responsible for defining the Strategy interface."""

from abc import ABC, abstractmethod
from typing import Tuple, List
from xrpl_controller.core import flatten
from xrpl_controller.validator_node_info import ValidatorNode

MAX_U32 = 2**32 - 1
validator_node_list_store: List[ValidatorNode] = []


class Strategy(ABC):
    """Class that defines the Strategy interface."""

    def __init__(self):
        """Initialize the Strategy interface with a default network partition."""
        # TODO: node.rpc.port should become node.peer.port when functionality for this becomes available
        self.validator_node_list = validator_node_list_store.copy()
        self.node_amount = len(self.validator_node_list)
        self.network_partitions: list[list[int]] = [
            [node.rpc.port for node in self.validator_node_list]
        ]
        self.port_dict = {
            port: index for index, port in enumerate(self.network_partitions[0])
        }
        self.communication_matrix = [
            [True for _ in range(self.node_amount)] for _ in range(self.node_amount)
        ]

    def set_network_partition(self, partitions: list[list[int]]):
        """
        Set the network partition and update the communication matrix.

        Args:
            partitions: a list containing the network partition
        """
        flattened_partition = flatten(partitions)
        if (
            set(flattened_partition) != set(flatten(self.network_partitions))
            or len(flattened_partition) != self.node_amount
        ):
            raise ValueError("The given network partition is not valid.")

        self.network_partitions = partitions
        self.communication_matrix = [
            [False for _ in range(self.node_amount)] for _ in range(self.node_amount)
        ]

        for partition in partitions:
            for i in partition:
                for j in partition:
                    self.communication_matrix[self.port_dict[i]][self.port_dict[j]] = (
                        True
                    )

    def apply_network_partition(
        self, action: int, peer_from_port: int, peer_to_port: int
    ):
        """Apply the network partition to an action and its ports."""
        return (
            action
            if self.communication_matrix[self.port_dict[peer_from_port]][
                self.port_dict[peer_to_port]
            ]
            else MAX_U32
        )

    @abstractmethod
    def handle_packet(self, packet: bytes) -> Tuple[bytes, int]:
        """
        This method is responsible for returning a possibly mutated packet and an action.

        Args:
            packet: the original packet.

        Returns:
        Tuple[bytes, int]: the new packet and the action.
            action 0: send immediately without delay
            action MAX: drop the packet
            action 0<x<MAX: delay the packet x ms
        """
        pass
