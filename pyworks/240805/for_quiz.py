
# 실습 1
# for문 - 1부터 사용자가 입력한 수까지 정수의 합계
total = 0
num = int(input("몇까지의 합을 계산할까요?"))
for i in range(1, num+1):
    total += i
print(f'1부터 {num}까지의 합 : {total}')


# for문 - 1부터 사용자가 입력한 수까지 홀수의 합계
user_range = int(input("어디까지 계산할까요?"))
odd_total = 0
for i in range(user_range+1):
    if i % 2 != 0:      #1, 3, 5
        odd_total += i
print(f'1부터 {user_range}까지의 합 : {odd_total}')


# 실습 2
# for문 - 사용자가 입력한 수부터 거꾸로 카운트
num2 = int(input("몇 초?:"))
for i in range(num2, 0, -1):
    print(i, end=" ")
print("발사!!")

# 실습 3
# 구구단 만들기 - 사용자가 입력한 숫자의 구구단 출력
num3 = int(input("몇 단을 출력할까요? "))
result = 1
for i in range(1, 10):
    result = num3 * i
    print(f'{num3}*{i}={result}')
