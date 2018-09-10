from concurrent import futures
import time

import grpc

import add_pb2
import add_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Add(add_pb2_grpc.AddServicer):

    def AddTwo(self, request, context):
        return add_pb2.AddReply(ret=(request.a + request.b))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_pb2_grpc.add_AddServicer_to_server(Add(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

