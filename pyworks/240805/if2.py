# 다중 조건문
"""
if 조건1:
    실행문(조건1 참일때)
elif 조건2:
    실행문(조건2 참일때)
else:
    실행문(조건1과 2가 모두 거짓일때)
"""
'''
age = 33
if age < 20:
    print("미성년자 입니다.")
elif age < 30:
    print("20대 입니다.")
elif age < 40:
    print("30대 입니다.")
else:
    print("이제는 중년...")
print(f'나이는 {age}세 입니다.')
'''

# 연령이 20대인 경우 성별이 여 이면 "20대 여성입니다"로 출력하고
# 남 이면 "20대 남성입니다"로 출력
age = int(input("나이를 입력하세요: "))
if 0 <= age < 20:  #다른 언어에서는 and로 구분해서 조건 넣어야 함.
    print("미성년자 입니다.")
elif 20 <= age < 30:
    gender = input("여 or 남으로 입력해 주세요: ")
    if gender == "여":
        print("20대 여성입니다.")
    else :
        print("20대 남성입니다.")
elif 30 <= age < 40:
    print("30대 입니다.")
else:
    print("이제는 중년...")
print(f'나이는 {age}세 입니다.')