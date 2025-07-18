import zmq
import time
import threading

class Server:
    def __init__(self, port="5557"):
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind(f"tcp://*:{self.port}")
        self.messages = []
        self.running = True
        print(f"Servidor ZeroMQ escutando na porta {self.port}...")

    def receive_messages(self):
        while self.running:
            try:
                message = self.socket.recv_string()
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Recebido: {message}")
                self.messages.append({"timestamp": timestamp, "message": message})
            except zmq.ZMQError as e:
                if e.errno == zmq.EAGAIN:
                    # Não há mensagens disponíveis, tente novamente
                    time.sleep(0.01)
                else:
                    print(f"Erro ZeroMQ: {e}")
                    break
            except Exception as e:
                print(f"Erro inesperado no servidor: {e}")
                break

    def get_stored_messages(self):
        return self.messages

    def stop(self):
        self.running = False
        print("Encerrando servidor...")
        self.socket.close()
        self.context.term()
        print("Servidor encerrado.")

def run_server():
    server = Server()
    # Inicia a recepção de mensagens em uma thread separada para não bloquear o programa principal
    receiver_thread = threading.Thread(target=server.receive_messages)
    receiver_thread.start()

    try:
        while True:
            # Você pode adicionar lógica para processar as mensagens aqui periodicamente
            # Por exemplo, imprimir o número de mensagens armazenadas a cada 10 segundos
            time.sleep(10)
            print(f"Total de mensagens armazenadas: {len(server.get_stored_messages())}")

    except KeyboardInterrupt:
        print("\nCtrl+C detectado. Encerrando o servidor...")
    finally:
        server.stop()
        receiver_thread.join() # Espera a thread de recepção terminar

if __name__ == "__main__":
    run_server()

"""
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
"""