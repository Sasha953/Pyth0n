a = [1, 3, 8, 7]
b = [1, 3, 8, 7]

print(a[0])
print(a[-1])

print()

print(a[1:])
print(a[-2:])
print(a[-1:])

print()

print(a[::1])
print(a[::2])
print(a[::3])
print(a[::4])
print(a[::-4])
print(a[::-3])
print(a[::-2])
print(a[::-1])

print()

print(a[1:4])
print(a[2:3])

print()

a[1:3] = [0, 0, 0]
print(a)