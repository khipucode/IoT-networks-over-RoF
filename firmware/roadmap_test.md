# Anydesk
Station 2 : Mini-PC2 - lrclab  = 1728504538
Station 1 : Mini-PC3 - killjoy = 1044099280

| a. 5 ms (0.005)  | b. 10 ms (0.01)  | c. 15 ms (0.015) | d. 20 ms (0.02)   | e. 25 ms (0.025) |
|------------------|------------------|------------------|-------------------|------------------|
| f. 30 ms  (0.03) | g. 35 ms  (0.035)| h. 40 ms  (0.04) | i. 45 ms  (0.045) | j. 50 ms  (0.05) |
| k. 60 ms  | l. 70 ms  | m. 80 ms  | n. 90 ms   | o. 100 ms |
| p. 120 ms | q. 140 ms | r. 160 ms | s. 180 ms  | t. 200 ms |
| u. 400 ms | v. 600 ms | w. 800 ms | x. 1000 ms |           |

![image](https://github.com/user-attachments/assets/98a7186e-526e-43bb-8def-50e60f238a2c)

#--------------------------------------------
# Calculo de lambda
Envio de pacotes de 5 ms (0.005 s) em média
lambda = 1/0.005
#--------------------------------------------

# Serial ports configuration
 *sink1* - USB1
 *sink2* - USB0
 node1 - ACM1     
 node2 - USB3          
 node3 - ACM0          
 node4 -  USB2       
 *sink3* - ACM1
 node5 - f1   
 node6 - f1   
 node7 - f1   
 node8 - f1   


# TEST 1

**f1 : B**   **Pan ID 1: 1234**  **Power 1: 0**
**f2 : C**   **Pan ID 2: 3020**  **Power 2: 0**

| STATION 1           | STATION 2           |
|---------------------|---------------------|
| *sink1* - f1        | *sink3* - f2        |
| sink2               |                     |
| node1 - f2          | node5 - f1          |
| node2 - f2          | node6 - f1          |
| node3 - f2          | *node7* - f1        |
| node4 - f2          | *node8* - f1        |

# TEST 2

**f1 : B**   **Pan ID 1: 1234**  **Power 1: 0**
**f2 : C**   **Pan ID 2: 3020**  **Power 2: 0**

| STATION 1           | STATION 2           |
|---------------------|---------------------|
| *sink1* - f1        | *sink3* - off        |
| *sink2* - f2        |                     |
| node1 - f2          | node5 - f1          |
| node2 - f2          | node6 - f1          |
| node3 - f2          | *node7* - f1        |
| node4 - f2          | *node8* - f1        |

# TEST 3

**f1 : B**   **Pan ID 1: 1234**  **Power 1: 0**
**f2 : C**   **Pan ID 2: 3020**  **Power 2: 0**

| STATION 1           | STATION 2           |
|---------------------|---------------------|
| *sink1* - f1        | *sink3* - off        |
| *sink2* - f2        |                     |
| node1 - f1          | node5 - f1          |
| node2 - f1          | node6 - f1          |
| node3 - f2          | *node7* - f2        |
| node4 - f2          | *node8* - f2        |
