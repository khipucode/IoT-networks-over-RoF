
from digi.xbee.devices import XBeeDevice
import datetime

PORT = "/dev/ttyACM1"  # Ajuste conforme sua porta
BAUD_RATE = 57600

device = XBeeDevice(PORT, BAUD_RATE)

# Dicionário para contar tramas recebidas por ID
tramas_recebidas = set()
total_esperado = 100  # Atualize conforme o número de tramas enviadas

def main():
    try:
        device.open()
        print("Rodando a recepção de pacotes...")

        def data_receive_callback(xbee_message):
            remetente = xbee_message.remote_device.get_64bit_addr()
            payload = xbee_message.data
            timestamp = datetime.datetime.now().isoformat()

            try:
                # Extrai o número da trama: N000, N001, etc.
                id_trama = payload.decode("utf-8").split("-")[0]  # "N000"
                tramas_recebidas.add(id_trama)
                print(f"Recebido de: {remetente} | {id_trama} | tamanho: {len(payload)} | payload: {payload}")
            except Exception as e:
                print(f"Erro ao processar payload: {payload} -> {e}")

        device.add_data_received_callback(data_receive_callback)

        input("Pressione ENTER para encerrar...
")

        # Cálculo do PDR
        recebidas = len(tramas_recebidas)
        pdr = recebidas / total_esperado * 100
        print(f"Pacotes recebidos: {recebidas}/{total_esperado}")
        print(f"PDR: {pdr:.2f}%")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
