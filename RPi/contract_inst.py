import time
from web3 import Web3, HTTPProvider
import contract_abi

contract_address     = 0x303e363acdf3d8b1862a96d32485bd824183cab0
wallet_private_key   = "0xfbed64c436bd41ff341e058e9a7ed3299ff0d7aa4652c9c74fdf0dc74363580f"
wallet_address       = 0xf05d96ef1cd5e83db50070099c2db357e4f21fca

# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.enable_unaudited_features()

contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

counter=5

def broadcast_reading(counter):


    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = contract.functions.newReading(counter).buildTransaction({
        'chainId': [Other],
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })
