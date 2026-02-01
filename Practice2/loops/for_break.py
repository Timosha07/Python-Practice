# 1. Поиск элемента в списке
for x in [10, 20, 30, 40]:
    if x == 30:
        print("Нашли 30!")
        break


# 2. Остановка при обнаружении ошибки (None)
for val in [1, 2, None, 4]:
    if val is None:
        print("Ошибка данных")
        break
    print("Данные:", val)


# 3. Поиск первой гласной в слове
for letter in "rhythm":
    if letter in "aeiouy":
        print("Первая гласная:", letter)
        break


# 4. Прерывание вложенного цикла (внешний продолжается)
for i in range(3):
    for j in range(10):
        if j > 2:
            break
        print(f"i={i}, j={j}")


# 5. Выход при превышении лимита суммы
s = 0
for i in range(1, 100):
    s += i
    if s > 50:
        print("Сумма превысила 50 на числе", i)
        break