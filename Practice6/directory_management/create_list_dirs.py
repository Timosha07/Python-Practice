import os

def manage_directories():
    # 1. Create nested directories 
    nested_path = "parent_folder/child_folder/sub_folder"
    os.makedirs(nested_path, exist_ok=True)
    print(f"✅ Папки созданы: {nested_path}")

    # тест
    open("parent_folder/test1.txt", "a").close()
    open("parent_folder/test2.py", "a").close()

    # 2. List files and folders 
    print("\n--- Содержимое папки 'parent_folder' ---")
    content = os.listdir("parent_folder")
    print(content)

    # 3. Find files by extension 
    extension = ".txt"
    txt_files = [f for f in content if f.endswith(extension)]
    print(f"\n Файлы с расширением {extension}:")
    print(txt_files)

if __name__ == "__main__":
    manage_directories()