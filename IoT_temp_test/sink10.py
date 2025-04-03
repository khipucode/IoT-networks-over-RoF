from digi.xbee.devices import XBeeDevice
import csv
import datetime

#PORT = "/dev/ttyACM0"  # Ajuste conforme sua porta
PORT = "/dev/ttyACM1"  # Ajuste conforme sua porta

BAUD_RATE = 57600 #19600 #115200 #38400
#CSV_FILE = "dados_recebidos.csv"

device = XBeeDevice(PORT, BAUD_RATE)

#def salvar_csv(timestamp, remetente, tamanho_payload, payload):
 #   with open(CSV_FILE, mode="a", newline='') as file:
  #      writer = csv.writer(file)
   #     writer.writerow([timestamp, remetente, tamanho_payload, payload])


def main():
    try:
        device.open()
        print("Rodando a recepção de pacotes...")

        #with open(CSV_FILE, mode="w", newline='') as file:
        #    writer = csv.writer(file)
        #    writer.writerow(["timestamp", "remetente", "tamanho_payload", "payload"])

        def data_receive_callback(xbee_message):
            remetente = xbee_message.remote_device.get_64bit_addr()
            payload = xbee_message.data
            timestamp = datetime.datetime.now().isoformat()
            #print(f"[{timestamp}] de: {remetente} | tamanho: {len(payload)} | payload: {payload}")
            print(f"Recebido de: {remetente} | tamanho: {len(payload)} | payload: {payload}")
            #salvar_csv(timestamp, remetente, len(payload), payload)

        device.add_data_received_callback(data_receive_callback)

        input("pressione ENTER para encerrar...\n")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
