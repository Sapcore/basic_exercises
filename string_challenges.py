# Вывести последнюю букву в слове
print("Task 1")
word = 'Архангельск'
print(f'Последняя буква слова "{word}" - это "{word[-1]}".')
print()


# Вывести количество букв "а" в слове
print('Task 2')
word = 'Архангельск'
letter = 'а'
print(f'Количество букв "{letter}" в слове "{word}" равно {word.lower().count(letter)}.')
print()


# Вывести количество гласных букв в слове
print("Task 3")
word = 'Архангельск'
vowels = 'аиеёоуыэюя'
count_vowels = 0
for char in vowels:
    count_vowels += word.count(char)
print(f'Количество гласных буквы в слове "{word}" равно {count_vowels}.')
print()


# Вывести количество слов в предложении
print('Task 4')
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении "{sentence}" равно {sentence.count(" ") + 1}.')
print()


# Вывести первую букву каждого слова на отдельной строке
print("Task 5")
sentence = 'Мы приехали в гости'
print(f'Предложение "{sentence}", выведенное по первым буквам каждого слова, выглядит следующим образом:')
for word in sentence.split():
    print(word[0])
print()


# Вывести усреднённую длину слова в предложении
print('Task 6')
sentence = 'Мы приехали в гости'
letters_qty = len(sentence) - sentence.count(' ')
words_qty = sentence.count(' ') + 1
print(f'Усредненная длина слова в предложении "{sentence}" равна {letters_qty / words_qty}.')