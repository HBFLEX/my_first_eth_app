import os
from web3 import Web3
from dotenv import load_dotenv


load_dotenv()

infra_url = "https://mainnet.infura.io/v3/dc0d4ab019a74e3a9d30d94c22425d51"
web3Client = Web3(Web3.HTTPProvider(infra_url))

print('connecting to node...')
is_connected = web3Client.is_connected()
balance = 0
block = None
meta_mask_account = os.environ.get('META_MASK_ACCOUNT_ADDR')


if is_connected:
    block = web3Client.eth.get_block_number()
    balance = web3Client.eth.get_balance(meta_mask_account)

    print(f'Connection Url: {infra_url}')
    print(f'Balance: {web3Client.from_wei(balance, 'ether')} ether')
    print(f'Block Number: {block}')

else:
    print('There was a connection problem to node')




