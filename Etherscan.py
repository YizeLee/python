import requests

# 取得帳戶餘額
api_key = "BQ2WWI89BYP42FKM2DQVWFSH3GKUMYTH32"
address = "0x91C951bE3fd3c07BDaD5ef34f81CEc22B7E17657"
tag = "latest" # earliest or pending or latest
def get_address_balance(api_key:str, address:str, tag:str):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag={tag}&apikey={api_key}"
    response = requests.get(url)
    balance = response.json()["result"] # unit: Wei
    balance = int(balance) / (10**18) # unit: Wei to Ether
    return balance
# print(get_address_balance(api_key, address, tag))

#取得帳戶的交易紀錄(最多10000筆)
def get_address_txnlist(api_key:str, address:str, startblock:int, endblock:int):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={startblock}&endblock={endblock}&page=1&offset=10&sort=asc&apikey={api_key}"
    response = requests.get(url)
    txn = response.json()
    return txn
print(get_address_txnlist(api_key, "0x7CfC66939423F36ae5E7bCC7335CD2273F4944aC", 13598671, 17106183))
    