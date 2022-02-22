# 95. (1)superMario 절차 지향 프로그래밍
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

# 97. class
# (1) int 타입
a = 3
print(type(a))
print(a.bit_length())   # a에 대한 비트 길이 출력

# (2) string 타입
b = "python"
print(type(b))
print(b.upper())