# 반복문 while
print("-" * 5, "정상적인 while문 예제", "-" * 5)
tree_hit = 0

while tree_hit < 10:
    tree_hit += 1
    print(f"나무를 {tree_hit}번 찍었습니다.")

    if tree_hit == 10:
        print("나무가 넘어갑니다")

# while 문 사용시 주의사항
# 1. while문 사용 시 반복 조건이 처음부터 false가 나오게 되면 while문을 한 번도 실행하지 않음
# 2. 증감식을 입력하지 않을 경우 무한 루프에 빠질 수 있음
# 3. while문은 증감식의 위치에 따라 결과 값이 다르게 표현될 수 있음.

print("-" * 5, "주의사항 1번 while문 예제", "-" * 5)
tree_hit = 0

while tree_hit > 10:
    tree_hit += 1
    print(f"나무를 {tree_hit}번 찍었습니다.")

    if tree_hit == 10:
        print("나무가 넘어갑니다")

""" print('-' * 5, '주의사항 2번 while문 예제', '-' * 5)
tree_hit = 0

# 증감식이 없어서 반복 조건의 결과값이 늘 true가 됨
while tree_hit < 10:
    # 증감식
    # tree_hit += 1
    print(f'나무를 {tree_hit}번 찍었습니다.')

    if tree_hit == 10:
        print('나무가 넘어갑니다') """

print("-" * 5, "주의사항 3번 while문 예제", "-" * 5)
tree_hit = 0

while tree_hit < 10:
    # 1번 위치
    tree_hit += 1

    print(f"나무를 {tree_hit}번 찍었습니다.")

    # 2번 위치
    tree_hit += 1

    if tree_hit == 10:
        print("나무가 넘어갑니다")

    # 3번 위치
    tree_hit += 1
