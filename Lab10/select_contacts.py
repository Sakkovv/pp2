import psycopg2
from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    # Определение функции load_config

def select_contacts():
    """ Выполнение запроса на извлечение всех контактов из таблицы """
    sql = "SELECT * FROM contacts;"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    contacts = select_contacts()
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("Нет данных в таблице 'контакты'")
