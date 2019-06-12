abi = """[
	{
		"constant": false,
		"inputs": [
			{
				"name": "energy",
				"type": "uint256"
			}
		],
		"name": "newReading",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_user",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_reading",
				"type": "uint256"
			}
		],
		"name": "readingEvent",
		"type": "event"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "_readings",
		"outputs": [
			{
				"name": "uAddr",
				"type": "address"
			},
			{
				"name": "energy_consumed",
				"type": "uint256"
			},
			{
				"name": "readingNo",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "readingsArr",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "returnCarbonCredits",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]"""
