# 1. Печать только нечетных чисел
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print("Нечетное:", i)


# 2. Пропуск конкретного числа
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Число:", i)


# 3. Фильтрация отрицательных значений при вводе
count = 0
while count < 3:
    num = int(input("Введите число: "))
    if num < 0:
        print("Пропускаем отрицательное")
        continue
    print("Вы ввели:", num)
    count += 1


# 4. Пропуск определенных букв в слове
word = "hello"
i = 0
while i < len(word):
    char = word[i]
    i += 1
    if char == "l":
        continue
    print("Буква:", char)


# 5. Обработка только чисел, кратных 5
n = 0
while n < 30:
    n += 1
    if n % 5 != 0:
        continue
    print("Кратно 5:", n)