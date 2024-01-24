from concurrent import futures

import grpc
import time
import threading
import protos.chat_pb2 as chat
import protos.chat_pb2_grpc as rpc
from chat_client import ChatClient
port = 33333


class ChatService(rpc.ChatServiceServicer):
    def __init__(self):
        self.chats = []

    def Receiver(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                msg = self.chats[lastindex]
                lastindex += 1
                yield msg

    def Sender(self, request: chat.ChatMessage, context):
        self.chats.append(request)
        return chat.Empty()


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServiceServicer_to_server(ChatService(), server)

    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    client = ChatClient('server')
    threading.Thread(target=client.send_message).start()
    while True:
        time.sleep(64 * 64 * 100)
