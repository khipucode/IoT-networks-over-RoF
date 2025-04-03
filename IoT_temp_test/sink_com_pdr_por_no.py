from digi.xbee.devices import XBeeDevice
import datetime

PORT = "/dev/ttyACM1"  # Ajuste conforme sua porta
BAUD_RATE = 57600

device = XBeeDevice(PORT, BAUD_RATE)

# Esperado por nó — informe quantos pacotes cada nó deve enviar
total_esperado_por_no = {
    "0013A20012345678": 100,  # exemplo de endereço 64-bit do nó 1
    "0013A20087654321": 100,  # exemplo de endereço do nó 2
    # adicione mais se precisar
}

# Contador de pacotes recebidos por nó
pacotes_recebidos = {}

def main():
    try:
        device.open()
        print("Rodando a recepção de pacotes...")

        def data_receive_callback(xbee_message):
            remetente = str(xbee_message.remote_device.get_64bit_addr())
            payload = xbee_message.data
            timestamp = datetime.datetime.now().isoformat()

            # Contar pacotes por nó
            if remetente not in pacotes_recebidos:
                pacotes_recebidos[remetente] = 0
            pacotes_recebidos[remetente] += 1

            print(f"[{timestamp}] De: {remetente} | Tamanho: {len(payload)} | Payload: {payload}")

        device.add_data_received_callback(data_receive_callback)

        input("Pressione ENTER para encerrar...\n")

        print("\n--- RESULTADO DO PDR POR NÓ ---")
        for no, total_esperado in total_esperado_por_no.items():
            recebidos = pacotes_recebidos.get(no, 0)
            pdr = recebidos / total_esperado * 100
            print(f"Nó {no} → {recebidos}/{total_esperado} pacotes recebidos → PDR = {pdr:.2f}%")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
