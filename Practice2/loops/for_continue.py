# 1. Пропуск фрукта из списка
for f in ["apple", "banana", "cherry"]:
    if f == "banana":
        continue
    print("Едим:", f)


# 2. Печать чисел, кроме делящихся на 3
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print("Число:", i)


# 3. Игнорирование пустых строк в списке
for text in ["привет", "", "мир"]:
    if not text:
        continue
    print("Текст:", text)


# 4. Обработка только положительных чисел
for n in [5, -2, 10, -1, 3]:
    if n < 0:
        continue
    print("Положительное:", n)


# 5. Пропуск заглавных букв
for char in "PyThOn":
    if char.isupper():
        continue
    print("Маленькая буква:", char)