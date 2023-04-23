import requests

# Get Ether Balance for a Single Address
api_key = "BQ2WWI89BYP42FKM2DQVWFSH3GKUMYTH32"
address_from = "0x91C951bE3fd3c07BDaD5ef34f81CEc22B7E17657"
tag = "latest" # earliest or pending or latest
def get_balance(api_key:str, address_from:str, tag:str):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address_from}&tag={tag}&apikey={api_key}"
    response = requests.get(url)
    balance = response.json()["result"] # unit: Wei
    balance = int(balance) / (10**18) # unit: Wei to Ether
    return balance
# print(get_balance(api_key, address_from, tag))


