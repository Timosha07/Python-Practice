# write_files.py
filename = "data.txt"

def write_and_append():
    # 1. Создаем файл и пишем данные
    content = "I like Kanye West\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Файл {filename} создан.")

    # 3. Дописываем новые строки
    with open(filename, "a", encoding="utf-8") as f:
        f.write("New line appended: Graduation is a classic album.\n")
    print("✅ Новые данные добавлены.")

if __name__ == "__main__":
    write_and_append()