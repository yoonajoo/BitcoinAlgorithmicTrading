# 86. call module test
import coinmodule

callbtc = coinmodule.get_open_price("BTC")
print(callbtc)

calleth = coinmodule.get_close_price("ETH")
print(calleth)

# 89. datetime module
import datetime

now = datetime.datetime.now()
print(now)

# 90. datetime.timedelta()
print(now + datetime.timedelta(hours=10))
print(now - datetime.timedelta(minutes=30))

# 91. requests module (anaconda에서 실행)
import requests
resp = requests.get("https://api.bithumb.com/public/ticker/BTC")
print(resp)
print(resp.content)