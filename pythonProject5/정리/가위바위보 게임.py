import random

game = ['x','x','o','x','x']

while True:
    a = random.randint(1,2)
    if a == 1:
        game.pop(-1)
        game.insert(0,'x')
        print('a 승리')


        if game[-1] == 'o':
            print(game)
            break

    else:
        print('b 승리')
        game.pop(0)
        game.insert(-1,'x')


        if game[0] == 'o':
            print(game)
            break

    print(game)

