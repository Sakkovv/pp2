import psycopg2
from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

def insert_contact(contact_name, contact_phone):
    """ Insert a new contact into the contacts table """

    sql = """INSERT INTO contacts(contact_name, contact_phone)
             VALUES(%s, %s) RETURNING contact_id;"""
    
    contact_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (contact_name, contact_phone))

                # get the generated id back                
                row = cur.fetchone()
                if row:
                    contact_id = row[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return contact_id

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS contacts (
            contact_id SERIAL PRIMARY KEY,
            contact_name VARCHAR(255) NOT NULL,
            contact_phone VARCHAR(20) NOT NULL
        )
        """,)
    try:
        config = load_config()

        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()

    # Вставка данных
    insert_contact("Zhumabek", "+8707774422")
