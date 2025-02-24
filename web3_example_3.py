
# web3 example
from web3 import Web3

# Connect to Ganache (or your local Ethereum node)
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

if web3.is_connected():
    print("Connected to Ethereum node")
    latest_block = web3.eth.get_block('latest')
    print(f"Latest block number: {latest_block.number}")
else:
    print("Not connected to Ethereum node")
    