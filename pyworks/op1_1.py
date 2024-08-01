'''
n1 = 10
n2 = 4

print(n1 **n2) #10000 거듭제곱
print(2**3)


# 산술 연산
sum = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2

#출력
print(sum)
print(sub)
print(mul)
print(div)

'''

#실습

bread = 30
people = 4
share  = bread // people
remain = bread % people

print("빵의 개수 :",share)
print("남은 빵의 개수 :",remain)

print("빵의 개수 :" + str(share))
print("남은 빵의 개수 :" + str(remain))

print("빵의 개수 :",str(bread//people))
print("남은 빵의 개수 :",str(bread%people))

print("빵의 개수 :", bread//people)
print("남은 빵의 개수 :", bread%people)

print(f'빵의 개수 :{share}')
print(f'남은 빵의 개수 :{remain}')
