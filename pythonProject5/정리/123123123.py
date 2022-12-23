# print(max(C, key=B.get), "1위")
# C_1 = max(C, key=B.get)
# del B[max(C, key=B.get)]
# print(max(C, key=B.get), "2위")
# C_2 = max(C, key=B.get)
#
# list = ['A', 'B', 'C', 'D', 'E']
# for alpha in list :
#     print()


#1~6경기 짜기

# dicA = {'네덜란드' : 0 ,'카타르' : 0 ,'세네갈' : 0 ,'에콰도르' : 0}
# list = [1,2,3,4]
# for i in list:
#
# for i, e in enumerate(['1','2','3','4']):
#     print('i = %d, e = %s' %(i, e))
#
# for i in range(1,4):
#     n1 = i
#     for j in range(i+1,5):
#         print(i,j)
# import random
# a0 =random.randrange(1,3)
# if a0 >= 8: #승률 70%와 60%
#     print(a0)
#     print(' 승리')
#
#
# elif a0 == 7:
#     print('무승부')
#
#
#
# else:
#     print(a0)
#     print(' 승리')
#
#

#
# import random
# list = ['네덜란드','세네갈','카타르','에콰도르']
# for i in list :
#     a = random.randrange(1,4)
#     print(i)
#     if a == 1:
#         print("승리")
#     elif a == 2:
#         print('패배')
#     else:
#         print('무승부')
#
# dicA = {'네덜란드' : 0 ,'카타르' : 0 ,'세네갈' : 0 ,'에콰도르' : 0}
# num = [dicA]
#
# for i in num:
#     print(i)

# vp = [{'name': 'team1', 'pts': 0}, {'name': 'team2', 'pts': 0}, {'name': 'team3', 'pts': 0},
#       {'name': 'team4', 'pts': 0}, {'name': 'team5', 'pts': 0}, {'name': 'team6', 'pts': 0},
#       {'name': 'team7', 'pts': 0}, {'name': 'team8', 'pts': 0}, {'name': 'team9', 'pts': 0},
#       {'name': 'team10', 'pts': 0}, {'name': 'team11', 'pts': 0}, {'name': 'team12', 'pts': 0},
#       {'name': 'team13', 'pts': 0}, {'name': 'team14', 'pts': 0}, {'name': 'team15', 'pts': 0},
#       {'name': 'team16', 'pts': 0}, {'name': 'team17', 'pts': 0}, {'name': 'team18', 'pts': 0},
#       {'name': 'team19', 'pts': 0}, {'name': 'team20', 'pts': 0}]
#
# def matchday(winner, loser, draw):
#     if draw == False:
#         print(f"{winner} (이)가 {loser} 에게 승리하였습니다")
#         for i in vp:
#             if i['name'] == winner:
#                 i['pts'] += 3
#     if draw == True:
#         print(f"{winner} 와 {loser} (이)가 무승부를 기록하였습니다")
#         for i in vp:
#             if i['name'] == winner or i['name'] == loser:
#                 i['pts'] += 1
#
#
#
#
# for mdf in range(19):
#     # 리그 전반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로
#     # 19번의 라운드를 반복하되 라운드당 10경기를 치르는 시스템으로 정한다
#     olf = []
#     # 전반부에 한번 붙은 팀이 다시 만나는 일이 없도록 중복방지 리스트 생성
#     mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#     # vp의 인덱스들
#     for matchcount in range(10):
#         # 한라운드 리그 경기 수(10경기)
#         rd1 = random.choice(mdindex)
#         # vp의 인덱스가 될 숫자중 하나 선택(mdindex중 하나 선택)
#         mdindex.remove(rd1)
#         # 겹치지 않도록 제거 (순열 조합 같은 느낌으로 이미 뽑은건 제거해서 다시 못뽑게함)
#         rd2 = random.choice(mdindex)
#         # 두번째 숫자 선택(겹칠일 없음)
#         mdindex.append(rd1)
#         # 계속 삭제되있으면 다음에도 안뽑히므로 다시 추가
#         while {rd1, rd2} in olf:
#             # 두 인덱스가 이미 선택된적이 있었을경우 반복해서 계속 랜덤으로 선택
#             # 이때 인덱스가 순서와 상관이 없기때문에 set 사용
#             rd1 = random.choice(mdindex)
#             mdindex.remove(rd1)
#             # 중복되지 않도록 삭제
#             rd2 = random.choice(mdindex)
#             mdindex.append(rd1)
#             # 고른후 다시 추가
#
#         mdindex.remove(rd1)
#         mdindex.remove(rd2)
#         # 반복문을 나온뒤 둘다 삭제
#         olf.append({rd1, rd2})
#         # 중복방지 리스트에 추가
#
#         order = [rd1, rd2]
#         # 승패팀 결정할 리스트에 두팀 추가
#         orderr = random.choice(order)
#         # rd1 과 rd2중 하나 선택(승패가 나뉠경우 승리팀과 패배팀 반반의 확률로 결정
#         # 무승부시 표기되는 순서만 바뀜
#         order.remove(orderr)
#         # 겹치는 것을 방지하기 위해 선택된 팀을 order에서 삭제
#         matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
#         # 처음에 선택된 팀의 이름  여기서 인덱스가 0인 이유는 요소가 두개인 order에서 하나가 삭제되어 요소가 하나밖에 안남았기 때문
# for mds in range(19):
#     # 리그 후반부는 190경기(실제로 프리미어리그 총 경기수는 380경기)로
#     # 19번의 라운드를 반복하되 라운드당 10경기를 치르는 시스템으로 정한다
#     olf = []
#     # 전반부에 한번 붙은 팀이 다시 만나는 일이 없도록 중복방지 리스트 생성
#     mdindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] \
#         # vp의 인덱스들
#     for matchcount in range(10):
#         # 한라운드 리그 경기 수(10경기)
#         rd1 = random.choice(mdindex)
#         # vp의 인덱스가 될 숫자중 하나 선택(mdindex중 하나 선택)
#         mdindex.remove(rd1)
#         # 겹치지 않도록 제거 (순열 조합 같은 느낌으로 이미 뽑은건 제거해서 다시 못뽑게함)
#         rd2 = random.choice(mdindex)
#         # 두번째 숫자 선택(겹칠일 없음)
#         mdindex.append(rd1)
#         # 계속 삭제되있으면 다음에도 안뽑히므로 다시 추가
#         while {rd1, rd2} in olf:
#             # 두 인덱스가 이미 선택된적이 있었을경우 반복해서 계속 랜덤으로 선택
#             rd1 = random.choice(mdindex)
#             mdindex.remove(rd1)
#             # 중복되지 않도록 삭제
#             rd2 = random.choice(mdindex)
#             mdindex.append(rd1)
#             # 고른후 다시 추가
#
#         mdindex.remove(rd1)
#         mdindex.remove(rd2)
#         # 반복문을 나온뒤 둘다 삭제
#         olf.append({rd1, rd2})
#         # 중복방지 리스트에 추가
#
#         order = [rd1, rd2]
#         # 승패팀 결정할 리스트에 두팀 추가
#         orderr = random.choice(order)
#         # rd1 과 rd2중 하나 선택(승패가 나뉠경우 승리팀과 패배팀 반반의 확률로 결정
#         # 무승부시 표기되는 순서만 바뀜
#         order.remove(orderr)
#         # 겹치는 것을 방지하기 위해 선택된 팀을 order에서 삭제
#         matchday(vp[orderr]['name'], vp[order[0]]['name'], random.choice([True, False]))
#         # 처음에 선택된 팀의 이름  여기서 인덱스가 0인 이유는 요소가 두개인 order에서 하나가 삭제되어 요소가 하나밖에 안남았기 때문
# vp.sort(key=lambda vir: vir['pts'], reverse=True)
# # 승점 역순으로 (큰것부터) vp 리스트 정렬(기존의 내용 필요없으므로 덮어씌우는 sort 사용)
# count = 0
# for i in vp:
#     count += 1
#     # count 하나씩 증가시키면서 등수 올림
#     print(f"{count}위 : {i['name']} {i['pts']}pts")
#
# print(f"{vp[0]['name']} 프리미어리그 우승!")
# # 승점 역순으로 정렬된 vp의 첫번째 요소. 즉 1위팀
# print(f"{vp[17]['name']} 2부리그로 강등")
# print(f"{vp[18]['name']} 2부리그로 강등")
# print(f"{vp[19]['name']} 2부리그로 강등")
# # 마지막 3개의 요소들, 강등팀



# A = {'네덜란드':0, '세네갈':0, '에콰도르':0, '카타르':0}
# B = {'잉글랜드':0, '웨일스':0, '미국':0, '이란':0}
# C = {'아르헨티나':0, '멕시코':0, '폴란드':0, '사우디아라비아':0}
# D = {'프랑스':0, '튀니지':0, '덴마크':0, '호주':0}
# E = {'스페인':0, '독일':0, '일본':0, '코스타리카':0}
# F = {'벨기에':0, '크로아티아':0, '모로코':0, '캐나다':0}
# G = {'브라질':0, '세르비아':0, '카메룬':0, '스위스':0}
# H = {'포루투갈':0, '우루과이':0, '가나':0, '대한민국':0}
#
# world = [A,B,C,D,E,F,G,H]
# for i in world:
#     print(i)


# dicA = {1 :'네덜란드', 2 :'세네갈', 3 :'에콰도르', 4 :'카타르'}
# for i in list :
#     print(i)
#     for j in list:
#         print(j,end='')

# for i in dicA:

#     print(dicA.get(i))
#
#     for j in dicA:
#         # j += 1
#         print(dicA.get(j+1))
# a11 = 0
# a12 = 0
# a13 = 0
# a14 = 0
#
# import random
# dicA = {1 :'네덜란드', 2 :'세네갈', 3 :'에콰도르', 4 :'카타르'}
# list = [70,60,40,20]
# for i in range(1,5):
#     for j in range(i+1,5): # 중복 없이 만나게 하기
#         print(dicA[i],end='') #6경기 만들기
#         print(' vs ',end='')
#         print(dicA[j])


# for i in range(1,5):
#     print(i)
#     for j in range(i+1,5):
#         print(j)











# print(menu)
# import random
# for i in range(1,5):
#         print(i,'주차')
#         for j in range(1,8):
#                 customer = random.randrange(1, 101) #손님 1명부터 100명 랜덤
#                 order = random.randrange(1,6) # 음식 주문 1개부터 5개 랜덤
#                 print('손님 방문 수 : ', customer,'명')
#                 # print(customer)
#                 # print('음식 주문 수 :', order,'개')
#                 # print(order)
#                   ('음식 주문:')
# import random
# def sale():

# 하루 장사 하기
# 1부터 100명 방문
        # customer = random.randrange(1,101)
# 순서대로 랜덤으로 1~5개 메뉴 주문
        # order = random.randrange(1,6)
# 결제 그후 다음 손님
        # pay = ((order * i[]) * customer)
#계산
#for i in range(order):
        #choose_menu = random.randrange(1,21)
        #for j in range(1,21):
                #if choose_menu == j:
                        #pay += menu[j][]


# def hollzzak(a):
#     if a % 2 == 0:
#         # print('짝수')
#         return '짝수'
#     else:
#         # print('홀수')
#         return '홀수'
# hollzzak(6)
# print(hollzzak(6))

# def twotimes(x):
#     y = 2 * x
#     return y
#
#
# print(twotimes(7))
import random
def week1():
    menu = {1: ['후라이드 치킨', 18000],
            2: ['양념 치킨', 19000],
            3: ['간장 치킨', 19000],
            4: ['후라이드 치킨 순살', 17000],
            5: ['양념 치킨 순살', 18000],
            6: ['간장 치킨 순살', 18000],
            7: ['마른오징어', 8000],
            8: ['과일안주', 15000],
            9: ['포테이토 후라이', 5000],
            10: ['쥐포', 7000],
            11: ['모듬튀김', 12000],
            12: ['테라', 5000],
            13: ['카스', 4000],
            14: ['오비라거', 4500],
            15: ['클라우드', 4500],
            16: ['콜라', 2500],
            17: ['사이다', 2000],
            18: ['쿨피스', 1000],
            19: ['오뎅탕', 7000],
            20: ['떡볶이', 7000]}
    part_cost = 1500000  # 알바비 변수
    refund = 0
    money = 0
    turn = 0
    for j in range(1,8):
        print('=' * 150,j,'일차')
        customer = random.randint(1, 100)
        print('손님수', customer,'명')
        for k in range(1, customer + 1):
            order = random.randint(1, 5)
            print('주문수', order, '개')
            for i in range(1,order+1):
                cl = 0
                k = random.randint(1, 20)
                money += menu[k][1]
                # print(menu[i][0],'는',menu[i][1],'원 입니다')
                customer_claim = random.randint(1,100)
                if customer_claim <= 15:
                   cl += 1
                   # print('환불', cl , '수')
                   refund += (2 * menu[k][1])
                   print('='*50,'환불금액은', 2 * menu[k][1],'원 입니다')

            if money >= part_cost:
                part = (money-refund) // part_cost