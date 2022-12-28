import random
sweets = 89
step = 0
players = ['Компьютер', 'Игрок']
random.shuffle(players)
currentPlayer = players[0]
while sweets > 28:
    if (currentPlayer == 'Игрок'):
        step = int(input(f'Ходит {currentPlayer}. Введите количество конфет: '))
        if (0 > step or step > 28):
            print('Нарушение правил игры! Количество конфет, взятых за один ход должно быть в пределах: 0 < step < 29')
            continue
    else:
        if sweets % 29 == 0:
            step = random.randint(1, 28)
        else:
            step = sweets % 29
        print(f'Ходит {currentPlayer}: взял {step} конфет')
    sweets -= step
    print(f'Осталось конфет: {sweets}')
    if currentPlayer == 'Компьютер':
        currentPlayer = 'Игрок'
    else:
        currentPlayer = 'Компьютер'
print(f'Игрок {currentPlayer} забирает последние конфеты, он победил!')
