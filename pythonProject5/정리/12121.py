# import random
# a11 = 0
# a12 = 0
# a13 = 0
# a14 = 0
# H = {'포루투갈':a11, '우루과이':a12, '가나':a13, '대한민국':a14}
# print('------------------------------------------')
# print('\t  H조 제1경기')
# print('포루투갈   vs 우루과이 ')
#
# a0 = random.randrange(1,15)
# if a0 >= 8: #승률 70%와 60%
#     print(a0)
#     print('포루투갈 승리')
#     a11 += 3
#     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
# elif a0 == 7:
#     print('무승부')
#     a11 += 1
#     a12 += 1
#     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
#
# else:
#     print(a0)
#     print('우루과이 승리')
#     a12 += 3
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
#
# print('------------------------------------------')
# print('\t  H조 제2경기')
# print('포루투갈   vs 가나 ')
# a01 = random.randrange(1,15)
# if a01 >= 7: #승률 70%와 40%
#     print(a01)
#     print('포루투갈 승리')
#     a11 += 3
#     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
# elif a01 == 5 and a01 == 6:
#     print('무승부')
#     a11 += 1
#     a13 += 1
#     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
#     print('가나 현재 승점은 %d 입니다.' % (a13))
#
# else:
#     print(a01)
#     print('가나 승리')
#     a13 += 3
#     print('가나 현재 승점은 %d 입니다.' % (a13))
#
# print('------------------------------------------')
# print('\t  H조 제3경기')
# print('포루투갈   vs 대한민국 ')
# a02 = random.randrange(1,15)
#
# if a02 >= 7:
#      print(a02)  # 승률 70%와 20%
#      print('포루투갈 승리')
#      a11 += 3
#      print('포루투갈 현재 승점은 %d 입니다.' % (a11))
# elif a02 > 2 and a02 < 7:
#     print('무승부')
#     a11 += 1
#     a14 += 1
#     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
# else:
#     print(a02)
#     print('대한민국 승리')
#     a14 += 3
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
# print('------------------------------------------')
# print('\t  H조 제4경기')
# print('우루과이   vs 가나 ')
# a03 = random.randrange(1,15)
# if a03 >= 8: #승률 60%와 40%
#     print(a03)
#     print('우루과이 승리')
#     a12 += 3
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
# elif a03 == 6 and a03 == 7:
#     print('무승부')
#     a12 += 1
#     a13 += 1
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
#     print('가나 현재 승점은 %d 입니다.' % (a13))
#
# else:
#     print(a03)
#     print('가나 승리')
#     a13 += 3
#     print('가나 현재 승점은 %d 입니다.' % (a13))
#
#
# print('------------------------------------------')
# print('\t  H조 제5경기')
# print('우루과이   vs 대한민국 ')
# a04 = random.randrange(1,15)
# if a04 >= 8: #승률 60%와 20%
#     print(a04)
#     print('우루과이 승리')
#     a12 += 3
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
# elif a04 == 6 and a04 == 7:
#     print('무승부')
#     a12 += 1
#     a14 += 1
#     print('우루과이 현재 승점은 %d 입니다.' % (a12))
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
# else:
#     print(a04)
#     print('대한민국 승리')
#     a14 += 3
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
# print('------------------------------------------')
# print('\t  H조 제6경기')
# print('가나  vs 대한민국 ')
# a05 = random.randrange(1,15)
# if a05 >= 9: #승률 40%와 20%
#     print(a05)
#     print('가나 승리')
#     a13 += 3
#     print('가나 현재 승점은 %d 입니다.' % (a13))
# elif a05 > 3 and a05 < 9:
#     print('무승부')
#     a11 += 1
#     a14 += 1
#     print('가나 현재 승점은 %d 입니다.' % (a13))
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
# else:
#     print(a05)
#     print('대한민국 승리')
#     a14 += 3
#     print('대한민국 현재 승점은 %d 입니다.' % (a14))
#
#
# print('최종승점은:')
# print('총 포루투갈 승점은 %d,  총 우루과이 승점은 %d, 총 가나 승점은 %d, 총 대한민국 승점은 %d 입니다.' % (a11,a12,a13,a14))
#
#
# print('------------------------------------------------------------------------------------')

#
# game_16=[]
#
# team_a={0:'A',1:["네덜란드",6,7],2:["세네갈",3,6],3:["에콰도르",8,4],4:["카타르",1,2]}
# point_list=[team_a[1][1],team_a[2][1],team_a[3][1],team_a[4][1]]             #승점 리스트를 새로 만들어
# team_list=[team_a[1][0],team_a[2][0],team_a[3][0],team_a[4][0]]              #팀 리스트도 하나 만들어
# temp_po=point_list[:]                                                        #승점 리스트의 데이터가 변경될테니까 카피본 만들기
#
# m = max(temp_po)                                                             #최대값
# position = point_list.index(m)                                                      #최대값 위치
# game_16.append(team_list[position])                                          #최대값 위치를 통해서 해당 국가 16강 진출리스트에 추가
# print(team_list[position])
# del point_list[position]                                                            #최대값 위치 데이터 삭제
#
# print(point_list)
# temp_po=point_list[:]                                                        #2번째 반복.
# m = max(temp_po)
# position = point_list.index(m)
# print(team_list[position])
# game_16.append(team_list[position])
#
# print(game_16)

# a11 = 0
# a12 = 0
# a13 = 0
# a14 = 0
# A = {'네덜란드':a11, '세네갈':a12, '에콰도르':a13, '카타르':a14}
# B = {'잉글랜드':a11, '웨일스':a12, '미국':a13, '이란':a14}
# C = {'아르헨티나':a11, '멕시코':a12, '폴란드':a13, '사우디아라비아':a14}
# D = {'프랑스':a11, '튀니지':a12, '덴마크':a13, '호주':a14}
# E = {'스페인':a11, '독일':a12, '일본':a13, '코스타리카':a14}
# F = {'벨기에':a11, '크로아티아':a12, '모로코':a13, '캐나다':a14}
# G = {'브라질':a11, '세르비아':a12, '카메룬':a13, '스위스':a14}
# H = {'포루투갈':a11, '우루과이':a12, '가나':a13, '대한민국':a14}
#
# num=[A,B,C,D,E]
#
# for i in num:
#     print(i)

# dicA = {1 :'네덜란드', 2 :'세네갈', 3 :'에콰도르', 4 :'카타르'}
# print(dicA((1))
import random
winner_16 = []
A = {0:'A',1:['네덜란드',0,7], 2:['세네갈',0,6], 3:['에콰도르',0,4], 4:['카타르',0,2]}
B = {0:'B',1:['잉글랜드',0,7], 2:['웨일스',0,6], 3:['미국',0,4], 4:['이란',0,2]}
C = {0:'C',1:['아르헨티나',0,7], 2:['멕시코',0,6], 3:['폴란드',0,4], 4:['사우디아라비아',0,2]}
D = {0:'D',1:['프랑스',0,7], 2:['튀니지',0,6], 3:['덴마크',0,4], 4:['호주',0,2]}
E = {0:'E',1:['스페인',0,7], 2:['독일',0,6], 3:['일본',0,4], 4:['코스타리카',0,2]}
F = {0:'F',1:['벨기에',0,7], 2:['크로아티아',0,6], 3:['모로코',0,4], 4:['캐나다',0,2]}
G = {0:'G',1:['브라질',0,7], 2:['세르비아',0,6], 3:['카메룬',0,4], 4:['스위스',0,2]}
H = {0:'H',1:['포루투갈',0,7], 2:['우루과이',0,6], 3:['가나',0,4], 4:['대한민국',0,2]}
list = [A, B, C, D, E, F, G, H]
for i in list:
    # print(i[1][0])
    a0 = random.randrange(1,15)
    print('\t',i[0],'조 제 1경기')
    print(i[1][0],'vs',i[2][0])
    if a0 >= 8: #승률 70%와 60%
        print(a0)
        print(i[1][0],'승리')
        i[1][1] += 3
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
    elif a0 == 7:
        print('무승부')
        i[1][1] += 1
        i[2][1] += 1
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
        print(i[2][0],'현재 승점은',i[2][1], '입니다.')
    else:
        print(a0)
        print(i[2][0],'승리')
        i[2][1] += 3
        print(i[2][0],'현재 승점은',i[2][1], '입니다.')
    print('------------------------------------------------------------------------------')
    print('\t', i[0], '조 제 2경기 ')
    print(i[1][0],'vs',i[3][0])
    a01 = random.randrange(1,15)
    if a01 >= 7: #승률 70%와 40%
        print(a01)
        print(i[1][0],'승리')
        i[1][1] += 3
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
    elif a01 == 5 and a01 == 6:
        print('무승부')
        i[1][1] += 1
        i[3][1] += 1
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
        print(i[3][0],'현재 승점은',i[3][1], '입니다.')
    else:
        print(a01)
        print(i[3][0],'승리')
        i[3][1] += 3
        print(i[3][0],'현재 승점은',i[3][1], '입니다.')
    print('------------------------------------------------------------------------------')
    a02 = random.randrange(1, 15)
    print('\t', i[0], '조 제 3경기 ')
    print(i[1][0], 'vs', i[4][0])
    if a02 >= 7:
        print(a02)  # 승률 70%와 20%
        print(a01)
        print(i[1][0],'승리')
        i[1][1] += 3
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
    elif a02 > 2 and a02 < 7:
        print('무승부')
        i[1][1] += 1
        i[4][1] += 1
        print(i[1][0],'현재 승점은',i[1][1], '입니다.')
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')
    else:
        print(a02)
        print(i[4][0],'승리')
        i[4][1] += 3
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')
    print('------------------------------------------------------------------------------')
    print('\t', i[0], '조 제 4경기 ')
    print(i[2][0], 'vs', i[3][0])
    a03 = random.randrange(1, 15)
    if a03 >= 8:  # 승률 60%와 40%
        print(a03)
        print(i[2][0], '승리')
        i[2][1] += 3
        print(i[2][0], '현재 승점은', i[2][1], '입니다.')
    elif a03 == 6 and a03 == 7:
        print('무승부')
        i[2][1] += 1
        i[3][1] += 1
        print(i[2][0],'현재 승점은',i[2][1], '입니다.')
        print(i[3][0],'현재 승점은',i[3][1], '입니다.')
    else:
        print(i[3][0],'승리')
        i[3][1] += 3
        print(i[3][0],'현재 승점은',i[3][1], '입니다.')
    print('------------------------------------------------------------------------------')
    print('\t', i[0], '조 제 5경기 ')
    print(i[2][0], 'vs', i[4][0])
    a04 = random.randrange(1, 15)
    if a04 >= 8:  # 승률 60%와 20%
        print(a04)
        print(i[2][0], '승리')
        i[2][1] += 3
        print(i[2][0], '현재 승점은', i[2][1], '입니다.')
    elif a04 == 6 and a04 == 7:
        print('무승부')
        i[2][1] += 1
        i[4][1] += 1
        print(i[2][0],'현재 승점은',i[2][1], '입니다.')
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')
    else:
        print(a04)
        print(i[4][0],'승리')
        i[4][1] += 3
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')
    print('------------------------------------------------------------------------------')
    print('\t', i[0], '조 제 6경기 ')
    print(i[3][0], 'vs', i[4][0])
    a05 = random.randrange(1, 15)
    if a05 >= 9:  # 승률 40%와 20%
        print(a05)
        print(i[3][0], '승리')
        i[3][1] += 3
        print(i[3][0], '현재 승점은', i[3][1], '입니다.')
    elif a05 > 3 and a05 < 9:
        print('무승부')
        i[1][1] += 1
        i[4][1] += 1
        print(i[3][0],'현재 승점은',i[3][1], '입니다.')
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')

    else:
        print(a05)
        print(i[4][0],'승리')
        i[4][1] += 3
        print(i[4][0],'현재 승점은',i[4][1], '입니다.')
    print('------------------------------------------------------------------------------')
    print("총 승점은",i[1][0],'팀은 ',i[1][1],'점',i[2][0],'팀은',i[2][1],'점',i[3][0],'팀은',i[3][1],'점',i[4][0],'팀은',i[4][1],'점 입니다.')

    # list = [i[1][0],i[2][0],i[3][0],i[4][0]]
    # list_1 = [i[1][1],i[2][1],i[3][1],i[4][1]]
    # print(list)
    # print(list_1,)
    # list_1.sort()
    # print(list_1)
    # print(max(list_1),'1위')
    # print((max(list_1),'2위'))
    # print(list_1)
    # del list_1[max]
    # max(list_1)
    # list_16 =[]
    # print()
    team_list = [i[1][0],i[2][0],i[3][0],i[4][0]]
    pts_list = [i[1][1],i[2][1],i[3][1],i[4][1]]
    temp_pts = pts_list[:]
    print(team_list)
    print(pts_list)
    # print(temp_pts)
    m = max(pts_list)
    position = pts_list.index(m)
    # print(m)
    # print(position)
    winner_16.append(team_list[position])
    del team_list [position]
    del pts_list [position]
    print(team_list)
    print(pts_list)
    # temp_pts = team_list[:]
    m = max(pts_list)
    position = pts_list.index(m)
    print(position)
    winner_16.append(team_list[position])
    print('------------------------------------------------------------------------------')
print('16강 진출팀')
print(winner_16)
#16강  진출팀
# print(winner_16)
# # winner_16[]
import random
# list = [winner_16]
# for i in list:
#     # print(i[1][0])
#     a8 = random.randrange(1,15)
#     print('\t',i[],'16강 제 1경기')
#     print(i[][],'vs',i[][])
#     if a8 >= 8:
#         print(a8)
#         print(i[][],'승리')
#     else:
#         print(a8)
#         print(i[][],'승리')
winner_8 = []
for i in range(0,16,4):
    # print(winner_16[i])
    # print(i[0])
    a8 = random.randrange(1,15)
    print('\t','16강 경기')
    print(winner_16[i],'vs',winner_16[i+2])
    if a8 >= 7:
        print(a8)
        print(winner_16[i], '승리')
        winner_8.append(winner_16[i])
    else:
        print(a8)
        print(winner_16[i+2], '승리')
        winner_8.append(winner_16[i+2])
    print(winner_16[i+1], 'vs', winner_16[i + 3])
    if a8 >= 7:
         print(a8)
         print(winner_16[i+1],'승리')
         winner_8.append(winner_16[i+1])
    else:
        print(a8)
        print(winner_16[i+3],'승리')
        winner_8.append(winner_16[i+3])
    print('------------------------------------------------------------------------------')
    # winner_8.append()
    # print(winner_8)
print('8강 진출팀')
print(winner_8)
#8강 진출팀
winner_4 = []
for i in range(0,8,2):
    # print(winner_8[i])
    # print(i[0])
    a9 = random.randrange(1,15)
    print('\t','8강 경기')
    print(winner_8[i],'vs',winner_8[i+1])
    if a9 >= 7:
        print(a9)
        print(winner_8[i], '승리')
        winner_4.append(winner_8[i])
    else:
        print(a9)
        print(winner_8[i+1], '승리')
        winner_4.append(winner_8[i+1])
    # print(winner_8[i+2], 'vs', winner_8[i+3])
    # if a8 >= 7:
    #      print(a9)
    #      print(winner_16[i+2],'승리')
    #      winner_4.append(winner_8[i+2])
    # else:
    #     print(a9)
    #     print(winner_16[i+3],'승리')
    #     winner_4.append(winner_8[i+3])
    print('------------------------------------------------------------------------------')
    print('4강 진출팀')
    print(winner_4)

final = []
lose = []
for i in range(0,4,2):
    a10 = random.randrange(1,15)
    print('\t','4강 경기')
    print(winner_4[i],'vs',winner_4[i+1])
    if a10 >= 7:
        print(a10)
        print(winner_4[i], '승리')
        final.append(winner_4[i])

    else:
        print(a10)
        print(winner_4[i+1], '승리')
        final.append(winner_4[i+1])

    print('------------------------------------------------------------------------------')
print('결승 진출팀')
print(final)
#결승전
champion = []
for i in range(0,1):
    a11 = random.randrange(1,15)
    print('\t','결승전 경기')
    print(final[i],'vs',final[i+1])
    if a11 >= 7:
        print(a11)
        print(final[i], '승리')
        champion.append(final[i])
    else:
        print(a11)
        print(final[i+1], '승리')
        champion.append(final[i+1])
    print('------------------------------------------------------------------------------')
print('우승팀은',end='')
print(champion)