import chat_pb2_grpc as chat_grpc
import chat_pb2
import time
import grpc

def run():
    with grpc.insecure_channel('localhost:5000') as channel:
        chat_grpc.ChatServiceStub(channel)
        

if __name__ == '__main__':
    print('Starting bidirectional chat between client [stub] and server')
    run()