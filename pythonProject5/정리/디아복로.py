import random
def monster_():
    b = random.randint(1000,3000)   #동혀니 홍거리 공격력
    c = random.randint(2500, 8000)  #디아복록 공격력
    d = random.randint(300, 500)    #좀비 hp
    e = random.randint(450, 700)    #구울
    f = random.randint(480, 800)    #해골
    g = random.randint(550, 900)    #버그베어
    h = random.randint(3000, 8000)  #동혀니,홍거리
    i = random.randint(5000, 15000) #디아복로
    monster = [['좀비',['공격력', 100],['HP',d]],
                ['구울',['공격력', 180],['HP',e]],
                ['해골',['공격력', 220],['HP',f]],
                ['버그베어',['공격력', 350],['HP',g]],
                ['동혀니',['공격력',b ],['HP',h]],
                ['홍거리',['공격력',b ],['HP',h]],
                ['디아복로',['공격력',c ],['HP',i]]]
    a = random.randint(1, 100)
    # a = 100
    if a <= 48:                         #좀비
        print(monster[0][0])
        print(monster[0][1])
        print(monster[0][2])
        return monster[0]
    elif a > 48 and a <=78:             #구울
        print(monster[1][0])
        print(monster[1][1])
        print(monster[1][2])
        return monster[1]
    elif a >78 and a <=90:              #해골
        print(monster[2][0])
        print(monster[2][1])
        print(monster[2][2])
        return monster[2]
    elif a > 90 and a <=95:             #버그베어
        print(monster[3][0])
        print(monster[3][1])
        print(monster[3][2])
        return monster[3]
    elif a > 95 and a <= 97:            #동혀니
        print(monster[4][0])
        print(monster[4][1])
        print(monster[4][2])
        return monster[4]
    elif a >97 and a <= 99:             #홍거리
        print(monster[5][0])
        print(monster[5][1])
        print(monster[5][2])
        return monster[5]
    else:                               #디아복로
        print(monster[6][0])
        print(monster[6][1])
        print(monster[6][2])
        return monster[6]

def fight(choco_y): #몬스터와 의용군 만났을때 함수
    monster = monster_() # return monster[]
    print(f'{monster[0]}와(과) 의용군이 만났습니다')
    yy = choco_y # choco_y = [500,[100,150],0,0,0]
    full_hp = yy[0] # 풀 Hp
    posion = 0 # 포션 갯수
    turn = 0 # 엘릭서 무적 횟수

    while True:
        attack = random.randint(choco_y[1][0],choco_y[1][1])
        if monster[0] == '디아복로':
            monster[1][1] = random.randint(2500,8000) # 몬스터 1회 공격력 랜덤
        if monster[0] =='동혀니':
            monster[1][1] = random.randint(1000, 3000) # 몬스터 1회 공격력 랜덤
        if monster[0] == '홍거리':
            monster[1][1] = random.randint(1000, 3000) # 몬스터 1회 공격력 랜덤
        o = int(input('1.싸운다 2.도망 간다. 3.포션 섭취 4.엘릭서 섭취'))
        if o == 2:
            run = random.randint(1, 2)
            print('도망을 선택하셨습니다.')
            if run == 1:
                print('도망 성공')
                break
            if run == 2:
                print('도망 실패')
                yy[0] -= monster[1][1]  # 몬스터의 공격으로 인한 의용군의 hp
                print(f'{monster[0]}의 공격 : {monster[1][1]}') # 도망 실패시 몬스터만 공격
                if yy[0] > 0:   # 의용군 hp 0보다 클때
                    print(f'의용군 hp: {yy[0]}') # 의용군 체력 표시
                if yy[0] <= 0:   #의용군 hp 0보다 작거나 같을때 게임 종료
                    print(f'의용군 죽었습니다')
                    break

        elif o == 1 :
            print('전투 시작')
            print('='*50)
            monster[2][1] -= attack # 의용군의 공격으로 인한 몬스터의 hp
            if monster[2][1] <= 0:
                print('몬스터가 죽었습니다')
                break
            if turn > 0:
                print(f'{turn}회 무적 입니다')  # 엘릭서 사용시 무적 횟수 표시
                turn -= 1
            else:
                yy[0] -= monster[1][1] # 몬스터의 공격으로 인한 의용군의 hp

            if yy[0] <= 0:
                print('의용군이 죽었습니다')
                break
            print(f'의용군의 공격력 : {attack}  {monster[0]}의 hp: {monster[2][1]} ')  # 전투시에 각각의 공격력과 hp
            print(f'{monster[0]}의 공격력 : {monster[1][1]} 의용군 hp: {yy[0]} ')      # 전투시에 각각의 공격력과 hp
            print('='*50)

        elif o == 3:  # 포션 사용시
            if yy[2] == 0: # 포션 없을때
                print('포션이 없습니다')
            else:    # 포션 있으면
                yy[0] = full_hp  # 체력 풀 hp로 회복
                yy[2] -= 1    # 포션 갯수 감소
                print(f'포션을 사용했습니다. 현재 hp는 {yy[0]}')
                print(f'남은 포션 개수는 {yy[2]}')
                continue  # 포션쓰고 다시 input으로

        elif o == 4:  # 엘릭서 선택
            if yy[3] <= 0: # 엘릭서 없을때
                print('엘릭서가 없습니다')
            if yy[3] > 0:   # 엘릭서 있을때
                yy[0] = full_hp  # 체력 풀 hp로 회복
                print(f'엘릭서를 사용했습니다. 현재 hp는 {yy[0]}')
                turn = 10 # 엘릭서 무적횟수 가 10  체력 풀 hp로 회복
                yy[3] -= 1  # 엘릭서 갯수 감소
                print(f'엘릭서 남은 개수는 {yy[3]}')
    if yy[0] > 0 and monster[2][1] <= 0: # 의용군 hp가 0보다 클때와 몬스터 hp가 0이거나 0보다 작을때(전투 승리)
        elic = random.randint(1,1000)  # 전투 승리시 엘리서 획득 확률 0.5%
        posion_1 = random.randint(1,2)  # 전투 승리시 포션 획득 확률  50%
        if elic <= 5:           # 엘릭서 획득 랜덤
            yy[3] += 1          # 엘릭서 획득시 리스트에 1개 증가
            print(f'엘릭서: {yy[3]}개')
        else:
            print('엘릭서 획득 실패')
        # print(posion_1)
        if posion_1 == 1:  # 포션 획득시 랜덤
            yy[2] += 1     # 포션 획득시 리스트에 1개 증가
            print(f'포션: {posion}개 획득했습니다')
        else:
            print('포션 획득 실패')

    return yy,monster   # yy는 [500, [100, 150], 1, 1, 500], monster는 hp 0을 가져오기

def after_fight(yy,monster):
    print('=' * 50)
    if yy[0] > 0 and monster[2][1]<=0 :      # 의용군 hp가 0보다 클때와 몬스터 hp가 0이거나 0보다 작을때(전투 승리)
        yy[1][1] = round(yy[1][1] * 1.05)    # 최소 공격력 5% 증가
        yy[1][0] = round(yy[1][0] * 1.05)    # 최대 공격력 5% 증가
        yy[0] = round(yy[0] * 1.05)          # 의용군 hp 남은 hp 5% 증가
        yy[4] = round(yy[4] * 1.05)          # 의용군 hp 최대 hp 5% 증가

def battle(choco_y):                         # 전투 함수( [500, [100, 150], 1, 1, 500])
    yy,monster= fight(choco_y)               # 리턴 값 가져오기
    after_fight(yy,monster)                  # 리턴 값을 전투 후 함수에 넣기

def main():                                  # 메인 함수 실행
    posion=0
    elic=0
    choco_y = [500, [100, 150], 1, 1, 500]
    battle(choco_y)
    if choco_y[0] > 0:
        print(f'현재 hp : {choco_y[0]}, 증가 공격력 : {choco_y[1]}, 현재 포션 갯수 : {choco_y[2]}, 현재 엘리서 갯수 : {choco_y[3]}, 최대 hp : {choco_y[4]}')

main()

