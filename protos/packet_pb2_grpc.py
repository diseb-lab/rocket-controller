# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import packet_pb2 as protos_dot_packet__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/packet_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class PacketServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_packet = channel.unary_unary(
            '/packet.PacketService/send_packet',
            request_serializer=protos_dot_packet__pb2.Packet.SerializeToString,
            response_deserializer=protos_dot_packet__pb2.PacketAck.FromString,
            _registered_method=True)
        self.send_validator_node_info = channel.stream_unary(
            '/packet.PacketService/send_validator_node_info',
            request_serializer=protos_dot_packet__pb2.ValidatorNodeInfo.SerializeToString,
            response_deserializer=protos_dot_packet__pb2.ValidatorNodeInfoAck.FromString,
            _registered_method=True)
        self.get_config = channel.unary_unary(
            '/packet.PacketService/get_config',
            request_serializer=protos_dot_packet__pb2.GetConfig.SerializeToString,
            response_deserializer=protos_dot_packet__pb2.Config.FromString,
            _registered_method=True)


class PacketServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def send_packet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_validator_node_info(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_config(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PacketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'send_packet': grpc.unary_unary_rpc_method_handler(
            servicer.send_packet,
            request_deserializer=protos_dot_packet__pb2.Packet.FromString,
            response_serializer=protos_dot_packet__pb2.PacketAck.SerializeToString,
        ),
        'send_validator_node_info': grpc.stream_unary_rpc_method_handler(
            servicer.send_validator_node_info,
            request_deserializer=protos_dot_packet__pb2.ValidatorNodeInfo.FromString,
            response_serializer=protos_dot_packet__pb2.ValidatorNodeInfoAck.SerializeToString,
        ),
        'get_config': grpc.unary_unary_rpc_method_handler(
            servicer.get_config,
            request_deserializer=protos_dot_packet__pb2.GetConfig.FromString,
            response_serializer=protos_dot_packet__pb2.Config.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'packet.PacketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('packet.PacketService', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class PacketService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def send_packet(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/packet.PacketService/send_packet',
            protos_dot_packet__pb2.Packet.SerializeToString,
            protos_dot_packet__pb2.PacketAck.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def send_validator_node_info(request_iterator,
                                 target,
                                 options=(),
                                 channel_credentials=None,
                                 call_credentials=None,
                                 insecure=False,
                                 compression=None,
                                 wait_for_ready=None,
                                 timeout=None,
                                 metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/packet.PacketService/send_validator_node_info',
            protos_dot_packet__pb2.ValidatorNodeInfo.SerializeToString,
            protos_dot_packet__pb2.ValidatorNodeInfoAck.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_config(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/packet.PacketService/get_config',
            protos_dot_packet__pb2.GetConfig.SerializeToString,
            protos_dot_packet__pb2.Config.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)