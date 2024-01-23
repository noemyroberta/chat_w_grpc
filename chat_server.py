from concurrent import futures
import time

import grpc
import chat_pb2
import chat_pb2_grpc as chat_grpc


class ChatServicer(chat_grpc.ChatServiceServicer):
    def __init__(self):
        self.clients = set()

    def BidiChat(self, request_iterator, context):
        for request in request_iterator:
            message = f"[{request.name}]: {request.msg}"

            for _ in self.clients:
                yield chat_pb2.ChatMessageResponse(name=request.name, msg=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    chat_grpc.add_ChatServicer_to_server(ChatServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()