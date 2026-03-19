from functools import reduce

def practice_functional():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Исходный список: {numbers}")

    #  map() — возводим каждое число в квадрат
    squared = list(map(lambda x: x**2, numbers))
    print(f"Квадраты чисел (map): {squared}")

    #  filter() — оставляем только четные числа
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Только четные (filter): {evens}")

    #  reduce() — перемножаем все числа в списке (агрегация)
    # Считает так: (((1*2)*3)*4...)
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
    print(f"Произведение чисел от 1 до 5 (reduce): {product}")

if __name__ == "__main__":
    practice_functional()