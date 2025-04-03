from digi.xbee.devices import XBeeDevice
import datetime

PORT = "/dev/ttyACM1"  # Ajuste conforme sua porta
BAUD_RATE = 57600

device = XBeeDevice(PORT, BAUD_RATE)

# Total de pacotes esperados (somando todos os nós)
TOTAL_ESPERADO = 200  # ajuste conforme seu teste

# Contador total de pacotes recebidos
total_recebidos = 0

def main():
    try:
        device.open()
        print("Rodando a recepção de pacotes...")

        def data_receive_callback(xbee_message):
            nonlocal total_recebidos
            payload = xbee_message.data
            remetente = xbee_message.remote_device.get_64bit_addr()
            timestamp = datetime.datetime.now().isoformat()

            total_recebidos += 1

            print(f"[{timestamp}] De: {remetente} | Tamanho: {len(payload)} | Payload: {payload}")

        device.add_data_received_callback(data_receive_callback)

        input("Pressione ENTER para encerrar...\n")

        # Cálculo do PDR total
        pdr = total_recebidos / TOTAL_ESPERADO * 100
        print(f"\n--- RESULTADO GLOBAL ---")
        print(f"Pacotes recebidos: {total_recebidos}/{TOTAL_ESPERADO}")
        print(f"PDR total: {pdr:.2f}%")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
