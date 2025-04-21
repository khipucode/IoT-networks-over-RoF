from digi.xbee.devices import XBeeDevice

# === READ CONFIGURAÇÕES DE CADA NÓ ===
# permite ler e monstrar as configurações dos nós e sink na estação 1
# ESTAÇÃO I - killjoy

NODES = [
    {
        "PORT": "/dev/ttyACM1",
        "BAUD_RATE": 57600
    },
    {
        "PORT": "/dev/ttyUSB2",
        "BAUD_RATE": 57600
    },
    {
        "PORT": "/dev/ttyACM0",
        "BAUD_RATE": 57600
    },
    {
        "PORT": "/dev/ttyUSB1",
        "BAUD_RATE": 57600
    },
    {
        "PORT": "/dev/ttyUSB0",
        "BAUD_RATE": 57600
    },
    {
        "PORT": "/dev/ttyUSB3",
        "BAUD_RATE": 57600
    }
]

def configurar_no(node_config):
    device = XBeeDevice(node_config["PORT"], node_config["BAUD_RATE"])

    try:
        device.open()
        print(f"\n>>> Configurando nó na porta {node_config['PORT']}")

        # === LER PARÂMETROS ATUAIS ===
        ni = device.get_parameter("NI").decode('utf-8')
        pl = int.from_bytes(device.get_parameter("PL"), 'big')
        ch = device.get_parameter("CH")[0]
        pan_id_bytes = device.get_parameter("ID")
        pan_id_hex = pan_id_bytes.hex().upper()
        #pan_id_hex = device.get_parameter("ID").hex().upper()
        pan_id_decimal = int.from_bytes(pan_id_bytes, byteorder='big')
        freq = 2405 + 5 * (ch - 11)

        print("=== PARÂMETROS ATUAIS ===")
        print(f"Nome (NI)    : {ni}")
        print(f"Potência (PL): {pl}")
        print(f"Canal (CH)   : {ch} - Frequência aprox: {freq} MHz")
        print(f"PAN ID       : 0x{pan_id_hex}={pan_id_decimal}")

    except Exception as e:
        print(f"Erro ao configurar o nó na porta {node_config['PORT']}: {e}")

    finally:
        if device is not None and device.is_open:
            device.close()

def main():
    for node in NODES:
        configurar_no(node)

if __name__ == "__main__":
    main()
