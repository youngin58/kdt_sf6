"""
# 변수 선언(변수명 만드는 문법)
- 숫자로 시작하면 안됨
- 공백문자가 있으면 안됨
- 특수문자 불가 ('_' 언더바 가능)


- 에러
  1. 실행전 에러(컴파일오류) - 에디터가 미리 알려줌
  2. 실행후 에러(런타임에러)
"""

#season = "여름"
# season이라는 변수에 여름이라는 문자값을 저장함

#season2 = "여름"   : OK
#season = summer    : 런타임에러
#2season = "여름"   : 컴파일에러
#season 2 = "summer"  : 컴파일에러 - 공백
#print(season 2)

#a-ge = 13
#print(a-ge)

'''
#연습 (퀴즈2)
name = 'Harin'
name = 'Jerry'
print(name)
'''

print('***회원가입***')
user_id = 'kdt6'
user_pw = 'sf1234'
email = "overcome365@naver.com"
age = 35

print("아이디 :",user_id)
print("비밀번호 :",user_pw)
print("email :", email)
print("나이 :", age)

print(f"아이디 : {user_id}")


#소수점 처리하기
#
n1 = 10
n2 = 3
div = n1 / n2
print(type(n1))
print(type(div))
print(div)
print(f'결과값 : {div}')
print(f'결과값 : {div : .1f}')
print(f'결과값 : {div : .2f}')
print(f'결과값 : {round(div,2)}')

# 반올림 함수 - round(숫자, 자리수)
print(round(1.647,2))
