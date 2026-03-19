def practice_iteration_and_types():
    names = ["Kanye", "Travis", "Drake"]
    albums = ["Graduation", "Astroworld", "Views"]

    #  zip() — объединяем два списка в пары
    # enumerate() — добавляем порядковый номер (индекс)
    print("--- Список артистов и альбомов ---")
    for i, (name, album) in enumerate(zip(names, albums), start=1):
        print(f"{i}. Артист: {name}, Альбом: {album}")

    print("\n--- Проверка типов (Type checking) ---")
    # Demonstrate type checking and conversions
    value = "100"
    print(f"Значение: {value}, Тип: {type(value)}")

    if isinstance(value, str):
        # Конвертация строки в целое число
        converted_value = int(value)
        print(f"После конвертации: {converted_value}, Тип: {type(converted_value)}")

if __name__ == "__main__":
    practice_iteration_and_types()