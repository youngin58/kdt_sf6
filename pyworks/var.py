# 변수와 자료형
# 자료형(type) - 숫자(정수, 실수), 문자

floor = 3 # 정수를 저장하는 floor라는 변수 # floor라는 변수에 3을 저장함
name = '정영인' # 문자열 변수 지정 시에는 꼭 ''나 "" 안에 넣어서 지정하자
weight = 2.5


print("나는",floor,"층에 살아요")
print("나는",floor,"층에 살아요", sep='') # 띄어쓰기를 없애기

print(f'나는{floor}층에 살아요') # 위와 동일기능, 변수를 중괄호 {}로 표현, f포맷
print(f"나는{floor}층에 살아요") # ''와 ""는 동일한 기능

# str(숫자) - 자료형을 변환할 필요 (숫자를 문자로 변환) 
print("이 노트북의 무게는 " + str(weight) + "kg입니다")

# f포맷 방식 출력 - 변수는 {}(중괄호)를 넣는다
print(f'이 노트북의 무게는{weight}kg 입니다')


print(name)
print("내 이름은 " + name + "입니다") # +는 연결 연산자(문자) 혹은 산술 연산자(숫자)


# type(자료형) - 자료형을 인식하는(아는) 함수
# int - 정수(integer), float - 실수(부동)
# str - 문자열(string)
print(type(floor))
print(type(weight))
print(type(name))

