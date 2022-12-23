# potion[0,0,0,0,0,0]
import random
import keyboard
import time


# 키보드 함수(import keyboard 필요) // 박규환 221210 1716
def key_board_move():
    # 정상적인 입력값이 나올 때까지 반복
    while True:
        # 반환 조건
        if keyboard.is_pressed('left'):
            # 입력값이 정상일 경우 정상적으로 반환
            return 'a'
        elif keyboard.is_pressed('right'):
            return 'd'
        elif keyboard.is_pressed('up'):
            return 'w'
        elif keyboard.is_pressed('down'):
            return 's'
        # 입력값이 해당 없을 경우
        else:
            # 패스 후 반복
            pass


def arr(a, b, floor, compre):
    # 임의적으로 15*15배열을 만듬 배경으로 검은색 하트를 넣음
    array = [['🖤' for col in range(15)] for row in range(15)]
    # a는 x좌표 행을 나타냄, b는 y좌표 열을 나타냄 ,초코의용이 (0,0)일때 네모서리, 네 모서리 사이, 그외의 8개가 찍히는경우 총 9가지 조건
    if a == 0 and b == 0:
        # 초코의용의 y좌표에 1을 더한값에 하트
        array[a][b + 1] = '❤'
        # 초코의용의 x좌표에 1을 더한값에 하트
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 0 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if 0 < a < 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
    if a == 14 and 0 < b < 14:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 14 and b == 14:
        array[a][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 0 and b == 14:
        array[a][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
    if 0 < a < 14 and b == 14:
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if 0 < a < 14 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
        array[a - 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
    # 1~9까지 k값
    for k in range(1, 10):
        # 6~10까지 h값, 총 9*5 몬스터 45마리생성, 팀원과 논의로 맵크기 의 20%를 몬스터 수를 정하기로 하였음. 45마리
        for h in range(6, 11):
            # compare는 1부터 14까지 리스트를 셔플한 값임, 실행을 누를 때마다 재배치 되도록 사용
            if a - 1 <= compre[k] <= a + 1 and b - 1 <= compre[h] <= b + 1:
                # compare[k]는 x좌표, x좌표에서 1을뺀값 부터 1을 더한값까지 ,compare[h]는 y좌표, y좌표 1을 뺀값 부터 1을 더한값까지 몬스터가 표시되도록 하였음
                array[compre[k]][compre[h]] = '🐉'
    # 초코의용 생성, 초기값은 (0,0)
    array[a][b] = '🐱‍'
    # 4,5일떄만 포탈을 생성하고 6일떄는 생성안하도록
    if floor != 6:
        # 포탈생성 앞에 좌표 고정 , 뒤에좌표 floor로 한 이유는 층이 변할 때마다 랜덤으로 포탈위치를 바꾸기 위함.
        array[compre[2]][compre[floor]] = '💠'
        # array에서 생성한 배열을 15*15로 end로 붙이고 개행을 하여 배열완성하는 포문
    for i in array:
        for j in i:
            print(j, end='')
        print()
        # 리턴값으로 array를 받아서 whire_arr에서 사용하기 위함
    return array


# 1층을 통한 와일문, floor_i는 4초기값 층, compre는 1부터 14까지 셔플된 리스트-실행시마다 랜덤재배치 위함, 포션을 메인함수에서 가져옴
# uy는 의용이의 상태창
def while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn):
    # 행,x좌표
    a = 0
    # 열, y좌표
    b = 0
    # 이동을 나타내기 위한 변수
    move = 0
    # 의용이가 포탈과 만날 때까지 진행하는 반복문, 1층 반복문
    while True:
        # 방향키를 한번눌렀을 때 50%확률로 포션 획득을 위한 랜덤변수
        get = random.randint(1, 2)
        # 몇층인지 알려주는 출력문
        print(f"=={floor_i - 3}층맵==")
        # 좌변은 arr함수의 리턴값인 array를 불러오고 우변은 arr함수를 호출하기 위함
        array_while = arr(a, b, floor_i, compre)
        # keyboard를 사용하여 input 제거하고 출력문만 나타냄
        print("방향키를 입력해주세요")
        # 방향키를 한번 누를 때마다 1씩 증감하도록함
        move += 1
        print(f"{move}이동")
        # 키보드의 올바른 작동을 위해 0.1초의 시간지연을 줌
        time.sleep(0.1)
        # 1부터 13까지 랜덤값을 가지게함
        move_a = random.randint(1, 13)
        # 6부터 13까지 랜덤값을 가지게 함
        move_b = random.randint(6, 13)
        # 움직임이 3의 배수 일 때 배치가 바뀌게 하였음
        if move % 3 == 0:
            # 배열의 위치가 x좌표가 compre[0], y좌표가 compre[1] 그것을 랜덤값을 가진 move_b,move_a 로 바뀌게 하여 3턴 마다 바뀌게 하였음
            compre[0], compre[1] = compre[move_b], compre[move_a]
            compre[1], compre[7] = compre[move_b], compre[move_a]
            # 키보드 함수에서 right를 누르면 리턴값으로 d를 받기로 하였음
        if key_board_move() == 'd':
            # b가 14인경우는 벽에 닿으므로 제외하기 위한 조건
            if b < 14:
                # 오른쪽을 누르면 b에 1이 더해지므로 그위치에 몬스터가 있으면 출력문이 나오도록함
                if array_while[a][b + 1] == '🐉':
                    print("몬스터 출현했습니다")
                    # 몬스터 대결 함수를 가져오면서 매개변수로 uy, potion을 가져옴
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                    # 움직일떄마다 1을 더하도록함
                b += 1
                # get이란 랜덤변수는 1부터 2, 1이 될때 포션을 획득하도록 함
                if get == 1:
                    # potion[0,0]은 메인함수에서 선언하였음, 앞에 값은 포션, 뒤에 값은 엘릭서임 , 포션수를 1씩 증가하게 함
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                # 벽에 다달랐을때 값고정을 함
                b = 14
        # 왼쪽을 눌렀을때 함수에서 리턴으로 a를 가짐
        elif key_board_move() == 'a':
            # b==0을 제외하기 위함
            if b > 0:
                if array_while[a][b - 1] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                b -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                b = 0

        elif key_board_move() == 's':
            if a < 14:
                if array_while[a + 1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)

                else:
                    print("몬스터가 없습니다")
                a += 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")

            else:
                a = 14

        elif key_board_move() == 'w':
            if a > 0:
                if array_while[a - 1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    battle(h1, h2, h3, h4, growth, potion, g, medi_turn)
                else:
                    print("몬스터가 없습니다")
                a -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                a = 0
        else:
            pass
        # 만약 초코의용군의 좌표(a,b)가 포탈의 위치하고 같고 floor_i가 6이 아닐때의 조건
        # floor_i는 초기값4, 1층에서는 4 2층에서는 5 3층에선 6이되므로// 1,2층에서만 발동
        if (a, b) == (compre[2], compre[floor_i]) and floor_i != 6:
            print("👏👏👏👏👏👏👏👏👏👏👏👏👏👏")
            # 브레이크를 걸어 whire_arr(1개 층을 나타내는 함수) 을 나가도록 함
            break


# def battle():
class monster():
    # 이름 , hp , 공격력, 발생확률
    def __init__(self, name, hp, power, occur_rate):
        self.name = name
        self.hp = hp
        self.power = power
        self.occur_rate = occur_rate

    def attack(self, target):
        print("몬스터의 턴입니다")
        print(f'{target.name}의 현재 hp{round(target.recent_hp)} 현재 mp{round(target.recent_mp)}')
        print(f"{self.name}의 체력: {round(self.hp)}")
        print(f'{target.name}의 체력: {round(target.recent_hp)}')
        print(f"{self.name}이 {round(self.power)}만큼의 피해를 입혔습니다.")
        target.recent_hp -= self.power
        print(f'{target.name}의 체력: {round(target.recent_hp)}')
        if target.recent_hp <= 0:
            print(f'{target.name}의 체력:0')
            print(f'{target.name}은 패배하였습니다')


# 이름, 체력, 엠피, 공격력, 피해값
# 상속만을 위한 클래스
class heroes():
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        self.name = name
        self.normal_hp = normal_hp
        self.recent_hp = recent_hp
        self.normal_mp = normal_mp
        self.recent_mp = recent_mp
        self.power = power


class warrior(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    def attack_skill(self, enemy):
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')
        skill_selection = int(input("0. 일반공격 1. 파워스트라이크, 2. 몸통박치기, 3.동귀어진"))
        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (파워 스트라이크) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 1.5)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 1.5)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (몸통박치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 2)}만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (동귀어진) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 3)}만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 3)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")

        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')



class bard(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    def attack_skill(self, enemy, h1, h2, h3, h4):
        print("바드의 노래시간입니다")
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')
        skill_selection = int(input("0. 일반공격 1. 수호의 연주, 2. 죽음의 전주곡, 3.폭풍의 서곡"))
        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (수호의연주) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.02)
            h2.power += round(h2.power * 1.02)
            h3.power += round(h3.power * 1.02)
            h4.power += round(h4.power * 1.02)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (죽음의 전주곡) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.04)
            h2.power += round(h2.power * 1.04)
            h3.power += round(h3.power * 1.04)
            h4.power += round(h4.power * 1.04)
            self.recent_mp = self.recent_mp - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")

        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (폭풍의 서곡) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            h1.power += round(h1.power * 1.06)
            h2.power += round(h2.power * 1.06)
            h3.power += round(h3.power * 1.06)
            h4.power += round(h4.power * 1.06)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")

        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')



class medi_fighther(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    def attack_skill(self, enemy, potion, medi_turn):
        skill_selection = int(input("0. 일반공격 1.약하게 치기, 2. 몸통박치기, 3.쎄게 치기 4.기력 포션제조 5. 활력 포션제조 6. 하프엘릭서 제조"))
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{enemy.hp}')

        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp - self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}이 (약하게 치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 1.5)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 1.5)
            self.recent_mp = round(self.recent_mp) - 100
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 2 and self.recent_mp < 200:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 2 and self.recent_mp >= 200:
            print(f"{self.name}이 (몸통박치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 2)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 200
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 3 and self.recent_mp < 300:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 3 and self.recent_mp >= 300:
            print(f"{self.name}이 (쎄게 치기) 사용")
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print(f"{enemy.name}에 {round(self.power * 3)}만큼의 피해를 입혔습니다.")
            enemy.hp = enemy.hp - (self.power * 3)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"{self.name}의 남은 mp:{self.recent_mp}")
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        if skill_selection == 4 and self.recent_mp <= 99:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 4 and self.recent_mp > 99:
            print("기력 포션을 제조합니다")
            self.recent_mp = self.recent_mp - 100
            medi_turn[0] = 1
            potion[3] += 1
        if skill_selection == 5 and self.recent_mp <= 199:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")


        if skill_selection == 5 and self.recent_mp > 199:
            print("활력 포션을 제조합니다")
            self.recent_mp = round(self.recent_mp) - 200
            medi_turn[0] = 1
            potion[4] += 1
        if skill_selection == 6 and self.recent_mp <= 299:
            print(f"{enemy.name}의 hp:{enemy.hp}")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            enemy.hp = enemy.hp - round(self.power)
            print(f"일반 공격으로 입힌 데미지:{round(self.power)}")

        if skill_selection == 6 and self.recent_mp > 299:
            print("하프 엘리서를 제조합니다")
            self.recent_mp = self.recent_mp - 300
            medi_turn[0] = 1
            potion[5] += 1
        if enemy.hp > 0:
            print(f"{enemy.name}의 남은 체력:{round(enemy.hp)}")
        else:
            print(f'{enemy.name}이(가) 죽었습니다.')

        return medi_turn


class archer(heroes):
    def __init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power):
        heroes.__init__(self, name, normal_hp, recent_hp, normal_mp, recent_mp, power)

    def attack_skill(self, enemy):
        skill_selection = int(input("0.일반공격 1.폭풍활, 2.폭풍화살, 3.용의 일격"))
        print(f'{self.name}의 현재 hp{round(self.recent_hp)} 현재 mp{round(self.recent_mp)}')
        print(f'{enemy.name}의 hp:{round(enemy.hp)}')

        if skill_selection == 0:
            print("일반 공격을 사용합니다")
            enemy.hp = round(enemy.hp) - round(self.power)
            if enemy.hp > 0:
                print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print('='*50)
                print(f'[{enemy.name}]가 죽었습니다.')

        if skill_selection == 1 and self.recent_mp <= 99:

            print(f"{enemy.name}의 hp:[{round(enemy.hp)}]")
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다.")

            enemy.hp = round(enemy.hp) - round(self.power)
            if enemy.hp > 0:
                print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
                print(f"{enemy.name}의 남은 체력:[{round(enemy.hp)}]")

            else:
                print(f'[{enemy.name}]이(가) 죽었습니다.')

        if skill_selection == 1 and self.recent_mp > 99:
            print(f"{self.name}가  폭풍활 사용")
            print(f'적에게 일반 공격 두번 합니다')
            print(f"{enemy.name}의 hp:{round(enemy.hp)}")
            enemy.hp = round(enemy.hp) - round(self.power * 2)
            self.recent_mp = round(self.recent_mp) - 100

            print(f"{enemy.name}에 [{round(self.power) * 2}]만큼의 피해를 입혔습니다.")
            print(f"{self.name}의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if skill_selection == 2 and self.recent_mp < 200:
            print('mp가 부족합니다')
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            print(f"{enemy.name}의 hp:{round(enemy.hp)}")

            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print('[{enemy.name}] 죽었습니다.')

        if skill_selection == 2 and self.recent_mp >= 200:

            print(f"{self.name}가 폭풍화살 사용")
            print(f"{enemy.name}의 hp:[{round(enemy.hp)}]")
            print(f"{enemy.name}에 [{round(self.power * 3)}]만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power) * 3
            self.recent_mp = round(self.recent_mp)- 200
            print(f"{self.name}의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if skill_selection == 3 and self.recent_mp < 300:
            print('mp가 부족합니다')
            print("스킬을 사용할수 없습니다. 일반 공격을 사용합니다")
            print(f"[{enemy.name}]의 hp:[{enemy.hp}]")

            enemy.hp = round(enemy.hp) - round(self.power)
            print(f"일반 공격으로 입힌 데미지:[{round(self.power)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}]이(가) 죽었습니다.')

        if skill_selection == 3 and self.recent_mp >= 300:

            print(f"[{self.name}]이 용의 일격 사용")
            print(f"[{enemy.name}]의 hp:[{round(enemy.hp)}]")
            print(f"[{enemy.name}]에 [{round(self.power * 5)}]만큼의 피해를 입혔습니다.")
            enemy.hp = round(enemy.hp) - round(self.power * 5)
            self.recent_mp = round(self.recent_mp) - 300
            print(f"[{self.name}]의 남은 mp:[{round(self.recent_mp)}]")
            if enemy.hp > 0:
                print(f"[{enemy.name}]의 남은 체력:[{round(enemy.hp)}]")
            else:
                print(f'[{enemy.name}] 죽었습니다.')

        if enemy.hp <= 0:
            print(f"[{enemy.name}]을 죽었습니다.")
        else:
            print(f"[{enemy.name}]의 hp가 [{round(enemy.hp)}]이 되었습니다.")




class normal(monster):
    def __init__(self, name, hp, power, occur_rate):
        monster.__init__(self, name, hp, power, occur_rate)


class boss(monster):
    def __init__(self, name, hp, power, occur_rate):
        monster.__init__(self, name, hp, power, occur_rate)


class zombie(normal):
    def __init__(self):
        self.name = '좀비'
        self.hp = random.randint(300, 500)
        self.power = 100
        self.occur_rate = 46.5


class ghoul(normal):
    def __init__(self):
        self.name = '구울'
        self.hp = random.randint(450, 700)
        self.power = 180
        self.occur_rate = 30


class skull(normal):
    def __init__(self):
        self.name = '해골'
        self.hp = random.randint(480, 800)
        self.power = 220
        self.occur_rate = 12


class bugbear(normal):
    def __init__(self):
        self.name = '버그베어'
        self.hp = random.randint(550, 900)
        self.power = 350
        self.occur_rate = 5


class arhendo(boss):
    def __init__(self):
        self.name = '아르헨도'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class chulmom(boss):
    def __init__(self):
        self.name = '철몸'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class gubum(boss):
    def __init__(self):
        self.name = '규범이'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class minju(boss):
    def __init__(self):
        self.name = '민주석'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class ilsung(boss):
    def __init__(self):
        self.name = '일성김'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class uyoun(boss):
    def __init__(self):
        self.name = '우연이'
        self.hp = random.randint(5000, 10000)
        self.power = random.randint(1000, 3000)
        self.occur_rate = 1


class diabloc(boss):
    def __init__(self):
        self.name = '디아복로'
        self.hp = random.randint(10000, 20000)
        self.power = random.randint(2500, 3000)
        self.occur_rate = 0.2


class choco(warrior):
    def __init__(self):
        self.name = '초코의용'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class kingtae(bard):
    def __init__(self):
        self.name = '킹기태'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class bumgu(medi_fighther):
    def __init__(self):
        self.name = '약범규'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)


class bowhunjae(archer):
    def __init__(self):
        self.name = '보우현재'
        self.normal_hp = 500
        self.recent_hp = 500
        self.normal_mp = 300
        self.recent_mp = 300
        self.power = random.randint(100, 150)
def battle(h1, h2, h3, h4, growth, potion, g, medi_turn):
    # if 0 not in g:
    #     exit()
    n1 = zombie()
    n2 = ghoul()
    n3 = skull()
    n4 = bugbear()
    n = [n1, n2, n3, n4]
    turn = 0

    b1 = arhendo()
    b2 = chulmom()
    b3 = gubum()
    b4 = minju()
    b5 = ilsung()
    b6 = uyoun()
    b7 = diabloc()
    b_list = [b1, b2, b3, b4, b5, b6, b7]
    occur = random.randint(1, 1000)

    if occur <= 465:
        mob = n1
    elif occur <= 765:
        mob = n2
    elif occur <= 885:
        mob = n3
    elif occur <= 935:
        mob = n4
    elif occur <= 945:
        mob = b1
    elif occur <= 955:
        mob = b2
    elif occur <= 965:
        mob = b3
    elif occur <= 975:
        mob = b4
    elif occur <= 985:
        mob = b5
    elif occur <= 995:
        mob = b6
    elif occur <= 1000:
        mob = b7
    while True:
        select = int(input("1.싸운다 2.포션 먹기 3.도망간다 4.기력 포션 먹기 5.활력 포션 먹기 6.하프 엘릭서 먹기 7.엘릭서 먹기 "))
        if select == 1 and h1.recent_hp > 0:
            print("용사턴=======")

            h1.attack_skill(mob)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                print("[아르헨도, 철몸, 규범, 민주, 일성, 우연, 디아블로]", g)
                if 0 not in g:
                    print("=======================")
                    print("=======================")
                    print("=======================")
                    exit()
                potion_class(potion).liquid_get()
                grooth(h1, h2, h3, h4, growth, potion)
                break
            medi_turn[0] = 0
            h2.attack_skill(mob, potion, medi_turn)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                    print("=======", g)
                if 0 not in g:
                    print("=======================")
                    print("=======================")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                break

            h3.attack_skill(mob)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")
                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                    print("=======", g)
                if 0 not in g:
                    print("=======================")
                    print("=======================")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                break

            h4.attack_skill(mob, h1, h2, h3, h4)
            if mob.hp <= 0:
                print("몬스터의 패배입니다")

                for i in range(0, len(b_list)):
                    if mob == b_list[i]:
                        g[i] = 1
                    print("=======", g)
                if 0 not in g:
                    print("=======================")
                    print("=======================")
                    print("=======================")
                    exit()
                grooth(h1, h2, h3, h4, growth, potion)
                break



        if select == 2:
            hero_select = int(input('1.초코의용, 2.약범규 3.보우현재 4.킹기태  캐릭터를 선택해주세요'))
            if hero_select == 1:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h1)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 2:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h2)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 3:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h3)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass
            if hero_select == 4:
                if potion[0] > 0:
                    potion_class(potion).liquid_recovery(h4)
                    pass
                else:
                    print("포션의 갯수가 0개입니다", potion[0])
                    pass

        if select == 3:
            run = random.randint(1, 10)
            if run <= 1:
                print("도망에 성공 했다")
                return
            else:
                print("도망에 실패했다")
                mob.attack(h1)
                mob.attack(h2)
                mob.attack(h3)
                mob.attack(h4)
                if h1.recent_hp <= 0 and h2.recent_hp <= 0 and h3.recent_hp <= 0 and h4.recent_hp <= 0:
                    print("용사팀의 패배입니다")
                    exit()
                # if mob.hp <= 0:
                #     print("몬스터의 패배입니다")
                #     break
        if select == 4 and medi_turn[0] == 1:
            if potion[3] > 0:
                potion_class(potion).mana_potion(h1, h2, h3, h4)
                potion[3] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
        if select == 5 and medi_turn[0] == 1:
            if potion[4] > 0:
                potion_class(potion).health_potion(h1, h2, h3, h4)
                potion[4] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
        if select == 6 and medi_turn[0] == 1:
            if potion[5] > 0:
                potion_class(potion).half_elixer(h1, h2, h3, h4)
                potion[5] -= 1
                pass
            else:
                print("포션의 갯수가 0개입니다")
                print("다시 선택 해주세요")
                pass
        if select==7:
            if potion[1]<=0:
                print("포션의 갯수가 0개입니다")
                pass
            else:
                potion[1]-=1
                turn=10
                print("엘릭서를 사용합니다")
                print("남은 무적 턴의 숫자:",turn)
                print("엘릭서 사용하고 남은 갯수", potion[1])

            print("몬스터턴==============")
        if turn==0:
            print("엘릭서의 턴이 0일때!!!!!!!!",turn)
            mob.attack(h1)
            if h1.recent_hp <= 0:
                print("초코의용은 죽었습니다")
                # exit()
                pass
            mob.attack(h2)
            if h2.recent_hp <= 0:
                print("약범규는 죽었습니다.")
                pass
            mob.attack(h3)
            if h3.recent_hp <= 0:
                print("보우현재는 죽었습니다.")
                pass
            mob.attack(h4)
            if h4.recent_hp <= 0:
                print("킹기태는 죽었습니다.")
                pass

            if h1.recent_hp and h2.recent_hp <= 0 and h3.recent_hp <= 0 and h4.recent_hp <= 0:
                print("용사팀 패배")
                exit()
        elif turn>0:
            turn-=1
            print(f"엘릭서의 효과발동!!!!!!!! 남은 무적턴:{turn}")

            pass
        else:
            print("잘못된 키 입력입니다 다시눌러주세요")
            pass
    return g





# select_first(h1,h2)


class potion_class:
    def __init__(self, potion):
        self.potion = potion

    def liquid_get(self):
        get = random.randint(1, 10)
        elixer_get=random.randint(1,1000)
        if get <= 1:
            self.potion[0] += 1
            print("포션 이벤트 성공~~~~~~~~~~~~~~~")
            print(f"포션을 얻었습니다.!!!!!!! 현재 포션의 갯수:{self.potion[0]}")
            if elixer_get<=5:
                self.potion[1]+=1
                print(f"엘릭서를 얻었습니다 엘릭서의 갯수:{self.potion[1]}",)
            else:
                pass
        else:
            pass

    def liquid_recovery(self, hiro):
        self.potion[0] -= 1
        print("^^^^^^")
        print('포션 갯수', self.potion[0])
        recovery_rate = (random.randint(3, 8) * 0.1)
        hiro.recent_hp += (hiro.recent_hp * recovery_rate)
        print(f"포션먹고 hp:{round(hiro.recent_hp)}")
        if hiro.normal_hp < hiro.recent_hp:
            hiro.recent_hp = hiro.normal_hp
            print(f"수정 hp:{hiro.recent_hp}")
        hiro.recent_mp += (hiro.recent_mp * recovery_rate)

    def mana_potion(self, h1, h2, h3, h4):
        print("기력 포션을 사용합니다 파티원들의 마나를 60%채웁니다")
        h1.recent_mp += (h1.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h1.normal_mp < h1.recent_mp:
            h1.recent_mp = h1.normal_mp
            print(f"수정 mp:{h1.normal_mp}")
        print("===========================")
        h2.recent_mp += (h2.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h2.normal_mp < h2.recent_mp:
            h2.recent_mp = h2.normal_mp
            print(f"수정 mp:{h2.normal_mp}")
        print("===========================")
        h3.recent_mp += (h3.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h3.normal_mp < h3.recent_mp:
            h3.recent_mp = h3.normal_mp
            print(f"수정 mp:{h3.normal_mp}")
        print("===========================")
        h4.recent_mp += (h4.recent_mp * 0.6)
        print(f"포션먹고 mp:{round(h1.recent_mp)}")
        if h4.normal_mp < h4.recent_mp:
            h4.recent_mp = h4.normal_mp
            print(f"수정 mp:{h4.normal_mp}")

    def health_potion(self, h1, h2, h3, h4):
        print("활력 포션을 사용합니다 파티원들의 체력을 60%채웁니다")
        h1.recent_hp += (h1.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h1.normal_hp < h1.recent_hp:
            h1.recent_hp = h1.normal_hp
            print(f"수정 hp:{h1.normal_hp}")
        print("===========================")
        h2.recent_hp += (h2.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h2.normal_hp < h2.recent_hp:
            h2.recent_hp = h2.normal_hp
            print(f"수정 hp:{h2.normal_hp}")
        print("===========================")
        h3.recent_hp += (h3.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h3.normal_hp < h3.recent_hp:
            h3.recent_hp = h3.normal_hp
            print(f"수정 hp:{h3.normal_hp}")
        print("===========================")
        h4.recent_hp += (h4.recent_hp * 0.6)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h4.normal_hp < h4.recent_hp:
            h4.recent_hp = h4.normal_hp
            print(f"수정 hp:{h4.normal_hp}")

    def half_elixer(self, h1, h2, h3, h4):
        print("하프 엘릭서를 사용합니다 파티원들의 체력을 80%채웁니다")
        h1.recent_hp += (h1.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h1.recent_hp)}")
        if h1.normal_hp < h1.recent_hp:
            h1.recent_hp = h1.normal_hp
            print(f"수정 hp:{h1.normal_hp}")
        print("===========================")
        h2.recent_hp += (h2.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h2.recent_hp)}")
        if h2.normal_hp < h2.recent_hp:
            h2.recent_hp = h2.normal_hp
            print(f"수정 hp:{h2.normal_hp}")
        print("===========================")
        h3.recent_hp += (h3.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h3.recent_hp)}")
        if h3.normal_hp < h3.recent_hp:
            h3.recent_hp = h3.normal_hp
            print(f"수정 hp:{h3.normal_hp}")
        print("===========================")
        h4.recent_hp += (h4.recent_hp * 0.8)
        print(f"포션먹고 hp:{round(h4.recent_hp)}")
        if h4.normal_hp < h4.recent_hp:
            h4.recent_hp = h4.normal_hp
            print(f"수정 hp:{h4.normal_hp}")



def grooth(h1, h2, h3, h4, growth, potion):
    h1.power += (h1.power * growth)
    h1.recent_hp += (h1.recent_hp * growth)
    h1.recent_mp += (h1.recent_mp * growth)
    h1.normal_hp += (h1.normal_hp * growth)
    h1.normal_mp += (h1.normal_mp * growth)
    h2.power += (h2.power * growth)
    h2.recent_hp += (h2.recent_hp * growth)
    h2.recent_mp += (h2.recent_mp * growth)
    h2.normal_hp += (h2.normal_hp * growth)
    h2.normal_mp += (h2.normal_mp * growth)
    h3.power += (h3.power * growth)
    h3.recent_hp += (h3.recent_hp * growth)
    h3.recent_mp += (h3.recent_mp * growth)
    h3.normal_hp += (h3.normal_hp * growth)
    h3.normal_mp += (h3.normal_mp * growth)
    h4.power += (h4.power * growth)
    h4.recent_hp += (h4.recent_hp * growth)
    h4.recent_mp += (h4.recent_mp * growth)
    h4.normal_hp += (h4.normal_hp * growth)
    h4.normal_mp += (h4.normal_mp * growth)
    return h1, h2, h3, h4, growth, potion





def main():
    medi_turn = [0]
    g = [0, 0, 0, 0, 0, 0, 0]
    growth = random.randint(2, 5) * 0.01
    h1 = choco()
    h2 = bumgu()
    h3 = bowhunjae()
    h4 = kingtae()
    potion = [0, 20, 0, 0, 0, 0]
    floor_i = 4
    # 이 리스트를 이용해 몬스터, p값 생성, 맵의 초기 좌표가 (0,0)이므로 겹치지 않게 하기 위해 1부터 시작하게 하였음.
    compre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # 셔플을 주어 실행을 할떄마다 랜덤한 위치에 생성하도록 함
    random.shuffle(compre)
    # 앞에 것은 포션, 뒤에 것은 엘릭서
    # 1층에대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)
    print("2층 맵을 시작합니다 ==========")
    # 층을 증가시키기 위한 증감식
    floor_i += 1
    # 2층에대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)
    print("3층 맵을 시작합니다 ==========")
    floor_i += 1
    # 3층에 대한 함수 호출
    while_arr(floor_i, compre, potion, h1, h2, h3, h4, growth, g, medi_turn)


# 1~3층이 들어가있는(while_arr)을 호출하기 위한 메인함수 호출
main()






