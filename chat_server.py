from concurrent import futures
import time

import grpc
import chat_pb2
import chat_pb2_grpc as chat_grpc

class ChatServicer(chat_grpc.ChatServiceServicer):
    def BidiChat(self, request_iterator, context):
        for request in request_iterator:
            print("Interacting request made:")
            print(request)

            aa = chat_pb2.ChatMessageResponse()
            aa.message = f"{request.name}: {request.message}"
            yield aa
        
        


def serve():
    host = 'localhost'
    port = '50051'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('{}:{}'.format(host, port))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()