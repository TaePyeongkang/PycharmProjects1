a = int(input('숫자를 입력하세요'))

for i in range(2,10):
    for j in range(1,a+1):
        print('%d X %d = %d' %(i,j,i*j))
