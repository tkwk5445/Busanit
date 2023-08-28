print('-' * 5, 'for문 사용하기', '-' * 5)

# 파이썬의 for문
# 파이썬의 for문은 다른 언어의 for ~ in, for each문과 동일한 기능을 하는 반복문
# 파이썬의 for문은 초기화 변수, 증감식, 반복조건을 사용자가 입력하지 않아도 됨
# 파이썬의 for문의 반복 조건은 사용되는 리스트의 크기로 결정됨

# while문과 for문의 차이점
# while문은 초기화 변수, 증감식, 반복조건이 반드시 필요함
# for문은 초기화 변수, 증감식, 반복조건이 반드시 필요하지는 않음
# while문은 사용자가 원하는 크기 만큼 반복 수행할 수 있음
# for문 지정한 객체의 크기만큼 반복 수행하기 때문에 사용자가 원하는 반복 회수를 지정할 수 없음


# 리스트 선언
test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)

print('-' * 5, 'while문으로 출력하기', '-' * 5)

count = 0

while count < len(test_list):
    print(test_list[count])
    count += 1

# 리스트를 미리 생성하고 나중에 for문으로 출력
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list1:
    print(f'변수 i의 값 : {i}')

# 리스트를 for문에 직접 입력하여 출력
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f'변수 i의 값 : {i}')

# while문으로 1 ~ 10까지 출력
count = 1
while count <= 10:
    print(f'count의 값 : {count}')
    count += 1

# range (시작숫자, 종료숫자) : 숫자 리스트를 자동 생성하는 함수
# 생성된 데이터는 리스트는 아니지만 리스트로 변환 가능함
# 매개변수가 1개만 존재할 경우 0부터 지정한 숫자까지의 리스트를 생성
# 매개변수가 2개 존재할 경우 시작 숫자부터 종료 숫자까지의 리스트를 생성
# 종료숫자는 리스트에 포함되지 않음 (종료숫자 -1 까지위 리스트 생성)
# 실제 리스트로 변환하고자 할 경우 list() 함수 사용
print(range(10))
print(range(5,10))
print(list(range(5,10)))


for i in range(10):
    print(f'i의 값 : {i}')


for i in range(5, 10):
    print(f'i의 값 : {i}')


# 문제 1) for 문을 사용하여 1 ~ 10까지의 합 구하기
hap1 = 0
for i in range(1, 11):
    hap1 += i
print(f'1부터 10까지의 합 : {hap1}')

# 문제 2) for문과 range를 사용하여 50 ~ 100까지의 총 합 구하기
hap2 = 0
for i in range(50, 101):
    hap2 += i
print(f'1부터 10까지의 합 : {hap2}')

# 문제 3) for문과 while문을 사용하여 구구단 출력
dan = 2  # 출력할 단을 지정

for i in range(1, 10):  # 1부터 9까지 반복
    result = dan * i
    print(f'{dan} x {i} = {result}')
