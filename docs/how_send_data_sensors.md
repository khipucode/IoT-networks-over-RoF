
# Estatísticas Típicas de Sensores IoT

Este documento reúne dados típicos de frequência de envio e tamanho de payload de sensores em aplicações de IoT.

---

## 📊 1. Frequência de envio de sensores (mensagens por tempo)

| Tipo de Aplicação                | Frequência comum         | Observações |
|----------------------------------|---------------------------|-------------|
| 💡 Sensor de temperatura         | 1 a cada 1–60 segundos    | Pode ser mais lenta se temperatura muda pouco |
| 🏡 Sensor de presença (PIR)      | Somente ao detectar algo | Evento-driven |
| 🌱 Sensor de umidade solo        | 1 por minuto até 1 por hora | Agricultura de precisão |
| 🏭 Sensor industrial (vibração)  | 10–100 vezes por segundo  | Pode ser até em tempo real |
| 🛣️ Sensor de tráfego             | 1–10 por segundo          | Varia conforme fluxo |
| 📈 Acelerômetro/Giroscópio       | 50–200 Hz                 | Alta taxa para movimentos |
| 🔋 Sensor de bateria (voltagem)  | 1 por minuto ou mais      | Baixa variação |
| 🌍 Estações meteorológicas       | 1 a cada 10 s – 5 minutos | Vários sensores integrados |

### 📌 Valores médios gerais:
- **Baixa frequência**: **1 mensagem a cada 10 segundos a 5 minutos**
- **Alta frequência (tempo real)**: até **100 mensagens por segundo**

---

## 📦 2. Tamanho médio de payload

| Conteúdo do payload                   | Tamanho típico (bytes) |
|--------------------------------------|-------------------------|
| Temperatura (float ou int16)         | 2 a 4 bytes             |
| ID do sensor                          | 2 a 8 bytes             |
| Timestamp (epoch)                    | 4 a 8 bytes             |
| Umidade, pressão, luminosidade       | 2 a 4 bytes cada        |
| GPS (latitude + longitude + hora)    | 16 a 32 bytes           |
| Pacote completo com cabeçalho        | 10 a 50 bytes           |

### 🔢 Exemplo típico de payload:
```json
{
  "id": 12,
  "temp": 22.3,
  "hum": 40.1,
  "bat": 3.65
}
```
Compactado (em binário ou JSON leve): cerca de **20 a 40 bytes**

---

## ✅ Resumo prático

| Métrica                     | Valor típico |
|----------------------------|--------------|
| 📬 Frequência de envio      | 1 a cada 10 s (sensor comum) |
| 📦 Tamanho médio de payload | 10 a 50 bytes |
| 📡 Volume por minuto        | 6 a 360 pacotes |
| ⏱️ Volume por hora          | 360 a 20.000 pacotes |
| 💾 Dados por hora           | 3,6 KB a 1 MB (dependendo da aplicação e compactação) |

---

> **Observação:** Estes valores são estimativas com base em aplicações reais de redes sem fio, literatura e projetos de sensores em campo.
