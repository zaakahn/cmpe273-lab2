import grpc

import add_pb2
import add_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = add_pb2_grpc.AddStub(channel)
        response = stub.AddTwo(add_pb2.AddRequest(a=1, b=2))
    print("Add result for 1 + 2: " + str(response.ret))


if __name__ == '__main__':
    run()

