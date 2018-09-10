# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import add_pb2 as add__pb2


class AddStub(object):
  """The add service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddTwo = channel.unary_unary(
        '/add.Add/AddTwo',
        request_serializer=add__pb2.AddRequest.SerializeToString,
        response_deserializer=add__pb2.AddReply.FromString,
        )


class AddServicer(object):
  """The add service definition.
  """

  def AddTwo(self, request, context):
    """Sends a add req
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AddServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddTwo': grpc.unary_unary_rpc_method_handler(
          servicer.AddTwo,
          request_deserializer=add__pb2.AddRequest.FromString,
          response_serializer=add__pb2.AddReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'add.Add', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
