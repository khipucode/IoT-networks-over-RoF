/IoT-RoF-Networks
│── 📄 README.md                 # General project documentation
│── 📄 architecture.md            # System architecture description
│
│── 📁 firmware/                  # Code for IoT devices
│   ├── 📁 station1/              # Scripts for Station 1 (Primary)
│   │   ├── sink_xbee1.py         # Script for the first sink
│   │   ├── sink_xbee2.py         # Script for the second sink
│   │   ├── node1_controller.py   # Control script for Node 1
│   │   ├── node2_controller.py   # Control script for Node 2
│   │   ├── node3_controller.py   # Control script for Node 3
│   │   ├── node4_controller.py   # Control script for Node 4
│   │   ├── README.md             # Documentation for Station 1
│   │
│   ├── 📁 station2/              # Scripts for Station 2 (Secondary)
│   │   ├── sink_xbee3.py         # Script for the third sink in Station 2
│   │   ├── node5_controller.py   # Control script for Node 5
│   │   ├── node6_controller.py   # Control script for Node 6
│   │   ├── node7_controller.py   # Control script for Node 7
│   │   ├── node8_controller.py   # Control script for Node 8
│   │   ├── README.md             # Documentation for Station 2
│
│── 📁 scripts/                    # Auxiliary scripts for communication and configuration
│   ├── network_setup.py           # Script for network configuration
│   ├── data_transmission.py       # Script for data packet transmission
│   ├── power_adjustment.py        # Script for adjusting node transmission power
│   ├── sync_stations.py           # Synchronization between Station 1 and Station 2
│   ├── README.md                  # Explanation of scripts
│
│── 📁 data/                        # Test data and configuration files
│   ├── test_results.csv            # Test results and measurements
│   ├── README.md                   # Explanation of stored data
│
│── 📁 docs/                        # Project documentation
│   ├── architecture.md             # Detailed explanation of the system architecture
│   ├── protocols.md                # Description of communication protocols used
│   ├── hardware.md                 # Hardware specifications (XBee, RoF, antennas, etc.)
│   ├── data_flow.md                # Data flow between devices
│
│── 📁 configs/                     # System configuration files
│   ├── system_config.md            # General system configuration
│
│── 📁 tests/                       # Automated test scripts
│   ├── test_communication.py       # Test script for device communication
│   ├── test_data_transmission.py   # Test script for packet transmission and reception
│
│── .gitignore                      # Files to be ignored by Git
│── requirements.txt                 # Project dependencies (Python libraries, etc.)
│── docker-compose.yml               # Docker configuration if needed
│── Makefile                         # Commands for easy execution
