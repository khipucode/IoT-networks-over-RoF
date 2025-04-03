from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time
import random

# === CONFIGURAÇÕES ===
#PORT = "/dev/ttyUSB0"
PORT = "/dev/ttyUSB1" 

BAUD_RATE = 57600 #19600   

NUM_TRAMAS = 100             # total de tramas a enviar
TAMANHO_PAYLOAD = 10         # tamanho do payload (em bytes)
INTERVALO_SEGUNDOS = 4    # tempo entre envios

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        print(f"Envio de {NUM_TRAMAS} tramas com {TAMANHO_PAYLOAD} bytes cada e intervalo de {INTERVALO_SEGUNDOS}s...")

        #destino broadcast
        remote = RemoteXBeeDevice(device, XBee64BitAddress.BROADCAST_ADDRESS)

        for i in range(NUM_TRAMAS):
            prefixo = f"N1{i:03}-"   #Mudar o numero do nó
            sufixo = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=TAMANHO_PAYLOAD - len(prefixo)))
            payload = bytes(prefixo + sufixo, 'utf-8')

            device.send_data_async(remote, payload)

            print(f"trama {i+1}/{NUM_TRAMAS} | Payload: {payload}")

            time.sleep(INTERVALO_SEGUNDOS)

        print("Fim")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
