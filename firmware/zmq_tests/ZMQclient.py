
import zmq
import time
import random
import sys

class Client:
    def __init__(self, server_address="tcp://localhost:5557", client_id=None):
        self.server_address = server_address
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.socket.connect(self.server_address)
        self.client_id = client_id if client_id else f"Client-{random.randint(1000, 9999)}"
        print(f"Cliente {self.client_id} conectado ao servidor {self.server_address}...")

    def send_messages(self):
        message_count = 0
        try:
            while True:
                message_count += 1
                message = f"[{self.client_id}] Mensagem {message_count} - {time.time()}"
                print(f"[{self.client_id}] Enviando: {message}")
                self.socket.send_string(message)
                time.sleep(1) # Envia uma mensagem a cada segundo
        except KeyboardInterrupt:
            print(f"\nCtrl+C detectado. Encerrando o cliente {self.client_id}...")
        except Exception as e:
            print(f"Erro inesperado no cliente {self.client_id}: {e}")
        finally:
            self.socket.close()
            self.context.term()
            print(f"Cliente {self.client_id} encerrado.")

def run_client():
    client_id = None
    if len(sys.argv) > 1:
        client_id = sys.argv[1] # Permite passar um ID de cliente como argumento

    client = Client(client_id=client_id)
    client.send_messages()

if __name__ == "__main__":
    run_client()
    
"""
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
"""