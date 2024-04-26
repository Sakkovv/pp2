import psycopg2
import csv
from config import host, user, password, db_name

try:
    #connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    
    #the cursor for perfoming database operations
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    
    
    
    #create a new table
    with connection.cursor() as cursor:
        # Удаление существующей таблицы (если она существует)
        cursor.execute("DROP TABLE IF EXISTS users;")
        
        # Создание новой таблицы
        cursor.execute("""
            CREATE TABLE users (
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                phone_number varchar(50) NOT NULL
            )
        """)
        print(f"[INFO] Table created successfully")
        



    #ВВОД ДАННЫХ В ТАБЛИЦУ
    #insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (name, phone_number) VALUES
    #         ('Zhumabek', '87072547241'),
    #         ('Zhumabeadasf', '8707254724444');"""
    #     )
    #     print(f"[INFO] Data was succesfully inserted")



    #Получения данных с таблицы
    #get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT * FROM users WHERE name = 'Zhumabek'"""
            
    #     )
    #     print(cursor.fetchone())
    #     cursor.execute(
    #         """SELECT * FROM users WHERE phone_number = '8707254744424'"""
    #     )
    #     print(cursor.fetchone())



    # РАБОТА С CSV-ФАЙЛОМ
    # Открываем CSV-файл для чтения


    # РАБОТА С CSV-ФАЙЛОМ
    with open('name_number.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            cursor.execute(
                "INSERT INTO users (name, phone_number) VALUES (%s, %s)",
                (row[0], row[1])
            )
        print("[INFO] Data was successfully inserted")




    #delete a table(УДАЛИТЬ ВСЮ ТАБЛИЦУ)
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #     print("[INFO] Table was deleted")

    # #УДАЛИТЬ ЗАПИСЬ ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE id = """
            
    #     )
    # #УДАЛИТЬ ЗАПИСЬ ПО ИМЕНИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE name = """
            
    #     )
    #УДАЛИТЬ ЗАПИСЬ ПО НОМЕРУ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM users WHERE phone_number = """
            
    #     )

    #ОБНОВИТЬ ИМЯ ПО НОМЕРУ ТЕЛЕФОНА
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET name = 'новое-имя' 
    #         WHERE phone_number = номер телефона """
            
    #     )
    # #ОБНОВИТЬ НОМЕР ТЕЛЕФОНА ПО ИМЕНИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET phone_number = 'новый-номер' 
    #         WHERE name = по имени"""
            
    #     )
    # #ОБНОВИТЬ ИМЯ ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET id = 'новое имя' 
    #         WHERE name = по номеру"""
            
    #     )
    # #ОБНОВИТЬ НОМЕР ТЕЛЕФОНА ПО АЙДИ
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """UPDATE users
    #         SET phone_number = 'новый-номер' 
    #         WHERE name = по имени"""
            
    #     )



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")