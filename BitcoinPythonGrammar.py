
# 1.2.6 문자열 인덱싱

mycoin = "bitcoin"
print(mycoin[0])
print(mycoin[4])

# 1.2.7 문자열 슬라이싱
greeting = "hello youna"
print(greeting[0:5])
print(greeting[6:])
print(greeting[-5:])

# 1.2.9 문자열 합치기
coin = "비트코인"
fmt = "내가 보유하는 코인은 " + coin + " 입니다."
print(fmt)

# 1.1.10 문자열의 길이
mystring = "hello youna's family"
print(len(mystring))

# 1.3.2 리스트
hold = ["bitcoin", "ripple", "ethereum"]
print(hold)

# 1.3.3 리스트 인덱싱
hold = ["btc_krw", "xrp_krw", "eth_krw"]
print(hold[1])

# 1.3.4 리스트 수정
hold = ["btc_krw", "xrp_krw", "eth_krw"]
hold[0] = "btc_btc"
print(hold[0])

# 1.3.6 리스트 삽입
portfolio = []
portfolio.append("btc")
portfolio.append("eth")
print(portfolio)

portfolio.insert(0, "dash")
print(portfolio)

# 1.3.7 리스트 데이터 삭제
del portfolio[1]
print(portfolio)

# 1.3.8 최대값/최솟값/평균값
ripple_close = [503, 505, 508, 599]
print(max(ripple_close))
print(min(ripple_close))

average = sum(ripple_close) / len(ripple_close)
print(average)

# 1.3.10 튜플 생성
portfolio = ("etc", "btc", "eth")
print(type(portfolio))

# 1.3.11 튜플 인덱싱과 슬라이싱
print(portfolio[0])
print(portfolio[0:2])

# 1.3.14 딕셔너리 생성과 추가
prices = {'btc': 8300000, 'xrp': 514}
# prices = {}
prices['eth'] = 120000
prices['yco'] = 2110
print(prices)

# 1.3.15 딕셔너리 인덱싱(only key값을 통해서)
print(prices['eth'])
print(prices['btc'])

# 1.3.17 딕셔너리 데이터 수정
prices = {'btc': 8300000, 'xrp': 514}
prices['xrp'] = 599
print(prices)

# 1.3.18 딕셔너리에서 데이터 삭제(key 값)
prices = {'btc': 8300000, 'xrp': 514}
del prices['xrp']
print(prices)

# 1.3.19 딕셔너리에서 key 값만 얻기 keys()
prices = {'btc': 8300000, 'xrp': 514}
print(prices.keys())
# dict_keys 타입 객체를 쉬운 타입으로 바꿔준다.
print(list(prices.keys()))
 
# 1.3.20 딕셔너리로부터 value 얻기
prices = {'btc': 8300000, 'xrp': 514}
print(prices.values())
print(list(prices.values()))