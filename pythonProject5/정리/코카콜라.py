import random

total = 0

money = int(input('돈을 넣어 주세요'))

print('1번 콜라: 1200원')
print('2번 우주맛 콜라: 1900원')
print('3번 제로콜라: 1200원')
print('4번 스프라이트: 1100원')
print('5번 환타: 900원')
print('6번 닥터페퍼: 1100원')
print('7번 몬스터: 1800원')
print('8번 파워에이드: 1900원')
print('9번 네스티: 1600원')
print('10번 비타민 워터: 2100원')
print('11번 미닛메이드: 1700원')
print('12번 조지아커피:900원')
print('13번 암바사: 900원')
print('14번 마테차: 1700원')
print('s: 결제하기')
print('x: 종료하기')

while True:
    choice = input()
    if choice == '1':
        print('콜라: 1200원')
        total += 1200
        
    elif choice =='2':
        print('우주맛 콜라: 1900원')
        total += 1900

    elif choice == '3':
        print('제로콜라: 1200원')
        total += 1200

    elif choice == '4':
        print('스프라이트: 1100원')
        total += 1100

    elif choice == '5':
        print('환타: 900원')
        total += 900

    elif choice == '6':
        print('닥터페퍼: 1100원')
        total += 1100

    elif choice == '7':
        print('몬스터: 1800원')
        total += 1800

    elif choice == '8':
        print('파워에이드: 1900원')
        total += 1900

    elif choice == '9':
        print('네스티: 1600원')
        total += 1600

    elif choice == '10':
        print('비타민 워터: 2100원')
        total += 2100

    elif choice == '11':
        print('미닛메이드: 1700원')
        total += 1700

    elif choice == '12':
        print('조지아커피:900원')
        total += 900

    elif choice == '13':
        print('암바사: 900원')
        total += 900

    elif choice == '14':
        print('마테차: 1700원')
        total += 1700

    if choice == 's':
        if money < total:
            print('총 %d원입니다.금액초과입니다. 종료하겠습니다.' % (total))
            break
        else:
            print('총 %d 원입니다. 거스름돈은 %d입니다.' % (total, money-total))
            break
    elif choice == 'x':
            print("종료합니다")
            break


