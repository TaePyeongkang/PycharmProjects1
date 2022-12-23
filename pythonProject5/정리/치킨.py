# import random
# # 한 주
# def week(partj):
#     menu = {1: ['후라이드 치킨', 18000],
#             2: ['양념 치킨', 19000],
#             3: ['간장 치킨', 19000],
#             4: ['후라이드 치킨 순살', 17000],
#             5: ['양념 치킨 순살', 18000],
#             6: ['간장 치킨 순살', 18000],
#             7: ['마른오징어', 8000],
#             8: ['과일안주', 15000],
#             9: ['포테이토 후라이', 5000],
#             10: ['쥐포', 7000],
#             11: ['모듬튀김', 12000],
#             12: ['테라', 5000],
#             13: ['카스', 4000],
#             14: ['오비라거', 4500],
#             15: ['클라우드', 4500],
#             16: ['콜라', 2500],
#             17: ['사이다', 2000],
#             18: ['쿨피스', 1000],
#             19: ['오뎅탕', 7000],
#             20: ['떡볶이', 7000]}
#
#     part = 0  # 알바 인원 변수
#     part_cost = 1500000  # 알바비 변수
#     refund = 0
#     money = 0
#     turn = 0
#     for j in range(1,8):
#         print('=' * 150,j,'일차')
#         customer = random.randint(1, 100*partj)
#         print('손님수', customer,'명')
#         for k in range(1, customer + 1):
#             order = random.randint(1, 5)
#             print('주문수', order, '개')
#             for i in range(1,order+1):
#                 cl = 0
#                 k = random.randint(1, 20)
#                 money += menu[k][1]
#                 # print(menu[i][0],'는',menu[i][1],'원 입니다')
#                 customer_claim = random.randint(1,100)
#                 if customer_claim <= 15:
#                    cl += 1
#                    # print('환불', cl , '수')
#                    refund += (2 * menu[k][1])
#                    print('='*50,'환불금액은', 2 * menu[k][1],'원 입니다')
#
#             if money >= part_cost:
#                 part = (money-refund) // part_cost
#         # turn += 1
#         # print('횟수 %d' %(turn))
#         # if turn > 5:
#         #     if money > 500000000:
#         #         print('프랜차이즈 개설')
#         #
#         #     else:
#         #         print('게임오버')
#
#
#     print('='*50,'수익은 %d원 입니다, 총 환불 금액은 %d원 입니다' % (money,refund))
#     print('='*200,'총 수익은 %d원 입니다' %(money-refund))
#     print('알바생 수는 %d 명입니다' % (part))
#     # print('='*180)
#     print('=' * 300)
#     return part
#
# week(week(week(week(1))))
import random


# def week_sale():
#     for i in (1,8):
#         part = 0
#         money = 0
#         part_cost = 1500000
#         refund = 0
#         menu = {1: ['후라이드 치킨', 18000],
#                 2: ['양념 치킨', 19000],
#                 3: ['간장 치킨', 19000],
#                 4: ['후라이드 치킨 순살', 17000],
#                 5: ['양념 치킨 순살', 18000],
#                 6: ['간장 치킨 순살', 18000],
#                 7: ['마른오징어', 8000],
#                 8: ['과일안주', 15000],
#                 9: ['포테이토 후라이', 5000],
#                 10: ['쥐포', 7000],
#                 11: ['모듬튀김', 12000],
#                 12: ['테라', 5000],
#                 13: ['카스', 4000],
#                 14: ['오비라거', 4500],
#                 15: ['클라우드', 4500],
#                 16: ['콜라', 2500],
#                 17: ['사이다', 2000],
#                 18: ['쿨피스', 1000],
#                 19: ['오뎅탕', 7000],
#                 20: ['떡볶이', 7000]}
#
#         customer = random.randint(1,100)
#         for j in range(1, customer + 1):
#             order = random.randint(1,5)
#             for k in range(1,order + 1):
#                 k = random.randint(1,20)



# def month ():
#     menu = {1: ['후라이드 치킨', 18000],
#             2: ['양념 치킨', 19000],
#             3: ['간장 치킨', 19000],
#             4: ['후라이드 치킨 순살', 17000],
#             5: ['양념 치킨 순살', 18000],
#             6: ['간장 치킨 순살', 18000],
#             7: ['마른오징어', 8000],
#             8: ['과일안주', 15000],
#             9: ['포테이토 후라이', 5000],
#             10: ['쥐포', 7000],
#             11: ['모듬튀김', 12000],
#             12: ['테라', 5000],
#             13: ['카스', 4000],
#             14: ['오비라거', 4500],
#             15: ['클라우드', 4500],
#             16: ['콜라', 2500],
#             17: ['사이다', 2000],
#             18: ['쿨피스', 1000],
#             19: ['오뎅탕', 7000],
#             20: ['떡볶이', 7000]}
#
#     for i in range(1,5):
#         print(i,'주차')

# def day ():
#     for i in range(0,1):
money = 10000000
part_cost = 1500000

def guest(part):
    if part == 0:
        customer = random.randint(1, 100)
    else:
        customer = random.randint(1, 100 * part)
    print("오늘 올 손님 수는", customer, "명")
    customer_claim = customer * 15 // 100
    print("환불 요구하는 사람", customer_claim, "명")
    return customer, customer_claim

def employ(week,money:int):
  part = 0
  while 1:
    if week > 1:
      print('알바생을 몇명 고용 할까요?')
      result = money // part_cost
      part = int(input('최대 고용 가능 수: (%d명)' % (result)))
      if part > result:
        print('최대 고용 인원 수를 초과 다시 입력해 주세요.')
      else:
        money -= part * part_cost
        print(f'알바고용후 잔액: {money:,}원')
        return part, money
    else:
      return part,money

for week in range(1, 5):
    print(week, '주차')
    a = (week, money)
    b = employ(a[0],a[1])
    part = b[0]
    c = guest(part)
    customer = c[0]
    customer_claim = c[1]
    print("손님", customer, "명 환불 요구하는사람", customer_claim)
    money = b[1]
    print(f'part: {part}, money: {money:,}원')