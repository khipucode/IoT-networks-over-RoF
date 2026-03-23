# NewSocket — Network Latency & PDR Measurement Tools

Scripts for evaluating **One-Way Delay (OWD)** and **Packet Delivery Ratio (PDR)** in a structured RoF (Radio over Fiber) network testbed.

---

## Files

| File | Role |
|------|------|
| `start_socket.py` | TCP sync server — fires a synchronized START signal to all clients |
| `receiver2_v1.py` | UDP receiver — measures and logs one-way delay per packet |
| `delay_log.csv` | Output log produced by `receiver2_v1.py` |

---

## How It Works

### Synchronized Start — `start_socket.py`

Runs on the central coordinator node. Waits for all configured clients (default: **6**) to connect via TCP on port **5000**. Once all clients are connected, it broadcasts a `START` byte string to all of them simultaneously.

This ensures every client node begins transmitting at the same instant, giving a clean, controlled test window.

```
[Client 1] ──┐
[Client 2] ──┤
[Client 3] ──┤──► start_socket.py (port 5000) ──► sends "START" to all
[Client 4] ──┤
[Client 5] ──┤
[Client 6] ──┘
```

**Config (top of file):**
```python
SERVER_IP   = "0.0.0.0"   # listen on all interfaces
SERVER_PORT = 5000
NUM_CLIENTS = 6            # wait for this many before firing
```

**Run:**
```bash
python3 start_socket.py
```

---

### One-Way Delay Measurement — `receiver2_v1.py`

Listens for UDP packets on port **5001**. Each packet payload is expected to be the sender's Unix timestamp in nanoseconds (as a plain ASCII integer).

#### Delay Algorithm

```
delay_ms = (RX_time_ns − TX_time_ns) / 1e6
```

- `TX_time_ns` — timestamp embedded by the sender at the moment of transmission (`time.time_ns()`)
- `RX_time_ns` — timestamp captured by the receiver at the moment of arrival (`time.time_ns()`)

This is a **One-Way Delay (OWD)** measurement. It does **not** require a round-trip, but it does require that sender and receiver clocks are synchronized (e.g., via NTP or PTP/IEEE 1588).

Every **100 packets** it prints a live stats report:

```
N=100  min=0.123  avg=0.451  med=0.430  p95=0.812  p99=1.043  max=1.201  jitter(std)=0.187 ms
```

At termination (Ctrl+C) it prints a **final summary** with the same metrics over all received packets.

**Config (top of file):**
```python
HOST         = "0.0.0.0"
PORT         = 5001
REPORT_EVERY = 100          # print stats every N packets
SAVE_CSV     = True
CSV_NAME     = "delay_log.csv"
```

**Run:**
```bash
python3 receiver2_v1.py
```

---

### Sender Side (client nodes)

Each client must:
1. Connect to `start_socket.py` on port 5000 and wait for the `"START"` signal.
2. Upon receiving `"START"`, begin sending UDP packets to the receiver host on port 5001.
3. Each packet payload must be the current nanosecond timestamp as a string:
   ```python
   import socket, time
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(str(time.time_ns()).encode(), ("RECEIVER_IP", 5001))
   ```

---

## Output — `delay_log.csv`

Two columns written by `receiver2_v1.py`:

| Column | Description |
|--------|-------------|
| `seq_time_s` | Elapsed seconds since the receiver started |
| `delay_ms` | One-way delay for that packet in milliseconds |

Example:
```
seq_time_s,delay_ms
0.024608,-0.174408
1.025119,-0.012462
2.025561,0.072357
```

> **Note:** Negative delay values indicate the sender clock is slightly ahead of the receiver clock. This is expected when clocks are not perfectly synchronized — use the relative trend and statistics (avg, p95, jitter) rather than absolute values.

---

## Metrics

| Metric | Meaning |
|--------|---------|
| `min` / `max` | Best and worst observed delay |
| `avg` | Mean one-way delay |
| `median` | 50th percentile — robust central estimate |
| `p95` / `p99` | 95th / 99th percentile — tail latency |
| `jitter (std)` | Standard deviation of delay — measures stability |
| **PDR** | Packet Delivery Ratio — computed externally by comparing sent vs received packet counts |

---

## Requirements

- Python 3.6+
- No external dependencies (stdlib only: `socket`, `time`, `statistics`, `csv`)
- Clock synchronization between sender and receiver nodes (NTP or PTP recommended)
