list = input('Введите строку: ').split()
print('-------------------')
for elem in list:
    print(elem, ' - ', list.count(elem))
#r=[]
#for i in range (len(list)):
#    for j in range (len(r)):
#        if list[i] == r[j]:
#           print(list[i])