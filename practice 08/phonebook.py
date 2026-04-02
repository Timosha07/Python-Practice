import psycopg2
from config import params

def main():
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        
        print("--- Поиск 'John' ---")
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", ('John',))
        for row in cur.fetchall():
            print(row)

        
        print(" Добавление contact")
        cur.execute("CALL upsert_contact(%s, %s);", ('Alice', '87771112233'))
        
       
        print("\n--- Удаление контакта ---")
        cur.execute("CALL delete_contact(%s);", ('Alice',))


        print("\n--- Пагинация (Limit 5, Offset 0) ---")
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (5, 0))
        for row in cur.fetchall():
            print(row)

        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()