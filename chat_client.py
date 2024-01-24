import threading
import grpc
import protos.chat_pb2 as chat
import protos.chat_pb2_grpc as chat_grpc
import time
address = 'localhost'
port = 33333


class ChatClient:
    def __init__(self, nickname: str):
        self.nickname = nickname
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.stub = chat_grpc.ChatServiceStub(channel)
        threading.Thread(target=self.__listen_for_messages,
                         daemon=True).start()

    def __listen_for_messages(self):
        for response in self.stub.Receiver(chat.Empty()):
            print("\n[{}] {}".format(response.name, response.msg))

    def send_message(self):
        while True:
            incomingMessage = input('Enter message or nothing to stop chatty: ')
            if incomingMessage != '':
                chatty = chat.ChatMessage()
                chatty.name = self.nickname
                chatty.msg = incomingMessage

                self.stub.Sender(chatty)
            else:
                break
            time.sleep(1)

if __name__ == '__main__':
    nickname = input('Enter your nickname: ')
    client = ChatClient(nickname)

    threading.Thread(target=client.send_message).start()
