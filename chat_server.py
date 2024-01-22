from concurrent import futures
import time

import grpc
import chat_pb2
import chat_pb2_grpc as chat_grpc

class ChatServicer(chat_grpc.ChatServiceServicer):
    def Chat(self, request, context):
        return super().BidiChat(request, context)