
#실습3 문제1번
name1 = input("이름을 입력하세요.")
age1 = input("나이를 입력하세요.")
print(f"안녕하세요! {name1}님 ({age1}세)")


#실습3 문제2번
try:
    name2 = input("이름을 입력하세요.")
    birth = int(input("태어난 년도를 입력하세요."))
    year = int(input("올해 년도를 입력하세요."))
    age = int(year-birth)
    print(f'올해는 {year}년, {name2}님의 나이는 {age}세 입니다.')
    #print("올해는"+str(year)+"년,"+name2+"님의 나이는"+str(year-birth)+"세 입니다.")
except ValueError:
    print("숫자로 꼭 입력해 주세요")

