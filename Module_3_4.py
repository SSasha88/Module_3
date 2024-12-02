# Самостоятельная работа по уроку "Произвольное число параметров"
# Создаю функцию
def single_root_words(root_word, *other_words):
    # Создаю пустой список
    same_words = []
    # Перевожу в нижний регистр root_word для сравнения
    root_word_lower = root_word.lower()
    # Прохожу по каждому слову из других слов
    for word in other_words:
        # Перевожу текущее слово в нижний регистр для сравнения
        word_lower = word.lower()
        # Проверяю на условие
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words
print('Задача "Однокоренные"')

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)