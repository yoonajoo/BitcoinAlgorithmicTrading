# https://blog.naver.com/rob_sten/222655171622
# 95. (1)superMario 절차 지향 프로그래밍
from sympy import primefactors


pos = 0

def forward(pos):
    return pos + 20

pos = forward(pos)
print(pos)

# 95. (2)superMario class 객체 지향 프로그래밍
class superMario:
    def __init__(self):
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20

mario = superMario()
mario.forward()
print(mario.pos)

# 96. (1)2players superMario 절차 지향 프로그래밍
p1_pos = 0
p2_pos = 0

def forward(pos):
    return pos + 20

p1_pos = forward(p1_pos)
p2_pos = forward(p2_pos)
print(p1_pos)
print(p2_pos)

# 96. (2)2players superMario class 객체 지향 프로그래밍
class superMario:
    def __init__(self) -> None:
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20

mario_p1 = superMario()
mario_p2 = superMario()
mario_p1.forward()
mario_p2.forward()

print(mario_p1.pos)
print(mario_p2.pos)

# 97. class (1) int 타입
a = 3
print(type(a))
print(a.bit_length())   # a에 대한 비트 길이 출력

# 97. class (2) string 타입
b = "python"
print(type(b))
print(b.upper())

# 100. 클래스에 메서드 추가하기 기본 값
class myClass:
    def method(self):
        print("method")
        
obj = myClass()
obj.method()

# 101. add() 함수 추가하기 -> 인자 세 개 add(self,a,b)
class MyClass:
    def add(self,a,b):
        return a + b

obj = MyClass()
ret = obj.add(4,6)
print(ret) 

# 103. 붕어빵틀 class로 쉽게 이해하기
class 붕어빵틀:
    def 팥소넣기(self, 팥소):
        self.팥소 = 팥소
        
붕어빵1 = 붕어빵틀()
붕어빵2 = 붕어빵틀()

붕어빵1.팥소넣기("초코맛팥소")
붕어빵2.팥소넣기("딸기맛팥소")

print(붕어빵1.팥소)
print(붕어빵2.팥소)

# 104. 초기화자(기본)
class 붕어빵틀:
    def __init__(self):
        self.팥소 = "초코맛팥소"

붕어빵1 = 붕어빵틀()
print(붕어빵1.팥소)

# 105. customer class 만들기
class customer:
    def __init__(self, id , name):
        self.id = id
        self.name = name

customer1 = customer(1, "김진수")
customer2 = customer(2, "백두산") 

# 107. 클래스
class parent:
    def sing(self):
        print("sing a song")

father = parent()
father.sing()

# 108. class inheritance 클래스 상속
class Parent:
    def sing(self):
        print("sing a song song!")

class LuckyChild(Parent):
    pass

luckyboy = LuckyChild()
luckyboy.sing()

# 109. 클래스 상속
class Parent:
    def sing(self):
        print("sing a song :)")

class LuckyChild(Parent):
    def dance(self):
        print("Suffle dance!")

luckyboy = LuckyChild()
luckyboy.sing()
luckyboy.dance()