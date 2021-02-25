list = input().split()

j = 0

for j in range(len(list)):
    for i in range(len(list) -1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
        i += 1
print (list)