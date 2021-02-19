a = input('Введите первую строку: ').split()
b = input('Введите вторую строку: ').split()
c = []

for i in a:
    for r in b:
        if i == r:
            c.append(i)
            break
print(c)