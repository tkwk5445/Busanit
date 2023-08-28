print("-" * 5, "break/continue문 사용하기", "-" * 5)

# break : 반복문 안에서 break문을 만날 경우 해당 반복문을 즉시 종료함
print("\n", "-" * 5, "break 사용시", "-" * 5)
dan = 5
count = 0

while count < 9:
    count += 1

    if count == 5:
        break

    print(f"{dan} x {count} = {dan * count}")

# continue : 반복문 안에서 continue문을 만날 경우 해당 반복문의 현재 루프만 즉시 종료, 다음번 루프로 이동
print("\n", "-" * 5, "continue 사용시", "-" * 5)
dan = 5
count = 0

while count < 9:
    count += 1

    if count == 5:
        continue

    print(f"{dan} x {count} = {dan * count}")

print("\n", "-" * 5, "for문에 break 적용시", "-" * 5)
for i in range(1, 10):
    if i == 5:
        break

    print(f"{dan} x {i} = {dan * i}")

# 각 제어문 (조건문, 반복문)은 서로 내부에 여러개의 제어문을 사용할 수 있음
# 조건문 안에 조건문 사용 가능, 반복문 안에 반복문 사용 가능
# 조건문 안에 반복문 사용 가능, 반복문 안에 조건문 사용 가눙

# 2중 for문 사용하기
dan = [2, 3, 4, 5, 6, 7, 8, 9]
su = [1, 3, 4, 5, 6, 7, 8, 9]

for i in dan:
    print("-" * 5, f"{i}단", "-" * 5)
    for j in su:
        print(f"{i} x {j} = {i * j}")

# 문제 1) 2중 while문을 사용하여 구구단 전체를 출력
i = 2
while i < 10:
    print("-" * 5, f"{i}단", "-" * 5)
    j = 1

    while j < 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
