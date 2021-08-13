import random

def generate_random_words(count=1, length=14):
    current_count = 0
    characters = list('abcdefghijklmnopqrstuvwxyz')
    while current_count < count:
        random_word = ""
        for index in range(length):
            random_word += random.choice(characters)
        yield random_word
        current_count += 1

def even_numbers(start=1,end=100):
    for number in range(start, end):
        if number%2 == 0:
            yield number



if __name__ == '__main__':
    for even in even_numbers(10, 20):
        print(even)
    for random_word in generate_random_words(count=4):
        print(random_word)


