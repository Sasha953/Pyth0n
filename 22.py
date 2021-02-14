#У заданому тексті потрібно підсумовувати числа. Необхідно рахувати лише окремі числа.
#Якщо число є частиною слова, воно не повинно рахуватися. Текст складається з цифр, пробілів та англійських букв.
#Введення: Рядок.
#Вихід: Int.

sum_numbers = 0
text = input("Enter your text: ")
for word in text.split():
    if word.isdigit():
        sum_numbers = sum_numbers + int(word)
print(sum_numbers)