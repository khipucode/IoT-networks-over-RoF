from digi.xbee.devices import XBeeDevice

# === CONFIGURAÇÕES DE CADA NÓ ===
# Script que configura todos os nós e sinks na estação II
# ESTAÇÃO II - lrclab

NODES = [
    {
        "PORT": "/dev/ttyUSB1",
        "BAUD_RATE": 57600,
        #"NI": b"N1", #Node5 
        "PL": b'\x00',
        "CH": 0x0C,
        "PAN_ID": (2030).to_bytes(2, byteorder='big')
    },
    {
        "PORT": "/dev/ttyUSB2",
        "BAUD_RATE": 57600,
        #"NI": b"N2", #Node6 
        "PL": b'\x00',
        "CH": 0x0C,
        "PAN_ID": (2030).to_bytes(2, byteorder='big')
    },
    {
        "PORT": "/dev/ttyACM1",
        "BAUD_RATE": 57600,
        #"NI": b"N3", #Node7 
        "PL": b'\x00',
        "CH": 0x0C,
        "PAN_ID": (2030).to_bytes(2, byteorder='big')
    },
    {
        "PORT": "/dev/ttyUSB0",
        "BAUD_RATE": 57600,
        #"NI": b"N4", #Node8 
        "PL": b'\x00',
        "CH": 0x0C,
        "PAN_ID": (2030).to_bytes(2, byteorder='big')
    },
    {
        "PORT": "/dev/ttyACM0",
        "BAUD_RATE": 57600,
        #"NI": b"N4", #sink3
        "PL": b'\x00',
        "CH": 0x0D,
        "PAN_ID": (2020).to_bytes(2, byteorder='big')
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

        # === APLICAR NOVOS PARÂMETROS ===
        print("Aplicando novos parâmetros...")
        #device.set_parameter("NI", node_config["NI"])
        device.set_parameter("PL", node_config["PL"])
        device.set_parameter("CH", bytes([node_config["CH"]]))
        device.set_parameter("ID", node_config["PAN_ID"])
        device.write_changes()
        print("Parâmetros atualizados com sucesso!")

        # === CONFIRMAR NOVOS PARÂMETROS ===
        ni = device.get_parameter("NI").decode('utf-8')
        pl = int.from_bytes(device.get_parameter("PL"), 'big')
        ch = device.get_parameter("CH")[0]
        pan_id_bytes = device.get_parameter("ID")
        pan_id_hex = pan_id_bytes.hex().upper()
        #pan_id_hex = device.get_parameter("ID").hex().upper()
        pan_id_decimal = int.from_bytes(pan_id_bytes, byteorder='big')
        freq = 2405 + 5 * (ch - 11)

        print("=== PARÂMETROS ATUALIZADOS ===")
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
