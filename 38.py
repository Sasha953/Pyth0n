#Запишіть кожне слово окремо до масиву, а потім напишіть невелику програму, яка друкує слова з наступного рядка через одне, починаючи з першого слова («цей»):
A = ['Этот', 'если', 'способ', 'вы', 'плохо', 'это', 'подходит', 'читаете', 'для', 'чего-то', 'шифрования', 'пошло']
A += ['важных', 'не', 'сообщений', 'так']

for i in range(len(A)):
    if i % 2 == 0:
        print(A[i], end=' ')