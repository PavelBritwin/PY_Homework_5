#Крестики-нолики
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
color = [37, 37, 37, 37, 37, 37, 37, 37, 37]
currentPlayer = 'Игрок O'
def checkWin():
    if field[0] == field[1] == field[2] or field[3] == field[4] == field[5] or field[6] == field[7] == field[8] or \
        field[0] == field[3] == field[6] or field[1] == field[4] == field[7] or field[2] == field[5] == field[8] or \
        field[0] == field[4] == field[8] or field[2] == field[4] == field[6]:
        return False
    return True
def printField(currentStep):
    if field[currentStep] == 'X':
        color[currentStep] = '31'
    elif field[currentStep] == 'O':
        color[currentStep] = '34'
    else:
        color[currentStep] = '37'
    print("\033[{}m{}".format(color[0], field[0]), "\033[{}m{}".format(color[1], field[1]), "\033[{}m{}".format(color[2], field[2]))
    print("\033[{}m{}".format(color[3], field[3]), "\033[{}m{}".format(color[4], field[4]), "\033[{}m{}".format(color[5], field[5]))
    print("\033[{}m{}".format(color[6], field[6]), "\033[{}m{}".format(color[7], field[7]), "\033[{}m{}".format(color[8], field[8]))
printField(1)
while checkWin():
    if currentPlayer == 'Игрок X':
        currentPlayer = 'Игрок O'
    else:
        currentPlayer = 'Игрок X'
    step = int(input('\033[37mХодит {}. Введите цифру с игрового поля: '.format(currentPlayer)))
    if currentPlayer == 'Игрок X':
        field[step - 1] = 'X'
    else:
        field[step - 1] = 'O'
    printField(step - 1)
print('\033[37mПобедил игрок {}'.format(currentPlayer))
