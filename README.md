# Ethereum-Smart-Meter
This project provides a cost-effective way of linking a standard digital energy meter with blockchain by connecting it with a Raspberry Pi which extracts the energy pulses from the meter and then simultaneously deploys them on the Ethereum blockchain.

Smart contracts for energy trade: https://github.com/Rishabh42/Energy-trade-contracts  
Project demo: https://www.youtube.com/watch?v=rKbV1VUOYm0

# Circuit Diagram of the setup:
This project uses an optocoupler circuit to connect the energy meter and the Raspberry Pi, the full circuit diagram is as shown below:
![image](https://user-images.githubusercontent.com/20457952/56360297-da643380-6201-11e9-901e-14394f298e0d.png)

This project requires you to fabricate an optocoupler which needs to be connectedto the RPi using 2 jumper wires as shown. The setup records pulses on pin number 3 of the RPi through GPIO (provided you have connected the other jumper to one of the ground pins, in this case: pin no. 39).

Aerial view of the setup:
![image](https://user-images.githubusercontent.com/20457952/56360744-2c598900-6203-11e9-93c8-7b57d5f5cd27.png)

# Running the project
1. Clone this repo
2. Setup SSH on the Raspberry Pi and connect it with your host system.
3. Run ganache-cli on port 8545 of your host system.
4. Forward a port, say 8080 on the Raspberry Pi to port 8545 on your host system because it's not practically feasible to run ganache on Raspberry Pi. Run this command on the RPi's terminal to achieve the same: 
`ssh -L 8080:localhost:8545 <Name of host>@<IP address of your host system>`
5. Deploy the smart contract. 
