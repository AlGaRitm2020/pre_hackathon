import sqlite3


def get_data_from_db(username):
    con = sqlite3.connect('identifier.sqlite')
    cur = con.cursor()

    request = f"SELECT * FROM users WHERE username = '{username}';"

    data = list(cur.execute(request).fetchall()[0])
    data[3] = data[3].split(', ')
    print(data)
    return data


if __name__ == '__main__':
    get_data_from_db('@AlGaRitm2020')
