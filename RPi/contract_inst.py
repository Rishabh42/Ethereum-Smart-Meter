import time
from web3 import Web3, HTTPProvider
import contract_abi

contract_address     = Web3.toChecksumAddress('0xb65cb3f2a530cf5abfdbf268c54d0a6d039931e9')
wallet_private_key   = "678dfd26724f3c4105d2af9e57f1e520faced11da78b0585c83463b88c6c47db"
wallet_address       = Web3.toChecksumAddress('0x908e2575c9df722c20d9b0a8209858064ee5e31e')

# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8080"))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

def broadcast_reading(counter):

    nonce = w3.eth.getTransactionCount(wallet_address)

    #Chain parameters
    txn_dict = contract.functions.newReading(counter).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    #signing the transaction 
    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = wallet_private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = None

    count = 0

    #check if the transaction happened and return the txhash
    while txn_receipt is None and (count < 30):
        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
        print(txn_receipt)
        time.sleep(10)

    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

for i in range(3):
    broadcast_reading(i)

def check_reading():

    return(contract.functions.returnCarbonCredits().call())

print(check_reading())
