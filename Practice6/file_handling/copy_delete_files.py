# copy_delete_files.py
import os
import shutil

def copy_and_delete():
    original = "data.txt"
    backup = "data_backup.txt"


    if os.path.exists(original):
        shutil.copy(original, backup)
        print(f" Создана резервная копия: {backup}")
    else:
        print(" Оригинальный файл не найден.")
        return


    for f in [original, backup]:
        if os.path.exists(f):
            os.remove(f)
            print(f"Файл {f} безопасно удален.")

if __name__ == "__main__":
    copy_and_delete()