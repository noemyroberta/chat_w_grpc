import chat_pb2_grpc as chat_grpc
import chat_pb2
import time
import grpc

def chat():
    while True:
        message = input("Please enter a message (or nothing to stop chatting): ")

        if message == "":
            break

        msg_request = chat_pb2.ChatMessageRequest(name = "You", message = message)
        yield msg_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = chat_grpc.ChatServiceStub(channel)
        
        responses = stub.BidiChat(chat())

        for response in responses:
            print("Interacting response received: ")
            print(response)


if __name__ == '__main__':
    print('Starting bidirectional chat between client and server')
    run()