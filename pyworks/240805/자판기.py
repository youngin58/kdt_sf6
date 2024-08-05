# 과제 1
vending_machine = ['게토레이','레쓰비','생수','이프로']

while True:
    print("=============== RESTART")
    order = input("마시고 싶은 음료? ")
    if order in vending_machine:
        vending_machine.remove(order) # 입력된 주문 삭제
        print(order, "드릴게요")
        print("남은 음료는", vending_machine)
    else:
        print(f"{order}는 지금 없네요")