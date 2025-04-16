from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import time
import random

# === CONFIGURAÇÕES ===
PORT = "/dev/ttyUSB0"
#PORT = "/dev/ttyUSB1"
BAUD_RATE = 57600  # Taxa de baud padrão do módulo

NUM_TRAMAS = 100             # Total de tramas a enviar
TAMANHO_PAYLOAD = 10         # Tamanho do payload (em bytes)

NOVO_CANAL = 0x0C            # Canal 12 (0x0C) -> 2410 MHz
NOVO_PAN_ID = b'\x30\x20'    # Novo PAN ID
NOVA_POTENCIA = b'\x04'      # Nível máximo de potência (varia com o modelo)

# Parâmetro para envio Poisson (lambda = média de pacotes por segundo)
LAMBDA = 1.5  # Exemplo: ~1 pacote a cada 0.66s

# === Tipo de intervalo entre envios: 'FIXO' ou 'ALEATORIO'
INTERVALO = 'FIXO'  #'ALEATORIO'
INTERVALO_SEGUNDOS_VAR = 2  # Valor usado se INTERVALO for 'FIXO'

# Descrição usada apenas para exibir no console
if INTERVALO == 'FIXO':
    descricao_var = INTERVALO_SEGUNDOS_VAR
else:
    descricao_var = f"Poisson (λ={LAMBDA})"

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        # === POTÊNCIA ===
        potencia_atual = device.get_parameter("PL")
        print(f"Potência atual: {int.from_bytes(potencia_atual, 'big')}")
        device.set_parameter("PL", NOVA_POTENCIA)
        print(f"Nova potência definida: {int.from_bytes(NOVA_POTENCIA, 'big')}")

        # === CANAL ===
        channel = device.get_parameter("CH")
        print(f"Canal atual: {channel.hex().upper()}")
        device.set_parameter("CH", bytes([NOVO_CANAL]))
        freq = 2405 + 5 * (NOVO_CANAL - 11)
        print(f"Canal alterado para {NOVO_CANAL} (Frequência aproximada: {freq} MHz)")

        # === PAN ID ===
        pan_id_atual = device.get_parameter("ID")
        print(f"PAN ID atual: 0x{pan_id_atual.hex().upper()}")
        device.set_parameter("ID", NOVO_PAN_ID)
        print(f"Novo PAN ID definido: 0x{NOVO_PAN_ID.hex().upper()}")

        # Salvar alterações permanentemente
        device.write_changes()
        print("Alterações salvas com sucesso.")

        # === INÍCIO DO ENVIO ===
        print(f"Envio de {NUM_TRAMAS} tramas com {TAMANHO_PAYLOAD} bytes cada e intervalo: {descricao_var}")

        remote = RemoteXBeeDevice(device, XBee64BitAddress.BROADCAST_ADDRESS)

        for i in range(NUM_TRAMAS):
            prefixo = f"N1{i:03}-"  # Mudar o número do nó conforme necessário
            sufixo = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=TAMANHO_PAYLOAD - len(prefixo)))
            payload = bytes(prefixo + sufixo, 'utf-8')

            device.send_data_async(remote, payload)
            print(f"Trama {i+1}/{NUM_TRAMAS} | Payload: {payload}")

            if INTERVALO == 'FIXO':
                time.sleep(INTERVALO_SEGUNDOS_VAR)
            else:
                time.sleep(random.expovariate(LAMBDA))

        print("Fim do envio.")

    finally:
        if device is not None and device.is_open:
            device.close()

if __name__ == '__main__':
    main()
