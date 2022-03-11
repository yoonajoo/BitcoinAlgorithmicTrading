# https://blog.naver.com/rob_sten/222642123809
# 2.2.1 for 문
# (1) 기본 개념 
for 좌석 in ["좌석1","좌석2", "좌석3", "좌석4"] :
    print(좌석, "표 확인")

# (2)      
for value in ["가", "나", "다", "라"] :
    print(value)

# (3)
ripple = [511, 674, 678, 524]
for close in ripple :
    print(close)
    
# 2.2.3 for와 딕셔너리
# (1) key 값만 출력
cur_price = {"btc": 910000000, "xpr": 511, "dash": 3600000}
for ticket in cur_price :
    print(ticket)
    
# (2) key, value 동시 접근 후 바인딩 -> .items()
cur_price = {"btc": 910000000, "xpr": 511, "dash": 3600000}
for ticket, price in cur_price.items() :
    print(ticket, price)

# 2.2.5 while문
# 항상 조건이 참 -> True
num = 1
while True : 
    num = num + 1
    if num <= 10 :
        print(num)
        
