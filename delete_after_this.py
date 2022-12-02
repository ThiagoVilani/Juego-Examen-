import sqlite3

def read_order_desc(db_name, field):
    with sqlite3.connect("{0}.db".format(db_name)) as connection:
        cursor = connection.cursor()
        sentence = f"SELECT * FROM ranking"
        cursor.execute(sentence)
        data = cursor.fetchall()
        connection.commit()
        return data



lista = read_order_desc("all_score", "score")
print(lista)