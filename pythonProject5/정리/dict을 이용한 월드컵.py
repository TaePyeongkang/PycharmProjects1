a11 = 0
a12 = 0
a13 = 0
a14 = 0
A = {'네덜란드':a11, '세네갈':a12, '에콰도르':a13, '카타르':a14}
# B = {'잉글랜드':b11, '웨일스':b12, '미국':b13, '이란':b14}
# C = {'아르헨티나':c11, '멕시코':c12, '폴란드':c13, '사우디아라비아':c14}
# D = {'프랑스':d11, '튀니지':d12, '덴마크':d13, '호주':d14}
# E = {'스페인':e11, '독일':e12, '일본':e13, '코스타리카':e14}
# F = {'벨기에':f11, '크로아티아':f12, '모로코':f13, '캐나다':f14}
# G = {'브라질':g11, '세르비아':g12, '카메룬':g13, '스위스':g14}
# H = {'포루투갈':h11, '우루과이':h12, '카나':h13, '대한민국':h14}


# dic = {'네덜란드':a11}
# print(dic)
# A = {'네덜란드':1, '세네갈':2, '에콰도르':3, '카타르':4}
# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)
# print(G)
# print(H)

print(max(A, key=H.get), "1위")
H_1 = max(A, key=H.get)
del H[max(A, key=H.get)]
print(max(A, key=H.get), "2위")
H_2 = max(A, key=H.get)

# wolrdCup_A조 = '\t카타르 \t    네덜란드\t   세네갈 \t 에콰도르'
# wolrdCup_B조 = '\t잉글랜드 \t 미국       이란\t     웨일스'
# wolrdCup_C조 = '\t아르헨티나    멕시코\t   폴란드\t 사우디아라비아'
# wolrdCup_D조 = '\t프랑스\t    덴마크\t   튀니지\t 호주'
# wolrdCup_E조 = '\t스페인\t\t 독일\t   일본\t     코스타리카'
# wolrdCup_F조 = '\t벨기에\t    크로아티아   모로코\t 캐나다'
# wolrdCup_G조 = '\t브라질\t    스위스 \t   세르비아\t 카메룬'
# wolrdCup_H조 = '\t포르투갈\t    우루과이    대한민국\t 가나'
# print("\t\t\t\t 2022 카타르 월드컵")
# print('\t1포트(70%)   2포트(60%) 3포트(40%) 4포트(20%)')
#
# print('A조', end='')
# print(wolrdCup_A조)
# print('B조', end='')
# print(wolrdCup_B조)
# print('C조', end='')
# print(wolrdCup_C조)
# print('D조', end='')
# print(wolrdCup_D조)
# print('E조', end='')
# print(wolrdCup_E조)
# print('F조', end='')
# print(wolrdCup_F조)
# print('G조', end='')
# print(wolrdCup_G조)
# print('H조', end='')
# print(wolrdCup_H조)