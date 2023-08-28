print("\n", "-" * 5, "함수 사용하기", "-" * 5)

# 변수와 연산을 이용한 출력
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


# 함수 호출
add(a=10, b=20)
add(a=100, b=200)
add(a=1000, b=2000)


# 함수 선언
def minus(a, b):
    c = a - b
    print(f"a - b = {c}")


def multiple(a, b):
    c = a * b
    print(f"a * b = {c}")


def divide(a, b):
    c = a / b
    print(f"a / b = {c}")


# 함수의 실행 : 실행하고자 하는 함수의 이름()을 입력 시 함수가 실행됨
# 해당 함수의 선언부의 내용을 확인하고 선언된 방식대로 실행해야함
# 매개변수가 없을 경우 함수이름()로 실행
# 매개변수가 있을경우 함수이름(매개변수값1, 매개변수값2, ...) 형태로 실행
# 선언된 함수를 실행 시 매개변수에 전달한 데이터의 개수가 다르면 오류 발생

minus(a=20, b=10)
multiple(a=10, b=3)
divide(a=10, b=3)


# 함수의 4가지 형태
# 1. 매개변수와 변환값이 모두 없는 형태
# 매개변수가 없기 때문에 함수 내부에서 연산에 필요한 변수를 선언하고, 사용하고, 삭제함
# 외부에서 전달되는 데이터가 없기 떄문에 연산 결과가 동일함
# 반환값이 없기 떄문에 함수 내부에서 화면 출력이 필요함
def func1():
    a = 10
    b = 20
    c = a + b
    print(f"a + b = {c}")


func1()


# 2. 매개변수는 존재하고, 반환값이 없는형태
# 연산에 필요한 데이터를 함수 외부에서 전달받아 연산을 수행함
# 외부에서 전달되는 데이터가 존재하기 때문에 연산 결과가 달라짐
# 반환값이 없기 때문에 함수 내부에서 화면 출력이 필요함
def func2(a, b):
    c = a + b
    print(f"a + b = {c}")


func2(10, 11)


# 3. 매개변수는 없고, 반환값이 존재하는 형태
# 매개변수가 없기 때문에 함수 내부에서 연산에 필요한 변수를 선언하고, 사용하고, 삭제함
# 외부에서 전달되는 데이터가 존재하기 때문에 연산 결과가 동일함
# 반환값이 존재하기 때문에 함수 내부에서 화면 출력이 필요함
def func3():
    a = 10
    b = 20
    c = a + b
    return c


result = func3()
print(f"result : {result}")
print(f"result : {result * 3}")


# 4. 매개변수는 없고, 반환값이 존재하는 형태
# 연산에 필요한 데이터를 함수 외부에서 전달받아 연산을 수행함
# 외부에서 전달되는 데이터가 존재하기 때문에 연산 결과가 달라짐
# 반환값이 존재하기 때문에 함수의 연산 결과를 외부에서 활용할 수 있음
def func4(a, b):
    c = a + b
    return c


result = func4(10, 20)
print(f"result : {result}")
print(f"result : {result + func4(result, result + result)}")


# 문제 1) 사칙연산을 하는 함수를 함수의 4가지 형태로 구현하세요
# 각 함수에서 사용되는 변수는 a, b, c로 선언
# ps) return 값을 받기 위한 변수는 result로 선언


# sum : 덧셈, 함수 2번형태
def sum(a, b, c):
    result = a + b + c
    print(f"a + b + c = {result}")


sum(10, 20, 30)


# sub : 뺄셈, 함수 3번형태
def sub():
    a = 10
    b = 2
    c = 4
    d = a - b - c
    return d


result = sub()
print(f"result : {result}")
print(f"result : {result * 3}")


# multi : 곱셈, 함수 4번형태
def multi(a, b):
    c = a * b
    return c


result = multi(10, 20)
print(f"result : {result}")


# div : 나눗셈, 함수 1번형태
def div():
    a = 100
    b = 20
    c = a / b
    print(f"a / b = {c}")


div()


# 문제2) 사용자가 지정한 단수의 구구단을 출력하는 함수를 구현
def gugudan():
    dan = int(input("출력할 구구단의 단수를 입력하세요 >> "))

    for i in range(1, 10):
        result = dan * i
        print(f"{dan} x {i} = {result}")


gugudan()
