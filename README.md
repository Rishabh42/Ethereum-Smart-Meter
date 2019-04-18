# Ethereum-Smart-Meter
Securing smart meters/ energy meters using Ethereum blockchain and smart contracts:
This project provides a cost-effective way of linking a standard digital energy meter with blockchain by hooking it up with a Raspberry Pi which extracts the energy pulses from the meter and then simultaneously deploys it on the Ethereum blockchain. 

# Circuit Diagram of the setup:
This project uses an optocoupler circuit to connect the energy meter and the Raspberry Pi, the full circuit diagram is as shown below:
![image](https://user-images.githubusercontent.com/20457952/56360297-da643380-6201-11e9-901e-14394f298e0d.png)

An optocoupler should be fabricated and 2 jumper wires should be used for connecting it to the RPi as shown. This project records pulses on pin number 3 of the RPi through GPIO, and the other one is the ground pin which is connected to pin 39.

Aerial view of the setup:
![image](https://user-images.githubusercontent.com/20457952/56360744-2c598900-6203-11e9-93c8-7b57d5f5cd27.png)

# Running the project
1. Clone this repo
2. Setup SSH on the Raspberry Pi and connect it with your host system.
3. Run ganache-cli on port 8545 of your host system.
4. Forward a port, say 8080 on the Raspberry Pi to port 8545 on your host system because it's not practically feasible to run ganache on Raspberry Pi. Run this command on the RPi's terminal to achieve the same: 
`ssh -L 8080:localhost:8545 <Name of host>@<IP address of your host system>`
5. Deploy the smart contract. 
