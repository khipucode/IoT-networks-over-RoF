from digi.xbee.devices import XBeeDevice

PORT = "/dev/ttyUSB1"  # ou COMx no Windows
BAUD_RATE = 9600

device = XBeeDevice(PORT, BAUD_RATE)

def receive_callback(xbee_message):
    print("Mensagem recebida de {}: {}".format(
        xbee_message.remote_device.get_64bit_addr(),
        xbee_message.data.decode()
    ))

try:
    device.open()
    device.add_data_received_callback(receive_callback)

    print("Aguardando mensagens... (Ctrl+C para sair)")
    input()  # Mantém o programa rodando

finally:
    if device is not None and device.is_open():
        device.close()
