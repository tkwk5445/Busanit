print("\n", "-" * 5, "함수 사용하기", "-" * 5)

a = 10
b = 20
c = a + b

print(f"a + b = {c}")

a = 100
b = 200
c = a + b

print(f"a + b = {c}")

a = 1000
b = 2000
c = a + b

print(f"a + b = {c}")


# 함수 선언
def add(a, b):
    c = a + b
    print(f"a + b = {c}")


add(a=10, b=20)
add(a=100, b=200)
add(a=1000, b=2000)


def minus(a, b):
    c = a - b
    print(f"a-b={c}")


def multiple(a, b):
    c = a * b
    print(f"a*b={c}")


def multiple(a, b):
    c = a / b
    print(f"a/b={c}")
