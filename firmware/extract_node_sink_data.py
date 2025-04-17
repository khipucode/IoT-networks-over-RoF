from digi.xbee.devices import XBeeDevice

# === CONFIGURAÇÕES ===
PORT = "/dev/ttyUSB0"
BAUD_RATE = 57600

# === NOVOS VALORES OPCIONAIS ===
NOVO_NI = b'N1'             # Nome identificador (até 20 caracteres)
NOVA_POTENCIA = b'\x04'     # 0x00 (mínimo) a 0x04 (máximo padrão)
NOVO_CANAL = 0x0C           # Canal entre 0x0B (11) e 0x1A (26)
NOVO_PAN_ID = b'\x12\x34'   # PAN ID de 2 bytes

def main():
    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        # === LER PARÂMETROS ATUAIS ===
        ni = device.get_parameter("NI").decode('utf-8')
        pl = int.from_bytes(device.get_parameter("PL"), 'big')
        ch = device.get_parameter("CH")[0]
        id_hex = device.get_parameter("ID").hex().upper()
        freq = 2405 + 5 * (ch - 11)

        print("=== PARÂMETROS ATUAIS ===")
        print(f"Nome (NI): {ni}")
        print(f"Potência (PL): {pl}")
        print(f"Canal (CH): {ch} - Frequência aprox: {freq} MHz")
        print(f"PAN ID: 0x{id_hex}")

        # === APLICAR NOVOS PARÂMETROS ===
        print("\nAplicando novos parâmetros...")
        device.set_parameter("NI", NOVO_NI)
        device.set_parameter("PL", NOVA_POTENCIA)
        device.set_parameter("CH", bytes([NOVO_CANAL]))
        device.set_parameter("ID", NOVO_PAN_ID)
        device.write_changes()
        print("Parâmetros atualizados com sucesso!")

        # === LER PARÂMETROS NOVAMENTE PARA CONFIRMAR ===
        ni = device.get_parameter("NI").decode('utf-8')
        pl = int.from_bytes(device.get_parameter("PL"), 'big')
        ch = device.get_parameter("CH")[0]
        id_hex = device.get_parameter("ID").hex().upper()
        freq = 2405 + 5 * (ch - 11)

        print("\n=== PARÂMETROS ATUALIZADOS ===")
        print(f"Nome (NI): {ni}")
        print(f"Potência (PL): {pl}")
        print(f"Canal (CH): {ch} - Frequência aprox: {freq} MHz")
        print(f"PAN ID: 0x{id_hex}")

    finally:
        if device is not None and device.is_open:
            device.close()

if __name__ == "__main__":
    main()
