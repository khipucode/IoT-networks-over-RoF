# IoT-networks-over-RoF
IEEE 802.15.4 supports ZigBee for mesh networking but faces challenges in extending coverage to remote nodes. Radio over Fiber (RoF) improves network expansion with low latency, high capacity, and resistance to interference. This study evaluates RoF’s impact on IEEE 802.15.4 and ZigBee networks through real-world testing.

## Physical network structure
The physical architecture includes remote wireless nodes connected through RoF links to a centralized sink or coordinator node. The fiber link bridges the distance between isolated areas and the main network hub.
![image](https://github.com/user-attachments/assets/2ad06c94-da97-4fd8-adb9-cd71166045ec)

## Logical network diagram
This logic diagram illustrates the data flow and communication roles within the mesh network. RoF extends the wireless reach while maintaining the ZigBee protocol’s logical structure for routing and coordination.
![diagrama2](https://github.com/user-attachments/assets/ebc6ac01-c10d-4efd-bb6c-dc65abd300ec)

## Project Structure
```
📂 IoT-RoF-Networks
├── 📄 README.md                → Project overview
├── 📁 firmware/               → IoT node and sink control scripts
├── 📁 scripts/                → Setup, transmission, and sync tools
├── 📁 data/                   → Test results
├── 📁 docs/                   → Protocols, hardware, and architecture
├── requirements.txt          → Python dependencies
└── Makefile                  → Automation commands
