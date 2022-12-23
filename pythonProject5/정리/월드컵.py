import random
# win = 3 # draw = 1# lose = 0
a11 = 0
a12 = 0
a13 = 0
a14 = 0
A = {'네덜란드':[a11,7], '세네갈':[a12,6], '에콰도르':[a13,4], '카타르':[a14,2]}
B = {'잉글랜드':[a11,7], '웨일스':[a12,6], '미국':[a13,4], '이란':[a14,2]}
C = {'아르헨티나':[a11,7], '멕시코':[a12,6], '폴란드':[a13,4], '사우디아라비아':[a14,2]}
D = {'프랑스':[a11,7], '튀니지':[a12,6], '덴마크':[a13,4], '호주':[a14,2]}
E = {'스페인':[a11,7], '독일':[a12,6], '일본':[a13,4], '코스타리카':[a14,2]}
F = {'벨기에':[a11,7], '크로아티아':[a12,6], '모로코':[a13,4], '캐나다':[a14,2]}
G = {'브라질':[a11,7], '세르비아':[a12,6], '카메룬':[a13,4], '스위스':[a14,2]}
H = {'포루투갈':[a11,7], '우루과이':[a12,6], '가나':[a13,4], '대한민국':[a14,2]}
list = [A,B,C,D,E,F,G,H]

print('------------------------------------------')
print('\t  A조 제1경기')
print('  네덜란드 vs 세네갈 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('네덜란드 승리')
    a11 += 3
    print('네덜란드 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('네덜란드 현재 승점은 %d 입니다.' % (a11))
    print('세네갈 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('세네갈 승리')
    a12 += 3
    print('세네갈 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  A조 제2경기')
print('  네덜란드 vs 에콰도르 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('네덜란드 승리')
    a11 += 3
    print('네덜란드 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('네덜란드 현재 승점은 %d 입니다.' % (a11))
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('에콰도르 승리')
    a13 += 3
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  A조 제3경기')
print('  네덜란드 vs 카타르 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('네덜란드 승리')
     a11 += 3
     print('네덜란드 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('네덜란드 현재 승점은 %d 입니다.' % (a11))
    print('카타르 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('카타르 승리')
    a14 += 3
    print('카타르 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  A조 제4경기')
print('  세네갈 vs 에콰도르 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('세네갈 승리')
    a12 += 3
    print('세네갈 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('세네갈 현재 승점은 %d 입니다.' % (a12))
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('에콰도르 승리')
    a13 += 3
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  A조 제5경기')
print('  세네갈 vs 카타르 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('세네갈 승리')
    a12 += 3
    print('세네갈 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('세네갈 현재 승점은 %d 입니다.' % (a12))
    print('카타르 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('카타르 승리')
    a14 += 3
    print('카타르 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  A조 제6경기')
print(' 에콰도르 vs 카타르 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('에콰도르 승리')
    a13 += 3
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('에콰도르 현재 승점은 %d 입니다.' % (a13))
    print('카타르 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('카타르 승리')
    a14 += 3
    print('카타르 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------------------------------------------------')
print('최종승점은:')
print('네덜란드 총 승점은 %d,세네갈 총 승점은 %d,에콰도르 총 승점은 %d,카타르 총 승점은 %d 입니다.' % (a11,a12,a13,a14))

A = {'네덜란드':a11, '세네갈':a12, '에콰도르':a13, '카타르':a14}
print(max(A, key=A.get), "1위")
A_1 = max(A, key=A.get)
del A[max(A, key=A.get)]
print(max(A, key=A.get), "2위")
A_2 = max(A, key=A.get)

# list = [a11, a21, a31, a41]
#
# print('16강 진출팀은')
# print('%s 팀입니다')
# print('%s 팀입니다')
# print('------------------------------------------------------------------------------------')
# dicA = {a1:a11, a2:a21, a3:a31, a4:a41}
# # del dicA(max(dicA))
# print(dicA)
#
import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0

print('------------------------------------------')
print('\t  B조 제1경기')
print('  잉글랜드 vs 웨일스 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('잉글랜드 승리')
    a11 += 3
    print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
    print('웨일스 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('웨일스 승리')
    a12 += 3
    print('웨일스 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  B조 제2경기')
print('  잉글랜드 vs 미국 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('잉글랜드 승리')
    a11 += 3
    print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
    print('미국 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('미국 승리')
    a13 += 3
    print('미국 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  B조 제3경기')
print('  잉글랜드 vs 이란 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('잉글랜드 승리')
     a11 += 3
     print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('잉글랜드 현재 승점은 %d 입니다.' % (a11))
    print('이란 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('이란 승리')
    a14 += 3
    print('이란 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  B조 제4경기')
print('  웨일스 vs 미국 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('웨일스 승리')
    a12 += 3
    print('웨일스 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('웨일스 현재 승점은 %d 입니다.' % (a12))
    print('미국 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('미국 승리')
    a13 += 3
    print('미국 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  B조 제5경기')
print('  웨일스 vs 이란 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('웨일스 승리')
    a12 += 3
    print('웨일스 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('웨일스 현재 승점은 %d 입니다.' % (a12))
    print('이란 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('이란 승리')
    a14 += 3
    print('이란 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  B조 제6경기')
print(' 미국 vs 이란 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('미국 승리')
    a13 += 3
    print('미국 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('미국 현재 승점은 %d 입니다.' % (a13))
    print('이란 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('이란 승리')
    a14 += 3
    print('이란 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('잉글랜드 총 승점은 %d,웨일스 총 승점은 %d,미국 총 승점은 %d,이란 총 승점은 %d 입니다.' % (a11,a12,a13,a14))
B = {'잉글랜드':a11, '웨일스':a12, '미국':a13, '이란':a14}
print(max(B, key=B.get), "1위")
B_1 = max(B, key=B.get)
del B[max(B, key=B.get)]
print(max(B, key=B.get), "2위")
B_2 = max(B, key=B.get)
print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0


print('------------------------------------------')
print('\t C 조 제1경기')
print(' 아르헨티나  vs 멕시코 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('아르헨티나 승리')
    a11 += 3
    print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
    print('멕시코 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('멕시코 승리')
    a12 += 3
    print('멕시코 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t C 조 제2경기')
print(' 아르헨티나  vs 폴란드 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('아르헨티나 승리')
    a11 += 3
    print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
    print('폴란드 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('폴란드 승리')
    a13 += 3
    print('폴란드 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t C 조 제3경기')
print('아르헨티나   vs 사우디아라비아 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('아르헨티나 승리')
     a11 += 3
     print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('아르헨티나 현재 승점은 %d 입니다.' % (a11))
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('사우디아라비아 승리')
    a14 += 3
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t C 조 제4경기')
print(' 멕시코 vs 폴란드 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('멕시코 승리')
    a12 += 3
    print('멕시코 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('멕시코 현재 승점은 %d 입니다.' % (a12))
    print('폴란드 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('폴란드 승리')
    a13 += 3
    print('폴란드 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  C조 제5경기')
print('멕시코   vs 사우디아라비아 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('멕시코 승리')
    a12 += 3
    print('멕시코 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('멕시코 현재 승점은 %d 입니다.' % (a12))
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('사우디아라비아 승리')
    a14 += 3
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t C 조 제6경기')
print('폴란드  vs 사우디아라비아 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('폴란드 승리')
    a13 += 3
    print('폴란드 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('폴란드 현재 승점은 %d 입니다.' % (a13))
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('사우디아라비아 승리')
    a14 += 3
    print('사우디아라비아 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총 승점은 아르헨티나 %d,  총 멕시코 승점은 %d, 총 폴란드 승점은 %d, 총 사우디아라비아 승점은 %d 입니다.' % (a11,a12,a13,a14))
C = {'아르헨티나':a11, '멕시코':a12, '폴란드':a13, '사우디아라비아':a14}
print(max(C, key=C.get), "1위")
C_1 = max(C, key=C.get)
del C[max(C, key=C.get)]
print(max(C, key=C.get), "2위")
C_2 = max(C, key=C.get)

print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0
print('------------------------------------------')
print('\t  D조 제1경기')
print(' 프랑스  vs 튀니지 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('프랑스 승리')
    a11 += 3
    print('프랑스 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('프랑스 현재 승점은 %d 입니다.' % (a11))
    print('튀니지 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('튀니지 승리')
    a12 += 3
    print('튀니지 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  D조 제2경기')
print('프랑스   vs 덴마크 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('프랑스 승리')
    a11 += 3
    print('프랑스 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('프랑스 현재 승점은 %d 입니다.' % (a11))
    print('덴마크 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('덴마크 승리')
    a13 += 3
    print('덴마크 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  D조 제3경기')
print('프랑스   vs 호주 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('프랑스 승리')
     a11 += 3
     print('프랑스 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('프랑스 현재 승점은 %d 입니다.' % (a11))
    print('호주 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('호주 승리')
    a14 += 3
    print('호주 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  D조 제4경기')
print(' 튀니지  vs 덴마크 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('튀니지 승리')
    a12 += 3
    print('튀니지 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('튀니지 현재 승점은 %d 입니다.' % (a12))
    print('덴마크 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('덴마크 승리')
    a13 += 3
    print('덴마크 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  D조 제5경기')
print(' 튀니지 vs 호주 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('튀니지 승리')
    a12 += 3
    print('튀니지 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('튀니지 현재 승점은 %d 입니다.' % (a12))
    print('호주 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('호주 승리')
    a14 += 3
    print('호주 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  D조 제6경기')
print('덴마크  vs 호주 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('덴마크 승리')
    a13 += 3
    print('덴마크 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('덴마크 현재 승점은 %d 입니다.' % (a13))
    print('호주 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('호주 승리')
    a14 += 3
    print('호주 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총 프랑스 승점은 %d,  총 튀니지 승점은 %d, 총 덴마크 승점은 %d, 총 호주 승점은 %d 입니다.' % (a11,a12,a13,a14))
D = {'프랑스':a11, '튀니지':a12, '덴마크':a13, '호주':a14}
print(max(D, key=D.get), "1위")
D_1 = max(D, key=D.get)
del D[max(D, key=D.get)]
print(max(D, key=D.get), "2위")
D_2 = max(D, key=D.get)


print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0
print('------------------------------------------')
print('\t  E조 제1경기')
print(' 스페인  vs 독일 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('스페인 승리')
    a11 += 3
    print('스페인 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('스페인 현재 승점은 %d 입니다.' % (a11))
    print('독일 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('독일 승리')
    a12 += 3
    print('독일 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  E조 제2경기')
print(' 스페인 vs 일본 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('스페인 승리')
    a11 += 3
    print('스페인 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('스페인 현재 승점은 %d 입니다.' % (a11))
    print('일본 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('일본 승리')
    a13 += 3
    print('일본 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  E조 제3경기')
print('스페인   vs 코스타리카 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('스페인 승리')
     a11 += 3
     print(' 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('스페인 현재 승점은 %d 입니다.' % (a11))
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('코스타리카 승리')
    a14 += 3
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t E조 제4경기')
print('독일   vs 일본 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('독일 승리')
    a12 += 3
    print('독일 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('독일 현재 승점은 %d 입니다.' % (a12))
    print('일본 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('일본 승리')
    a13 += 3
    print('일본 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  E조 제5경기')
print('독일   vs 코스타리카 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('독일 승리')
    a12 += 3
    print('독일 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('독일 현재 승점은 %d 입니다.' % (a12))
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('코스타리카 승리')
    a14 += 3
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  E조 제6경기')
print('일본  vs 코스타리카 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('일본 승리')
    a13 += 3
    print('일본 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('일본 현재 승점은 %d 입니다.' % (a13))
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('코스타리카 승리')
    a14 += 3
    print('코스타리카 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총 스페인 승점은 %d,  총 독일 승점은 %d, 총 일본 승점은 %d, 총 코스타리카 승점은 %d 입니다.' % (a11,a12,a13,a14))
E = {'스페인':a11, '독일':a12, '일본':a13, '코스타리카':a14}
print(max(E, key=E.get), "1위")
E_1 = max(E, key=E.get)
del E[max(E, key=E.get)]
print(max(E, key=E.get), "2위")
E_2 = max(E, key=E.get)

print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0

print('------------------------------------------')
print('\t F조 제1경기')
print('벨기에   vs 크로아티아 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('벨기에 승리')
    a11 += 3
    print('벨기에 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('벨기에 현재 승점은 %d 입니다.' % (a11))
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('크로아티아 승리')
    a12 += 3
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  F조 제2경기')
print('벨기에   vs 모로코 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('벨기에 승리')
    a11 += 3
    print('벨기에 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('벨기에 현재 승점은 %d 입니다.' % (a11))
    print('모로코 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('모로코 승리')
    a13 += 3
    print('모로코 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  F조 제3경기')
print('벨기에   vs 캐나다 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('벨기에 승리')
     a11 += 3
     print('벨기에 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('벨기에 현재 승점은 %d 입니다.' % (a11))
    print('캐나다 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('캐나다 승리')
    a14 += 3
    print('캐나다 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  F조 제4경기')
print('크로아티아   vs 모로코 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('크로아티아 승리')
    a12 += 3
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))
    print('모로코 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('모로코 승리')
    a13 += 3
    print('모로코 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  F조 제5경기')
print('크로아티아   vs 캐나다 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('크로아티아 승리')
    a12 += 3
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('크로아티아 현재 승점은 %d 입니다.' % (a12))
    print('캐나다 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('캐나다 승리')
    a14 += 3
    print('캐나다 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  F조 제6경기')
print('모로코  vs 캐나다 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('모로코 승리')
    a13 += 3
    print('모로코 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('모로코 현재 승점은 %d 입니다.' % (a13))
    print('캐나다 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('캐나다 승리')
    a14 += 3
    print('캐나다 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총 벨기에 승점은 %d,  총 크로아티아 승점은 %d, 총 모로코 승점은 %d, 총 캐나다 승점은 %d 입니다.' % (a11,a12,a13,a14))
F = {'벨기에':a11, '크로아티아':a12, '모로코':a13, '캐나다':a14}

print(max(F, key=F.get), "1위")
F_1 = max(F, key=F.get)
del F[max(F, key=F.get)]
print(max(F, key=F.get), "2위")
F_2 = max(F, key=F.get)
print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0
print('------------------------------------------')
print('\t  G조 제1경기')
print('브라질   vs 세르비아 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('브라질 승리')
    a11 += 3
    print('브라질 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('브라질 현재 승점은 %d 입니다.' % (a11))
    print('세르비아 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('세르비아 승리')
    a12 += 3
    print('세르비아 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  G조 제2경기')
print('브라질   vs 카메룬 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('브라질 승리')
    a11 += 3
    print('브라질 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('브라질 현재 승점은 %d 입니다.' % (a11))
    print('카메룬 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('카메룬 승리')
    a13 += 3
    print('카메룬 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  G조 제3경기')
print('브라질   vs 스위스 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('브라질 승리')
     a11 += 3
     print('브라질 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('브라질 현재 승점은 %d 입니다.' % (a11))
    print('스위스 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('스위스 승리')
    a14 += 3
    print('스위스 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  G조 제4경기')
print('세르비아  vs  카메룬 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('세르비아 승리')
    a12 += 3
    print('세르비아 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('세르비아 현재 승점은 %d 입니다.' % (a12))
    print('카메룬 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('카메룬 승리')
    a13 += 3
    print('카메룬 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  G조 제5경기')
print('세르비아   vs 스위스 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('세르비아 승리')
    a12 += 3
    print('세르비아 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('세르비아 현재 승점은 %d 입니다.' % (a12))
    print('스위스 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('스위스 승리')
    a14 += 3
    print('스위스 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  G조 제6경기')
print('카메룬  vs 스위스 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('카메룬 승리')
    a13 += 3
    print('카메룬 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('카메룬 현재 승점은 %d 입니다.' % (a13))
    print('스위스 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('스위스 승리')
    a14 += 3
    print('스위스 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총 브라질 승점은 %d,  총 세르비아 승점은 %d, 총 카메룬 승점은 %d, 총 스위스 승점은 %d 입니다.' % (a11,a12,a13,a14))
G = {'브라질':a11, '세르비아':a12, '카메룬':a13, '스위스':a14}

print(max(G, key=G.get), "1위")
G_1 = max(G, key=G.get)
del G[max(G, key=G.get)]
print(max(G, key=G.get), "2위")
G_2 = max(G, key=G.get)
print('------------------------------------------------------------------------------------')

import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0
print('------------------------------------------')
print('\t  H조 제1경기')
print('포루투갈   vs 우루과이 ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print('포루투갈 승리')
    a11 += 3
    print('포루투갈 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print('포루투갈 현재 승점은 %d 입니다.' % (a11))
    print('우루과이 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print('우루과이 승리')
    a12 += 3
    print('우루과이 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  H조 제2경기')
print('포루투갈   vs 가나 ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print('포루투갈 승리')
    a11 += 3
    print('포루투갈 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print('포루투갈 현재 승점은 %d 입니다.' % (a11))
    print('가나 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print('가나 승리')
    a13 += 3
    print('가나 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  H조 제3경기')
print('포루투갈   vs 대한민국 ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print('포루투갈 승리')
     a11 += 3
     print('포루투갈 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print('포루투갈 현재 승점은 %d 입니다.' % (a11))
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print('대한민국 승리')
    a14 += 3
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  H조 제4경기')
print('우루과이   vs 가나 ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print('우루과이 승리')
    a12 += 3
    print('우루과이 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print('우루과이 현재 승점은 %d 입니다.' % (a12))
    print('가나 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print('가나 승리')
    a13 += 3
    print('가나 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  H조 제5경기')
print('우루과이   vs 대한민국 ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print('우루과이 승리')
    a12 += 3
    print('우루과이 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print('우루과이 현재 승점은 %d 입니다.' % (a12))
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print('대한민국 승리')
    a14 += 3
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  H조 제6경기')
print('가나  vs 대한민국 ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print('가나 승리')
    a13 += 3
    print('가나 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print('가나 현재 승점은 %d 입니다.' % (a13))
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print('대한민국 승리')
    a14 += 3
    print('대한민국 현재 승점은 %d 입니다.' % (a14))

H0 = []
H0.append()
print('최종승점은:')
print('총 포루투갈 승점은 %d,  총 우루과이 승점은 %d, 총 가나 승점은 %d, 총 대한민국 승점은 %d 입니다.' % (a11,a12,a13,a14))
H = {'포루투갈':a11, '우루과이':a12, '가나':a13, '대한민국':a14}

print(max(H, key=H.get), "1위")
H_1 = max(H, key=H.get)
del H[max(H, key=H.get)]
print(max(H, key=H.get), "2위")
H_2 = max(H, key=H.get)

print('------------------------------------------------------------------------------------')
print('16강 진출팀은')
print(A_1,A_2, B_1,B_2, C_1,C_2, D_1,D_2, E_1,E_2, F_1,F_2, G_1,G_2, H_1,H_2)
ahah = []
ahah = A_1,A_2,B_1,B_2,C_1,C_2,D_1,D_2,E_1,E_2,F_1,F_2,G_1,G_2,H_1,H_2
print(ahah)


# rate = [7,6,4,2,7,6,4,2,7,6,4,2,7,6,4,2]
# def rat (ay,b,i):
#     quarter = []
#     quarter_rate = []
#     result = random.randint(1, rate[ay]+rate[b])
#     print(ahah[i])
#     print(ahah[i+3])
#     if result <= rate[ay]:
#         print(ahah[i],"승")
#         quarter.append(ahah[ay])
#         quarter_rate.append(rate[ay])
#     elif result > rate[ay]:
#         print(ahah[i+3], "승")
#         quarter.append(ahah[b])
#         quarter_rate.append(rate[b])
# rat(7,6,0)
# rat(7,6,1)
# rat(7,6,2)
# rat(7,6,3)
# rat(7,6,4)
# rat(7,6,5)
# rat(7,6,6)
# rat(7,6,7)

