import pickle
list = [input('Введите: ').split()]
try:
    file = open("favorites.dat.", "wb")

    try:
        pickle.dump(things, file)
    finally:
        file.close()

except FileNotFoundError:
    print("Неполучилось:(")