import grpc
import chat_pb2
import chat_pb2_grpc
from concurrent import futures
import threading

class ChatClient:
    def __init__(self, name):
        self.name = name
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = chat_pb2_grpc.ChatServiceStub(self.channel)

    def send_message(self, msg):
        message_request = chat_pb2.ChatMessageRequest(name=self.name, msg=msg)
        response_iterator = self.stub.BidiChat(iter([message_request]))
        for response in response_iterator:
            print(f"[{response.name}]: {response.msg}")

def receive_messages(client):
    message_response = chat_pb2.ChatMessageRequest(name=client.name, msg="")
    response_iterator = client.stub.BidiChat(iter([message_response]))
    for response in response_iterator:
        print(f"[{response.name}]: {response.msg}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    client = ChatClient(name)

    try:
        while True:
            msg = input("Enter message (or type 'exit' to quit): ")
            if msg.lower() == "exit":
                break
            client.send_message(msg)
            receive_messages(client)
    except KeyboardInterrupt:
        pass