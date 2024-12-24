import sqlite3


def connect():
    conn = sqlite3.connect('card.s3db')
    conn.execute("""CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0);""")
    return conn


def select_card(conn, card_number):
    with conn:
        card = conn.execute(f"""SELECT * FROM card WHERE number = :number""",
                        {'number': card_number}).fetchone()
    return card


def insert_card(conn, new_account):
    with conn:
        conn.execute("INSERT INTO card (number, pin, balance) VALUES (:number, :pin, :balance)",
                     {'number': new_account.card_number, 'pin': new_account.pin, 'balance': new_account.balance})


def update_balance(conn, which_account):
    with conn:
        conn.execute("UPDATE card SET balance = :balance WHERE id = :id",
                     {'balance': which_account.balance, 'id': which_account.identification})


def delete_account(conn, which_account):
    with conn:
        conn.execute("DELETE FROM card WHERE id = :id", {'id': which_account.identification})


def close(self):
    self.conn.close()
