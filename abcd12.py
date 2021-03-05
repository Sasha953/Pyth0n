from itertools import groupby
from operator import itemgetter

word_list = input().split()

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)