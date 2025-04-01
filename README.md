# IoT-networks-over-RoF
IEEE 802.15.4 supports ZigBee for mesh networking but faces challenges in extending coverage to remote nodes. Radio over Fiber (RoF) improves network expansion with low latency, high capacity, and resistance to interference. This study evaluates RoF’s impact on IEEE 802.15.4 and ZigBee networks through real-world testing.

## Physical network structure
The physical architecture includes remote wireless nodes connected through RoF links to a centralized sink or coordinator node. The fiber link bridges the distance between isolated areas and the main network hub.



<p align="center">
  <img src="https://github.com/user-attachments/assets/2ad06c94-da97-4fd8-adb9-cd71166045ec" alt="diagrama2" width="95%">
</p>


## Logical network diagram
This logic diagram illustrates the data flow and communication roles within the mesh network. RoF extends the wireless reach while maintaining the ZigBee protocol’s logical structure for routing and coordination.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ebc6ac01-c10d-4efd-bb6c-dc65abd300ec" alt="diagrama2" width="95%">
</p>

![image](https://github.com/user-attachments/assets/2ad06c94-da97-4fd8-adb9-cd71166045ec)

## Logical network diagram
This logic diagram illustrates the data flow and communication roles within the mesh network. RoF extends the wireless reach while maintaining the ZigBee protocol’s logical structure for routing and coordination.
![image](https://github.com/user-attachments/assets/33f6407c-09b2-4aa3-b898-1c23db7a79aa)

>>>>>>> minha-nova-branch


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
