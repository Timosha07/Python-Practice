# 1. Поиск первого числа, делящегося на 7
n = 1
while True:
    if n % 7 == 0:
        print("Первое число:", n)
        break
    n += 1


# 2. Ограничение попыток ввода пароля
attempts = 3
while attempts > 0:
    pwd = input("Пароль: ")
    if pwd == "secret":
        print("Доступ разрешен")
        break
    attempts -= 1


# 3. Выход из бесконечного цикла по условию
i = 0
while True:
    print("Итерация", i)
    if i == 4:
        break
    i += 1


# 4. Поиск символа в строке
s = "Python"
idx = 0
while idx < len(s):
    if s[idx] == "h":
        print("Найдено 'h' на индексе", idx)
        break
    idx += 1


# 5. Прерывание при достижении критического значения
val = 1
while val < 1000:
    if val > 50:
        print("Слишком много:", val)
        break
    val *= 3