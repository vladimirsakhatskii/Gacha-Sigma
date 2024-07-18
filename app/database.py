import mysql.connector

config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'users_transactions_db',
}

conn = mysql.connector.connect(**config)
c = conn.cursor()


def create_table():
    # Создаем таблицы, если они еще не существуют
    c.execute("""CREATE TABLE IF NOT EXISTS Users
                 (UserID INT PRIMARY KEY,
                  Coins INT  NOT NULL,
                  CountPlay INT NOT NULL,
                  )
                  """)

    c.execute("""CREATE TABLE IF NOT EXISTS Transactions
                 (TransactionID INT PRIMARY KEY,
                  SenderID INT NOT NULL,
                  IsConfirmed BOOLEAN NOT NULL,
                  FOREIGN KEY(SenderID) REFERENCES Users(UserID),
                  FOREIGN KEY(ReceiverID) REFERENCES Users(UserID))""")

    # Сохраняем изменения
    conn.commit()


def add_user(user_id, coins=0) -> str:
    c.execute("SELECT (user_id) FROM Users", user_id)
    current_user = c.fetchall()
    if current_user is not None:
        return "пользователь уже существует"

    c.execute("INSERT INTO Users (UserID, Coins, CountPlay) VALUES (%s, %s, %s)", (user_id, coins, 0))
    conn.commit()

    return "успешно добавлен"


def add_transaction(sender_id):
    c.execute("INSERT INTO Transactions (SenderID, IsConfirmed) VALUES (?, ?)",
              (sender_id, 0))
    conn.commit()

    return "транзакция добавлена"


def confirm_transaction(transaction_id, new_coins):
    c.execute("UPDATE Transactions SET IsConfirmed = TRUE WHERE TransactionID = %s", (transaction_id,))
    current_coins = get_coins(transaction_id)
    # TODO: тут точно нихера не работает
    new_coins_value = current_coins + amount
    cursor.execute("UPDATE Users SET Coins = %s WHERE UserID = %s", (new_coins_value, user_id))

    conn.commit()

    return "транзакция подтверждения"


def get_coins(transaction_id):
    cursor.execute("SELECT SenderID FROM Transactions WHERE TransactionID = %s", (transaction_id,))
    result = cursor.fetchone()
    user_id = result[0]

    cursor.execute("SELECT Coins FROM Users WHERE UserID = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Возвращаем значение Coins, если пользователь найден
    else:
        return None


def increment_user_play_count(user_id: int):
    c.execute("SELECT (user_id) FROM Users", user_id)
    value = c.fetchall()

    return value


def user_play():
    pass
