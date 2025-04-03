from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time
import random

# === CONFIGURAÇÕES ===
#PORT = "/dev/ttyUSB0"        # Ajuste para sua porta real

PORT = "/dev/ttyUSB2"        # Ajuste para sua porta real

BAUD_RATE = 57600 #19600             # Ajuste conforme o XBee

NUM_TRAMAS = 100             # Total de tramas a enviar
TAMANHO_PAYLOAD = 6         # Tamanho do payload (em bytes)
INTERVALO_SEGUNDOS = 7       # Tempo entre envios

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        print(f"Iniciando envio de {NUM_TRAMAS} tramas com {TAMANHO_PAYLOAD} bytes cada...")

        # Objeto de destino broadcast
        remote = RemoteXBeeDevice(device, XBee64BitAddress.BROADCAST_ADDRESS)

        for i in range(NUM_TRAMAS):
            prefixo = f"N{i:03}-"
            sufixo = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=TAMANHO_PAYLOAD - len(prefixo)))
            payload = bytes(prefixo + sufixo, 'utf-8')

            device.send_data_async(remote, payload)

            print(f"Enviada trama {i+1}/{NUM_TRAMAS} | Payload: {payload}")
            time.sleep(INTERVALO_SEGUNDOS)

        print("Envio concluído.")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
