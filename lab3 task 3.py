# TODO  Напишите функцию count_letters
def count_letters(text):
    letter_count = {}
    for char in text.lower():  # Преобразуем текст в нижний регистр
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())  # Общее количество букв
    frequency_dict = {}
    for letter, count in letter_count.items():
        frequency_dict[letter] = round(count / total_letters, 2)  # Округляем до двух знаков
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count = count_letters(main_str)

# Вычисление частоты букв
frequency_dict = calculate_frequency(letter_count)

# Вывод частот в столбик
for letter, freq in frequency_dict.items():
    print(f"{letter}: {freq:.2f}")