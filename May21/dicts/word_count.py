word = input('Enter the word: ')
letter_counts = {}
for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1
print(letter_counts)

# Vowel Count
vowels = 'aeiou'
vowel_count = {}
for letter in word:
    if letter in vowels:
        if letter in vowel_count:
            vowel_count[letter] += 1
        else:
            vowel_count[letter] = 1
print(vowel_count)