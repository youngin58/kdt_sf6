age = int(input("나이를 숫자로 입력해 주세요 : "))
card = input("결제 방법을 입력해주세요. ('카드' 또는 '현금'만 입력) : ")


if age < 8 :
    print("%d세의 카드 요금은 무료입니다 " %age)
          
elif (age >= 8) and (age < 14) :
    print("%d세의 카드 요금은 450원 입니다 " %age)

elif (age >= 14) and (age < 20) :
    if card == "카드" :
        print("%d세의 카드 요금은 720원 입니다 " %age)

    else :
        print("%d세의 현금 요금은 1000원 입니다 " %age)

elif (age >= 20) and (age < 75) :
    if card == "카드" :
        print("%d세의 카드 요금은 1200원 입니다 " %age)

    else :
        print("%d세의 현금 요금은 1300원 입니다 " %age)

else :
    print("%d세의 카드 요금은 무료입니다 " %age)
    
    
    
    
