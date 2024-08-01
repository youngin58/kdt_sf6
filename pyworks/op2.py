# 복합 대입 연산자

val = 1

# val = val + 10
val += 10 #11
print(val)

val -= 10 #1
print(val)

val *= 10 #10
print(val)
print(type(val))

val /= 10 #1
print(val)      # 변수가 계속 바뀌고 있다는 사실이 중요함.
print(type(val))


# 청바지 수량
jean = 0   # 정수 초기값
msg = ""  # 빈 문자열(초기값)
#jean = jean + 1
jean += 1
print("청바지 수량:", jean)
