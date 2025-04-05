from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time
import random

# === CONFIGURAÇÕES ===
PORT = "/dev/ttyUSB2"
BAUD_RATE = 57600
NUM_TRAMAS = 100
TAMANHO_PAYLOAD = 6

# Definido pelo usuário: taxa média de pacotes por segundo (lambda)
LAMBDA = 1.5  # Por exemplo, 1.5 pacotes por segundo (~1 envio a cada 0.66s)

def gerar_intervalo_poisson(lambd):
    """Retorna o tempo (em segundos) até o próximo envio, com base na distribuição exponencial."""
    return random.expovariate(lambd)

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        print(f"Iniciando envio Poissoniano de {NUM_TRAMAS} tramas (λ = {LAMBDA} tramas/seg)...")

        remote = RemoteXBeeDevice(device, XBee64BitAddress.BROADCAST_ADDRESS)

        for i in range(NUM_TRAMAS):
            prefixo = f"N{i:03}-"
            sufixo = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=TAMANHO_PAYLOAD - len(prefixo)))
            payload = bytes(prefixo + sufixo, 'utf-8')

            device.send_data_async(remote, payload)

            print(f"Enviada trama {i+1}/{NUM_TRAMAS} | Payload: {payload}")

            intervalo = gerar_intervalo_poisson(LAMBDA)
            time.sleep(intervalo)

        print("Envio concluído.")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
