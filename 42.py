import pickle #Добавляет модуль pickle
list = [input('Введите: ').split()] #Позволят не менять код при заполнении а просто ввести
try:
    file = open("favorites.dat.", "wb") #Создает файл

    try:
        pickle.dump(things, file) #возвращает сериализованный объект
    finally:
        file.close() #Завершает процесс

except FileNotFoundError:
    print("Неполучилось:(") #Если что-то не так