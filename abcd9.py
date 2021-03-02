a = ['-', '-', '-','-', '-', '-','-', '-', '-']
p = 1
w = 0

while w == 0:
    if p == 1:
        b = int(input('Введите число от 1 до 9: ')) - 1
        a[b] = 'X'
        print(a[0], a[1], a[2])
        print(a[3], a[4], a[5])
        print(a[6], a[7], a[8])
        p = 0
    if p == 0:
        b = int(input('Введите число от 1 до 9: ')) - 1
        a[b] = 'O'
        print(a[0], a[1], a[2])
        print(a[3], a[4], a[5])
        print(a[6], a[7], a[8])
        p = 1
    if a[0] and a[1] and a[2] == 'X':
        w = 1
    if a[3] and a[4] and a[5] == 'X':
        w = 1
    if a[6] and a[7] and a[8] == 'X':
        w = 1
    if a[0] and a[3] and a[6] == 'X':
        w = 1
    if a[1] and a[4] and a[7] == 'X':
        w = 1
    if a[2] and a[5] and a[8] == 'X':
        w = 1
    if a[0] and a[4] and a[8] == 'X':
        w = 1
    if a[2] and a[4] and a[6] == 'X':
        w = 1
    if a[0] and a[1] and a[2] == 'O':
        w = 1
    if a[3] and a[4] and a[5] == 'O':
        w = 1
    if a[6] and a[7] and a[8] == 'O':
        w = 1
    if a[0] and a[3] and a[6] == 'O':
        w = 1
    if a[1] and a[4] and a[7] == 'O':
        w = 1
    if a[2] and a[5] and a[8] == 'O':
        w = 1
    if a[0] and a[4] and a[8] == 'O':
        w = 1
    if a[2] and a[4] and a[6] == 'O':
        w = 1
    else:
        w = 0
if w == 1:
    print('Win!!!')