from concurrent import futures
import time

import grpc
import chat_pb2
import chat_pb2_grpc as chat_grpc

class ChatServicer(chat_grpc.ChatServiceServicer):
    def Chat(self, request, context):
        return super().BidiChat(request, context)
    


def serve():
    host = 'localhost'
    port = '5000'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    chat_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('{}:{}'.format(host, port))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()