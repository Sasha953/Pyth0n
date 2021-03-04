import random
i = int(input('Вставьте от какого числа будет рандом: '))
o = int(input('Вставьте до какого числа будет рандом: '))
b = random.randrange(i, o)
a = int(input('Число: '))
if a  == b:
    print("Ты победил!")
else:
    print()
    print(b)
    print('Потрачено:(')