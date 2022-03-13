# https://blog.naver.com/rob_sten/222642123809
# 2.3 함수
def get_min_order(ticket) :
    min_order = None 
    if ticket == "ETC" :
        min_order = 0.1
    elif ticket == "ETH" :
         min_order = 0.5
    elif ticket == "BTC" :
         min_order = 0.01
    elif ticket == "XRP" :
         min_order = 10
    else :
        min_order = 0.005
    return min_order

min_order = get_min_order("BTC")
print(min_order)

# 2.3.2 함수는 이름표
def 별찍기() :
    print("*" * 40)
    print("*" * 40)

별찍기()