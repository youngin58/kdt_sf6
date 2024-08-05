# 다중 if 실습
'''
score = int(input("점수 입력 :"))
if score >= 90:
    print("A 등급입니다.")
elif score >= 80 and score <90:
        print("B 등급입니다.")
elif score >= 70 and score <80:
        print("C 등급입니다.")
elif score >= 60 and score <70:
        print("D 등급입니다.")
else:
        print("E 등급입니다.")
'''

# 다중 if 실습
score = int(input("점수 입력 :"))
grade = "" # 빈 문자열

if score >= 90:
    grade = "A"
elif score >= 80 and score <90:
    grade = "B"
elif score >= 70 and score <80:
    grade = "C"
elif score >= 60 and score <70:
    grade = "D"
else:
    grade = "E"
print(f"{grade} 등급입니다.")