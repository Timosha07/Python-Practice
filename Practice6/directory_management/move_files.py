import os
import shutil

def move_and_copy():
    # Создаем папки для демонстрации если их нет
    os.makedirs("folder_A", exist_ok=True)
    os.makedirs("folder_B", exist_ok=True)

    # Создаем файл в folder_A
    source_file = "folder_A/move_me.txt"
    with open(source_file, "w") as f:
        f.write("I'm moving between folders.")

    # 4. Move/copy files between directories
    destination = "folder_B/moved_file.txt"
    
    # Безопасное перемещение
    if os.path.exists(source_file):
        shutil.move(source_file, destination)
        print(f"файл перемещен из folder_A в folder_B")
    else:
        print(" Файл для перемещения не найден.")

if __name__ == "__main__":
    move_and_copy()