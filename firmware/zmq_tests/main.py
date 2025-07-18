from digi.xbee.devices import XBeeDevice
import serial
import zmq
import time
import threading
import csv

# --- Configurações do XBee ---
PORT = '/dev/ttyACM0'
BAUD_RATE = 57600

CSV_FILE = "dados_recebidos.csv"

device = XBeeDevice(PORT, BAUD_RATE)

# --- Configurações ZeroMQ ---
SERVER_ADDRESS = "tcp://localhost:5557"


class XBeeZeroMQGateway:
    def __init__(self, PORT, baud_rate, server_address):
        self.PORT = PORT
        self.baud_rate = baud_rate
        self.server_address = server_address
        self.running = True

        self.ser = None
        self.zmq_context = None
        self.zmq_socket = None

    def salvar_csv(self):
        with open(CSV_FILE, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.timestamp, self.remetente, self.tamanho_payload, self.payload])


    def _init_serial(self):
        try:
            self.ser = serial.Serial(self.PORT, self.baud_rate, timeout=1)
            print(f"Conectado à porta serial {self.PORT}...")
            return True
        except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial {self.PORT}: {e}")
            return False

    def _init_zmq(self):
        try:
            self.zmq_context = zmq.Context()
            # PUSH para enviar dados do XBee para o servidor ZeroMQ
            self.zmq_socket = self.zmq_context.socket(zmq.PUSH)
            self.zmq_socket.connect(self.server_address)
            print(f"Conectado ao servidor ZeroMQ em {self.server_address}...")
            return True
        except zmq.ZMQError as e:
            print(f"Erro ZeroMQ ao conectar ao servidor: {e}")
            return False

    def read_xbee_and_send_to_zmq(self):
        if not self._init_serial() or not self._init_zmq():
            self.stop()
            return

        print("Gateway XBee-ZeroMQ pronto. Lendo do XBee e enviando para ZeroMQ...")
        while self.running: # TODO: implementar o mecanismo de recebimento aqui
            try:
                # Ler dados do XBee (pode ser necessário um protocolo de enquadramento)
                data_from_xbee = self.ser.readline().decode('utf-8').strip()

                if data_from_xbee:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    message_to_send = f"[{timestamp}] XBee Data: {data_from_xbee}"
                    print(f"Recebido do XBee: '{data_from_xbee}' -> Enviando para ZeroMQ: '{message_to_send}'")
                    self.zmq_socket.send_string(message_to_send)
                else:
                    time.sleep(0.01) 

            except serial.SerialException as e:
                print(f"Erro serial: {e}. Reconectando...")
                self.stop()
                time.sleep(5) # Espera antes de tentar reconectar
                self.__init__(self.PORT, self.baud_rate, self.server_address) # Tenta reiniciar
                self.start() # Reinicia o ciclo
                break
            except zmq.ZMQError as e:
                print(f"Erro ZeroMQ: {e}. Verifique o servidor ZeroMQ.")
                self.stop()
                break
            except UnicodeDecodeError:
                print("Erro de decodificação de bytes do XBee. Ignorando...")
            except Exception as e:
                print(f"Erro inesperado: {e}")
                self.stop()
                break


    def start(self):
        self.read_thread = threading.Thread(target=self.read_xbee_and_send_to_zmq)
        self.read_thread.start()

    def stop(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Porta serial fechada.")
        if self.zmq_socket:
            self.zmq_socket.close()
        if self.zmq_context:
            self.zmq_context.term()
        print("Gateway XBee-ZeroMQ encerrado.")

if __name__ == "__main__":
    gateway = XBeeZeroMQGateway(PORT, BAUD_RATE, SERVER_ADDRESS)
    try:
        gateway.start()
        while threading.active_count() > 1: # Espera todas as threads terminarem (no caso só a de leitura)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCtrl+C detectado. Encerrando o gateway...")
    finally:
        gateway.stop()