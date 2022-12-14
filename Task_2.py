import random

sweets = 100
step = 28
player = random.randrange(1, 3)
while sweets > 28:
    step = int(input(f'Ход игрока {player}. Введите количество конфет: '))
    if (0 > step or step > 28):
        print('Нарушение правил игры! Количество конфет, взятых за один ход должно быть в пределах: 0 < step < 29')
        continue
    sweets -= step
    print(f'Осталось конфет: {sweets}')
    if player == 1:
        player = 2
    else:
        player = 1
print(f'Игрок {player} забирает последние конфеты, он победил!')