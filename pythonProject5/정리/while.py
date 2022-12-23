# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다.' % (treeHit))
#     if treeHit == 10:
#         print('나무가 넘어갑니다')
#
# hit = 1
# for i in range(1,11):
#     print('나무를 %d번 찍었습니다' %(hit))
#     hit += 1
#     if i == 10:
#         print('나무가 넘어갑니다')

# hit = 0
# for i in range(1,11):
#     hit += 1
#     print('나무를 %d번 찍었습니다' %(hit))
#     if i == 10:
#         print('나무가 넘어갑니다')

# coffee = 5
# print('커피 가격은 300원 입니다')
# money = int(input('돈을 넣어주세요'))
# while 1:
#     if  money == 300:
#         print('커피 제조중 입니다')
#         print('커피를 가져가세요')
#         coffee -=1
#         print('현재 남은 커피는 %d개 입니다' % (coffee))
#         # break
#     elif money < 300:
#         print('돈이 부족합니다')
#         print('돈을 반환해 가세요')
#         break
#     else:
#         print('커피 제조중 입니다')
#         print('거스름돈은 %d 원 입니다' % (money-300))
#         print('커피를 가져가세요')
#         coffee -=1
#         print('현재 남은 커피는 %d개 입니다' % (coffee))
#         # break
#     if coffee == 0:
#         print('커피가 다 떨어졌습니다')
#         break

# yuzaTea = 1200
# coffee = 500
# cocoa = 300
# total = 0
# print('유자차 1번')
# print('커피 2번')
# print('코코아 3번')
# money = int(input('돈을 입력하세요'))
# for i in :
#     choice = input()
#     if choice == 1:
#         print('유자차를 선택 하셨습니다')
#         total += yuzaTea
#         print('총 금액은 %d원 입니다' %(total))
#
#     elif choice == 2:
#         print('커피를 선택 하셨습니다')
#         total += coffee
#
#     else:
#         print('코코아를 선택 하셨습니다')
#         total += cocoa

count = 0
for i in range(0 , 21):
    for j in range(0 , 9):
        for k in range(0 , 34):
            if(i * 500) + (j * 1200) + (k * 300) <= 10000:
                print(f'커피{i}개, 유자차{j}개, 코코아{k}개')
                count += 1
                print('경우의 수는', end='')
                print(count)



# yuzaTea = 1200
# coffee = 500
# cocoa = 300
# total = 0
# print('잔돈 반환은 아무 키 누르세요')
# print('1번 유자차 1200원')
# print('2번 코코아 300원')
# print('3번 커피 500원')
#
# money = int(input('돈을 넣어 주세요'))
# # for i in range(0,34):#1번 자판기
# while True:
#     print('번호 선택하세요')
#     choice = input()
#     if money
#         if choice == '1':
#             print('유자차')
#             total += 1200
#             print('총 금액은 %d원 입니다' % (total))
#         elif choice == '2':
#             print('코코아')
#             total += 300
#             print('총 금액은 %d원 입니다' % (total))
#         else:
#             print('커피')
#             total += 500
#             print('총 금액은 %d원 입니다' % (total))