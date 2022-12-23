import random
a11 = 0
a12 = 0
a13 = 0
a14 = 0

print('------------------------------------------')
print('\t  조 제1경기')
print('   vs  ')

a0 = random.randrange(1,15)
if a0 >= 8: #승률 70%와 60%
    print(a0)
    print(' 승리')
    a11 += 3
    print(' 현재 승점은 %d 입니다.' % (a11))
elif a0 == 7:
    print('무승부')
    a11 += 1
    a12 += 1
    print(' 현재 승점은 %d 입니다.' % (a11))
    print(' 현재 승점은 %d 입니다.' % (a12))

else:
    print(a0)
    print(' 승리')
    a12 += 3
    print(' 현재 승점은 %d 입니다.' % (a12))

print('------------------------------------------')
print('\t  조 제2경기')
print('   vs  ')
a01 = random.randrange(1,15)
if a01 >= 7: #승률 70%와 40%
    print(a01)
    print(' 승리')
    a11 += 3
    print(' 현재 승점은 %d 입니다.' % (a11))
elif a01 == 5 and a01 == 6:
    print('무승부')
    a11 += 1
    a13 += 1
    print(' 현재 승점은 %d 입니다.' % (a11))
    print(' 현재 승점은 %d 입니다.' % (a13))

else:
    print(a01)
    print(' 승리')
    a13 += 3
    print(' 현재 승점은 %d 입니다.' % (a13))

print('------------------------------------------')
print('\t  조 제3경기')
print('   vs  ')
a02 = random.randrange(1,15)

if a02 >= 7:
     print(a02)  # 승률 70%와 20%
     print(' 승리')
     a11 += 3
     print(' 현재 승점은 %d 입니다.' % (a11))
elif a02 > 2 and a02 < 7:
    print('무승부')
    a11 += 1
    a14 += 1
    print(' 현재 승점은 %d 입니다.' % (a11))
    print(' 현재 승점은 %d 입니다.' % (a14))

else:
    print(a02)
    print(' 승리')
    a14 += 3
    print(' 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  조 제4경기')
print('   vs  ')
a03 = random.randrange(1,15)
if a03 >= 8: #승률 60%와 40%
    print(a03)
    print(' 승리')
    a12 += 3
    print(' 현재 승점은 %d 입니다.' % (a12))
elif a03 == 6 and a03 == 7:
    print('무승부')
    a12 += 1
    a13 += 1
    print(' 현재 승점은 %d 입니다.' % (a12))
    print(' 현재 승점은 %d 입니다.' % (a13))

else:
    print(a03)
    print(' 승리')
    a13 += 3
    print(' 현재 승점은 %d 입니다.' % (a13))


print('------------------------------------------')
print('\t  조 제5경기')
print('   vs  ')
a04 = random.randrange(1,15)
if a04 >= 8: #승률 60%와 20%
    print(a04)
    print(' 승리')
    a12 += 3
    print(' 현재 승점은 %d 입니다.' % (a12))
elif a04 == 6 and a04 == 7:
    print('무승부')
    a12 += 1
    a14 += 1
    print(' 현재 승점은 %d 입니다.' % (a12))
    print(' 현재 승점은 %d 입니다.' % (a14))

else:
    print(a04)
    print(' 승리')
    a14 += 3
    print(' 현재 승점은 %d 입니다.' % (a14))

print('------------------------------------------')
print('\t  조 제6경기')
print('  vs  ')
a05 = random.randrange(1,15)
if a05 >= 9: #승률 40%와 20%
    print(a05)
    print(' 승리')
    a13 += 3
    print(' 현재 승점은 %d 입니다.' % (a13))
elif a05 > 3 and a05 < 9:
    print('무승부')
    a11 += 1
    a14 += 1
    print(' 현재 승점은 %d 입니다.' % (a13))
    print(' 현재 승점은 %d 입니다.' % (a14))

else:
    print(a05)
    print(' 승리')
    a14 += 3
    print(' 현재 승점은 %d 입니다.' % (a14))


print('최종승점은:')
print('총  승점은 %d,  총  승점은 %d, 총  승점은 %d, 총  승점은 %d 입니다.' % (a11,a12,a13,a14))


print('------------------------------------------------------------------------------------')