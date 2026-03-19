# read_files.py
filename = "data.txt"

def read_and_print():
    try:
        # 2. Читаем и выводим контент
        with open(filename, "r", encoding="utf-8") as f:
            print("--- Содержимое файла ---")
            print(f.read())
            print("------------------------")
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден. Сначала запусти write_files.py")

if __name__ == "__main__":
    read_and_print()