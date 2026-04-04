# phonebook.py
from connect import get_connection

def search_contacts(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_records(%s);", (pattern,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def upsert_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def batch_insert(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM batch_insert_users(%s, %s);", (names, phones))
    errors = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return errors

def get_paged(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def delete_contact(target):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_record(%s);", (target,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n--- МЕНЮ ТЕЛЕФОННОЙ КНИГИ ---")
        print("1. Добавить/Обновить контакт")
        print("2. Поиск (по имени/номеру)")
        print("3. Показать список (пагинация)")
        print("4. Удалить контакт")
        print("5. Выход")
        
        choice = input("\nВыбери действие (1-5): ")

        if choice == '1':
            name = input("Введите имя: ")
            phone = input("Введите номер: ")
            upsert_contact(name, phone)
            print(f"Готово! {name} в базе.")

        elif choice == '2':
            pattern = input("Что ищем? (часть имени или номера): ")
            results = search_contacts(pattern)
            print("\nРезультаты поиска:")
            for r in results:
                print(f"ID: {r[0]} | Имя: {r[1]} | Тел: {r[3]}")

        elif choice == '3':
            lim = int(input("Сколько записей показать? "))
            off = int(input("Сколько пропустить? "))
            results = get_paged(lim, off)
            print(f"\nСтраница (limit {lim}):")
            for r in results:
                print(f"ID: {r[0]} | Имя: {r[1]} | Тел: {r[3]}")

        elif choice == '4':
            target = input("Введите имя или номер для удаления: ")
            delete_contact(target)
            print(f"Запись '{target}' удалена (если она была).")

        elif choice == '5':
            print("Пока!")
            break

        else:
            print("Не тупи, выбери от 1 до 5.")