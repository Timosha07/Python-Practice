import csv
from connect import connect

def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        contact_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
    );
    """
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    finally:
        conn.close()

def insert_from_csv(file_path):
    conn = connect()
    try:
        with conn.cursor() as cur:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader) 
                for row in reader:
                    cur.execute("INSERT INTO contacts (first_name, phone_number) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            print("Данные из CSV загруженылер.")
    finally:
        conn.close()

def add_contact(name, phone):
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO contacts (first_name, phone_number) VALUES (%s, %s)", (name, phone))
            conn.commit()
            print(f"Контакт {name} добавлендер.")
    finally:
        conn.close()

def update_contact(name, new_phone=None, new_name=None):
    conn = connect()
    try:
        with conn.cursor() as cur:
            if new_phone:
                cur.execute("UPDATE contacts SET phone_number = %s WHERE first_name = %s", (new_phone, name))
            if new_name:
                cur.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (new_name, name))
            conn.commit()
            print("Контакт обновлендер.")
    finally:
        conn.close()

def query_contacts(filter_val):
    conn = connect()
    try:
        with conn.cursor() as cur:
            # Поиск по имени or по началу номера
            cur.execute("SELECT * FROM contacts WHERE first_name LIKE %s OR phone_number LIKE %s", 
                        (f'%{filter_val}%', f'{filter_val}%'))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    finally:
        conn.close()

def delete_contact(identifier):
    conn = connect()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM contacts WHERE first_name = %s OR phone_number = %s", (identifier, identifier))
            conn.commit()
            print("Контакт удален.")
    finally:
        conn.close()

if __name__ == '__main__':
    create_table()
    
    print("--- 1. Импорт из CSV ---")
    insert_from_csv('contacts.csv')
    
    print("\n--- 2. Ввод из консоли ---")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    add_contact(name, phone)
    
    print("\n--- 3. Поиск по фильтру (8701) ---")
    query_contacts('8701')
    
    print("\n--- 4. Обновление контакта ---")
    update_contact('Ivan', new_phone='80000000000')
    
    print("\n--- 5. Удаление контакта ---")
    delete_contact('Maria')
    
    print("\npgAdmin.")