#비교 연산- >,>=,<,<=,==,!=
#결과:'bool'자료(True,False)
print(2>1) #True
b1 = 2>1
print(b1)
print(type(b1))

b2 = (2==1)


# 논리 연산 - and(&&), or(||), not(~)
# and - 2가지 이상의 조건에서 모두 참일때는 참(True)
logic1 = (2>1) and (2==1) #True and False -> False
print(logic1)

#or
logic2 = (2>1) or (2==1) #두 가지 이상의 조건에서 하나의 조건만 참.

#not
logic3 = not(2!=1)

#  논리 연산 예제
age = 17
under_17 = age < 20
print(not under_20)

# 논리곱
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

# 논리합
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

# 논리부정
print (not True) # False
print (not False) # True