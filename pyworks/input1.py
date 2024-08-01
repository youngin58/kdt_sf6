# 입력함수 - input(문자열)
# name = "daisy"
#name = input("이름 입력: ")
#print("당신의 이름은 " + name + "이군요")

#number = input("숫자 입력: ")
#print(number)
#print(number + 1)      #변수 number와 1의 자료형이 달라 에러남
#print(int(number) + 1)  #101 출력됨

'''
num1 = input("첫번째 수 입력: ")
num2 = input("두번째 수 입력: ")
print(type(num1))   # 자료형이 str이 나옴 
print(num1 + num2)
'''
'''
num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))
print(type(num1))   # int
print(num1 + num2)
'''
'''
#오류 처리(try ~ except)
num1 = float(input("첫번째 수 입력: "))
num2 = float(input("두번째 수 입력: "))
print(type(num1))   # 실수 - 소수점 숫자도 받을 수 있음 
print(num1 + num2)
'''

print(int(10.5))  #10

'''
#오류 처리(try ~ except 구분)
: (콜론) - 코드 블록({ })
# 다음 줄에서는 4칸 띄어쓰기(indent)
try:
    실행문(오류가 나올 수 있는 문)
except:
    오류를 처리할 수 있는 구문
'''

try:
    num1 = input("첫번째 수 입력: ")
    num2 = input("두번째 수 입력: ")
    print(int(num1)+int(num2))
except:
    print("정수를 입력해주세요")
    
