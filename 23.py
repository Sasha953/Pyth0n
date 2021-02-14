#Заданий рядок зі словами і числами, розділеними пробілами (один пробіл між словами та / або числами).
#Слова складаються тільки з букв. Вам потрібно перевірити чи є у вихідному рядку три слова підряд.
#Наприклад, в рядку "start 5 one two three 7 end" є три слова підряд.
#Вхідні дані: Рядок зі словами (str).
#Вихідні дані: Відповідь як логічне значення (bool), True або False.

a = input('(Макс. 6 слов)Введите предложение: ').split()
if a[0].isdigit():
    print("True")
if a[1].isdigit():
    print("True")
if a[2].isdigit():
    print("True")
if a[3].isdigit():
    print("True")
if a[4].isdigit():
    print("True")
if a[5].isdigit():
    print("True")
if a[6].isdigit():
    print("True")
