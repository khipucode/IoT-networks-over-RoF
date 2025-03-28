from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress

PORT = "/dev/ttyUSB0"  # ou "COM3" no Windows
BAUD_RATE = 9600

device = XBeeDevice(PORT, BAUD_RATE)

try:
    device.open()

    # Endereços dos nós remotos (pegar no XCTU ou via código)
    remote1 = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040F4F9EF"))
    # remote2 = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040B8YYYY"))

    # Enviar mensagens para todos os nós
    #for remote in [remote1, remote2]:
    for remote in [remote1]:
        device.send_data(remote, "Olá do nó central!")

    print("Mensagens enviadas com sucesso!")

finally:
    if device is not None and device.is_open():
        device.close()
