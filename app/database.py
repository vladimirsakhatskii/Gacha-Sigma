import sqlite3

# import mysql.connector

# config = {
#     'user': 'your_username',
#     'password': 'your_password',
#     'host': 'localhost',
#     'database': 'users_transactions_db',
# }

conn = sqlite3.connect("sigma.sqlite")
c = conn.cursor()


def create_table():
    # Создаем таблицы, если они еще не существуют
    c.execute("""CREATE TABLE IF NOT Enew_coinsXISTS Users
                 (UserID INTEGER PRIMARY KEY,
                  Coins INTEGER  NOT NULL,
                  CountPlay INTEGER NOT NULL
                  )
                  """)

    c.execute("""CREATE TABLE IF NOT EXISTS Transactions
                 (TransactionID INTEGER PRIMARY KEY,
                  SenderID INTEGER NOT NULL,
                  IsConfirmed BOOLEAN NOT NULL,
                  FOREIGN KEY(SenderID) REFERENCES Users(UserID))
                  """)

    # Сохраняем изменения
    conn.commit()


def add_user(user_id: int, coins: int = 0) -> str:
    try:
        c.execute("SELECT * FROM Users WHERE UserID =?", (user_id,))
        current_user = c.fetchone()
        if current_user is not None:
            return "пользователь уже существует"
        c.execute("INSERT OR IGNORE INTO Users (UserID, Coins, CountPlay) VALUES (?, ?, ?)", (user_id, 0, 0))
        conn.commit()

        return "успешно добавлен"
    except Exception as e:
        return "что то пошло не так"


def add_transaction(sender_id, transaction_id: int) -> str:
    c.execute("INSERT OR IGNORE INTO Transactions (TransactionID, SenderID, IsConfirmed) VALUES (?, ?, ?)",
              (transaction_id, sender_id, 0,))
    conn.commit()

    return "транзакция добавлена"


"""Пополнение баланса пользователя после подтверждения."""
def confirm_transaction(transaction_id, new_coins):
    # TODO: нужно сделать так, чтобы админ отвечал на сообщение и вызывался этот метод для пополнения баланса
    c.execute("UPDATE Transactions SET IsConfirmed = TRUE WHERE TransactionID = ?", (transaction_id,))
    current_coins, user_id = get_coins(transaction_id)
    # TODO: тут точно нихера не работает
    new_coins_value = current_coins + new_coins
    c.execute("UPDATE Users SET Coins = ? WHERE UserID = ?", (new_coins_value, user_id,))

    conn.commit()

    return "транзакция подтверждения"


"""Возвращает юзера и его количество монет по айди транзакции"""
def get_coins(transaction_id):
    c.execute("SELECT SenderID FROM Transactions WHERE TransactionID = ?", (transaction_id,))
    result = c.fetchone()
    user_id = result[0]

    c.execute("SELECT Coins FROM Users WHERE UserID = ?", (user_id,))
    result = c.fetchone()
    if result:
        return result[0], user_id  # Возвращаем значение Coins, если пользователь найден
    else:
        return None


def increment_user_play_count(user_id: int):
    c.execute("SELECT (user_id) FROM Users", user_id)
    value = c.fetchall()

    return value


def user_play():
    pass
