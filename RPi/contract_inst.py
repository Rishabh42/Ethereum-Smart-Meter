from web3 import Web3

# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

contract = w3.eth.contract(address = , abi = )
