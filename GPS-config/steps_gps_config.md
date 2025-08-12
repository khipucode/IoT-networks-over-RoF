# Sincronização de Hora no Raspberry Pi usando GPS NEO-6M

Este guia explica como configurar um módulo **GPS NEO-6M** no Raspberry Pi para ajustar automaticamente o relógio do sistema, sem depender de internet.

---

## 📍 1. Conexão Física

Conecte o módulo GPS ao Raspberry Pi usando UART:

| GPS NEO-6M | Raspberry Pi (pinos GPIO)         |
|------------|----------------------------------|
| **VCC**    | Pin 2 (5V) ou Pin 1 (3.3V)        |
| **GND**    | Pin 6 (GND)                       |
| **TX**     | Pin 10 (GPIO15 / RX)              |
| **RX**     | Pin 8  (GPIO14 / TX)              |

> **Velocidade padrão:** 9600 bps

---

## ⚙️ 2. Configuração no Raspbian

1. **Ativar UART**
   ```bash
   sudo raspi-config

- Interface Options → Serial Port
- Desativar login por serial
- Ativar porta serial de hardware
- Instalar pacotes necessários
  
  ```bash
  sudo apt update
  sudo apt install gpsd gpsd-clients jq -y
  ```

2. **Configurar** /etc/default/gpsd
   
   ```bash
   START_DAEMON="true"
   GPSD_OPTIONS="-n"
   DEVICES="/dev/ttyAMA0"
   USBAUTO="false"
   GPSD_SOCKET="/var/run/gpsd.sock"
   ```
## ⏱ 3. Script de Sincronização

**Crie o arquivo** /usr/local/bin/gps_time_sync.sh:
  ```bash
  #!/usr/bin/env bash
  # Sincroniza a hora do sistema usando GPS via gpsd
  
  LOG="/var/log/gps_time_sync.log"
  INTERVAL=60   # segundos entre ajustes
  NOFIX_SLEEP=5 # segundos entre tentativas se não houver fix
  
  echo "[$(date)] Iniciando sincronização de hora via GPS..." | tee -a "$LOG"
  
  # Espera gpsd iniciar
  for i in {1..30}; do
    if timeout 2s gpspipe -w -n 1 >/dev/null 2>&1; then break; fi
    sleep 1
  done
  
  while true; do
    # Captura hora UTC válida do GPS
    TPV=$(gpspipe -w -n 20 2>/dev/null | grep TPV | jq -c 'select(.class=="TPV" and (.mode//0) >= 2 and (.time != null))' | head -n1)
    
    if [ -z "$TPV" ]; then
      echo "[$(date)] Aguardando fix do GPS..." | tee -a "$LOG"
      sleep $NOFIX_SLEEP
      continue
    fi
  
    TIME_UTC=$(echo "$TPV" | jq -r '.time')
  
    if [ -n "$TIME_UTC" ]; then
      if sudo date -u -s "$TIME_UTC" >/dev/null 2>&1; then
        echo "[$(date)] Hora do sistema ajustada para $TIME_UTC (UTC) via GPS." | tee -a "$LOG"
      else
        echo "[$(date)] ERRO ao ajustar hora" | tee -a "$LOG"
      fi
      sleep $INTERVAL
    else
      echo "[$(date)] Sem hora no TPV, tentando novamente..." | tee -a "$LOG"
      sleep $NOFIX_SLEEP
    fi
  done
  ```
**Dar permissão de execução:**
  ```bash
  sudo chmod +x /usr/local/bin/gps_time_sync.sh
  ```
## 🔄 4. Serviço Systemd
**Crie o arquivo**
  ```bash
  /etc/systemd/system/gps-time-sync.service:
  ```
  ```bash
  [Unit]
  Description=Sincronização de hora via GPS (gpsd TPV)
  After=network-online.target gpsd.service
  Wants=gpsd.service
  
  [Service]
  Type=simple
  ExecStart=/usr/local/bin/gps_time_sync.sh
  Restart=always
  RestartSec=5
  StandardOutput=journal
  StandardError=journal
  
  [Install]
  WantedBy=multi-user.target
  ```
Ativar e iniciar:

  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable --now gps-time-sync.service
  ```
## 📋 5. Verificação
Ver status do serviço:
  ```bash
  sudo systemctl status gps-time-sync.service --no-pager -l
  ```
Ver log em tempo real:

  ```bash
  tail -f /var/log/gps_time_sync.log
  ```
Conferir hora do sistema:
  ```bash
timedatectl
  ```

## 📦 6. Replicação em Outro Raspberry Pi

Para instalar em outro dispositivo:
* Conectar o GPS da mesma forma.
* Habilitar UART no raspi-config.
* Instalar gpsd, gpsd-clients, jq.
* Configurar /etc/default/gpsd.
* Copiar gps_time_sync.sh e gps-time-sync.service para os caminhos indicados.
* Ativar o serviço com systemctl enable --now.

## 💡 Observações
Funciona mesmo sem internet.

Se precisar alterar a frequência de atualização, edite INTERVAL no script.

Para evitar que o log cresça indefinidamente, configure logrotate para /var/log/gps_time_sync.log.

  
