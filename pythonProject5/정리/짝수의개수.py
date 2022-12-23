even = 0

for i in range(10):
    num = int(input('숫자를 입력'))
    if num % 2 == 0:
        # print('%d는 짝수입니다' %(num))
        even += 1

print(f'총 짝수의 개수는 {even}개 입니다')
