import sqlite3


def register(username, chat_id):
    username = '@' + username

    con = sqlite3.connect('identifier.sqlite')
    cur = con.cursor()

    check_request = f"SELECT * FROM users WHERE username = '{username}';"
    if not cur.execute(check_request).fetchall():
        print('not found')
        insert_request = f"INSERT INTO users(username, chat_id) VALUES('{username}', '{chat_id}');"
        cur.execute(insert_request)
        con.commit()
        return True


def get_data_from_db(username):
    con = sqlite3.connect('identifier.sqlite')
    cur = con.cursor()

    request = f"SELECT * FROM users WHERE username = '{username}';"

    data = list(cur.execute(request).fetchall()[0])

    if data[3]:
        data[3] = data[3].split(', ')
    print(data)
    return data


if __name__ == '__main__':
    get_data_from_db('@albert_gareev')
