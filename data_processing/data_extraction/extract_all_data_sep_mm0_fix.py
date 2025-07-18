import requests
import csv
from collections import Counter

# Arquivo de saída
csv_file = "results_sep_mm0.csv"


# Lista de URLs dos arquivos .log
#msnumber = "5000ms"
list_ms = ["1ms", "2ms", "3ms", "4ms", "5ms", "10ms", "15ms", "20ms", "25ms", "30ms", "35ms", "40ms", "50ms", "60ms", "80ms", "100ms", "120ms", "160ms", "200ms", "250ms", "300ms", "400ms", "500ms", "600ms", "800ms" ,"1000ms", "1500ms"]

test_name = "sep_nodes"

for msnumber in list_ms:
    
    sinknumber1 = "sink1_t1"
    sinknumber2 = "sink2_t1"



    # Lista de URLs dos arquivos .log
    urls = [
        f"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/data_set_sep_mm0/{msnumber}/{sinknumber1}.log"
        #f"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/sleeptime_fix/data_set_sep/{msnumber}/{sinknumber1}.log"
        #"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/sleeptime_fix/data_set_mix/{msnumber}/{sinknumber1}.log",
        #"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/building1_building2_mix_split/400ms/sink1_T2.log",
        #"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/building1_building2_mix_split/400ms/sink1_T3.log"
        # Adicione mais links aqui se quiser
    ]

    ascii_payloads = []
    counter = Counter()

    # Loop sobre cada URL
    for url in urls:
        response = requests.get(url)
        response.raise_for_status()

        lines = response.text.strip().splitlines()[1:]  # Ignora o cabeçalho

        for line in lines:
            hex_data = line.split(",")[-1]

            try:
                start = hex_data.index("4E")
                payload_hex = hex_data[start:]
                ascii_text = bytearray.fromhex(payload_hex).decode("ascii", errors="replace")
            except ValueError:
                ascii_text = "FFFF"

            ascii_payloads.append(ascii_text)

            # Contagem por prefixo
            if ascii_text.startswith("N1"):
                counter["N1"] += 1
            elif ascii_text.startswith("N2"):
                counter["N2"] += 1
            elif ascii_text.startswith("N3"):
                counter["N3"] += 1
            elif ascii_text.startswith("N4"):
                counter["N4"] += 1
            #elif ascii_text.startswith("N5"):
             #   counter["N5"] += 1
            #elif ascii_text.startswith("N6"):
              #  counter["N6"] += 1
            #elif ascii_text.startswith("N7"):
             #   counter["N7"] += 1
            #elif ascii_text.startswith("N8"):
             #   counter["N8"] += 1

    # Mostrar resultados
    print("Payload counts by node prefix:")
    for key in ["N1", "N2", "N3", "N4"]:
        print(f"{key}: {counter[key]}")

    num_nodes = 4
    num_envios = 1

    envio_total = num_nodes*num_envios*100

    sum_sink1 = 0
    for k in  ["N1", "N2", "N3", "N4"]:
        sum_sink1 += counter[k]

    pdr_sink1 = sum_sink1 / envio_total
    print("Sink-1  :", sum_sink1/envio_total)
   
    #-----------------------------------------------------------------

    #import requests
    #from collections import Counter

    # Lista de URLs dos arquivos .log
    
    urls = [
        f"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/data_set_sep_mm0/{msnumber}/{sinknumber2}.log"
        #f"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/sleeptime_fix/data_set_sep/{msnumber}/{sinknumber2}.log"
        #"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/building1_building2_mix_split/400ms/sink2_T2.log",
        #"https://raw.githubusercontent.com/khipucode/IoT-networks-over-RoF/refs/heads/main/data_set/building1_building2_mix_split/400ms/sink2_T3.log"
    # Adicione mais links aqui se quiser
    ]

    ascii_payloads = []
    #counter = Counter()

    # Loop sobre cada URL
    for url in urls:
        response = requests.get(url)
        response.raise_for_status()

        lines = response.text.strip().splitlines()[1:]  # Ignora o cabeçalho

        for line in lines:
            hex_data = line.split(",")[-1]

            try:
                start = hex_data.index("4E")
                payload_hex = hex_data[start:]
                ascii_text = bytearray.fromhex(payload_hex).decode("ascii", errors="replace")
            except ValueError:
                ascii_text = "FFFF"

            ascii_payloads.append(ascii_text)

            # Contagem por prefixo
            #if ascii_text.startswith("N1"):
             #   counter["N1"] += 1
            #elif ascii_text.startswith("N2"):
             #   counter["N2"] += 1
            #if ascii_text.startswith("N3"):
             #   counter["N3"] += 1
            #elif ascii_text.startswith("N4"):
             #   counter["N4"] += 1
            if ascii_text.startswith("N5"):
                counter["N5"] += 1
            elif ascii_text.startswith("N6"):
               counter["N6"] += 1
            elif ascii_text.startswith("N7"):
                counter["N7"] += 1
            elif ascii_text.startswith("N8"):
                counter["N8"] += 1

    # Mostrar resultados
    print("Payload counts by node prefix:")
    for key in ["N5", "N6", "N7", "N8"]:
        print(f"{key}: {counter[key]}")

    num_nodes = 4
    num_envios = 1
    envio_total = num_nodes*num_envios*100

    sum_sink2 = 0
    for k in  ["N5", "N6", "N7", "N8"]:
        sum_sink2 += counter[k]

   # print("Sink-1  :", sum_sink1/envio_total)
    print("Sink-2  :", sum_sink2/envio_total)

    pdr_sink2 = sum_sink2 / envio_total

    # Prepara linha para CSV
    linha_csv = [
        msnumber,
        test_name,
        counter["N1"],
        counter["N2"],
        counter["N3"],
        counter["N4"],
        counter["N5"],
        counter["N6"],
        counter["N7"],
        counter["N8"],
        f"{pdr_sink1:.3f}",
        f"{pdr_sink2:.3f}"
    ]

    # Escreve no CSV
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(linha_csv)

    print(f"Salvo para {msnumber}")