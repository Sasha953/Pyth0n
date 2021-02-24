a = input()

b = 0
while a[b] == ' ':
    b += 1
a = a[b:]

b = len(a)
while a[b - 1] == ' ':
    b -= 1
a = a[:b]

o = a[0]
i = 1
while i < len(a):
    if a[i] != ' ':
        o += a[i]
    elif a[i - 1] != ' ':
        o += '*'
    i += 1
print(o)