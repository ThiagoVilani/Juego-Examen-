import sqlite3

def create_db(db_name):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        connection.commit()
        print("creo base de datos")



def create_table(db_name):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """CREATE TABLE ranking (
                    name text,
                    score integer
                )
                """
            )
            connection.commit()
            print("creo la tabla")
        except:
            return "already exists"


def insert(db_name, name, score):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        sentence = f"INSERT INTO ranking VALUES ('{name}', {score})"
        cursor.execute(sentence)
        connection.commit()
        print("inserto")


def read_order_desc(db_name, field):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        sentence = f"SELECT * FROM ranking ORDER BY {field} DESC"
        cursor.execute(sentence)
        data = cursor.fetchall()
        connection.commit()
        return data


def search(db_name, name):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        sentence = f"SELECT * FROM ranking WHERE name= '{name}'"
        cursor.execute(sentence)
        data = cursor.fetchall()
        connection.commit()
        return data


def update(db_name, name, score):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        sentence = f"UPDATE ranking SET score={score} WHERE name='{name}'"
        cursor.execute(sentence)
        connection.commit()



def insert_data(db_name, name, score, field):
    create_db(db_name)
    create_table(db_name)
    result_search = search(db_name, name)
    if len(result_search) != 0:
        if result_search[0][1] < score:
            update(db_name, name, score)
    else:
        insert(db_name, name, score)
    read_order_desc(db_name, field)


