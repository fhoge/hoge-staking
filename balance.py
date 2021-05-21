import os
import os.path
from datetime import datetime
import requests

API_KEY = os.environ.get('API_KEY')
ADDRESS = os.environ.get('ADDRESS')
HOGE_ADDRESS = "0xfAd45E47083e4607302aa43c65fB3106F1cd7607"

balance_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&address={ADDRESS}&contractaddress={HOGE_ADDRESS}&apikey={API_KEY}"
transactions_url = f"https://api.etherscan.io/api?module=account&action=tokentx&address={ADDRESS}&contractaddress={HOGE_ADDRESS}&apikey={API_KEY}"


transactions = requests.get(transactions_url).json().get('result')

buys = [t for t in transactions if t.get('to') == ADDRESS]
sells = [t for t in transactions if t.get('from') == ADDRESS]

transactions_balance = sum([int(t.get('value')) for t in buys]) - sum([int(t.get('value')) for t in sells])

balance = requests.get(balance_url).json().get('result')

staked = int(balance) - transactions_balance

print(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')},{staked / 10**9}")
