# === EQUIVALÊNCIAS E FAIXAS VÁLIDAS ===

# ➤ Canal (CH) e Frequência:
#  Canal  |  Hex | Freq (MHz)
#   11    | 0x0B |   2405
#   12    | 0x0C |   2410
#   13    | 0x0D |   2415
#   14    | 0x0E |   2420
#   15    | 0x0F |   2425
#   16    | 0x10 |   2430
#   17    | 0x11 |   2435
#   18    | 0x12 |   2440
#   19    | 0x13 |   2445
#   20    | 0x14 |   2450
#   21    | 0x15 |   2455
#   22    | 0x16 |   2460
#   23    | 0x17 |   2465
#   24    | 0x18 |   2470
#   25    | 0x19 |   2475
#   26    | 0x1A |   2480

# ➤ PAN ID (ID):
#  - Valor de 2 bytes: b'\x00\x00' até b'\xFF\xFF'
#  - Usado para identificar uma rede. Módulos com PAN ID diferente não se comunicam entre si.

# ➤ Potência (PL):
#  - Varia de acordo com o modelo do XBee.
#  - Faixa comum: 0x00 (menor potência) até 0x04 (máxima).
#    Exemplos:
#      0x00 →  -10 dBm
#      0x01 →   -6 dBm
#      0x02 →   -4 dBm
#      0x03 →   -2 dBm
#      0x04 →    0 dBm (ou maior, dependendo do módulo)

# ➤ Nome (NI):
#  - Nome identificador opcional do nó (até 20 caracteres).
#  - Usado para identificação lógica durante testes ou mapeamento.

