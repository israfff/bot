import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('db.db')
    return __connection

# Новый пользователь
def new_user(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
    conn.commit()

# Проверка на заход
def checking_to_info(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT check_on FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Верификация
def verif(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET check_on=check_on+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Достаём баланс
def get_balance(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT balance FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Всего просмотров
def get_prosmotry(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT prosmotry FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Добавляем просмотр
def add_prosmotry(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET prosmotry=prosmotry+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем общий просмотр
def add_other_prosmotry(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET all_watching=all_watching+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Достаём общий просмотры
def get_all_waches(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT all_watching FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Достаём все комменты
def get_all_comments(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT all_comments FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Достаём всех рефералов
def get_all_referals(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT referals FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Добавляем 10 рублей
def add_many(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance+10 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем 500 рублей
def add_more_many(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance+500 WHERE user_id=(?)', (user_id,))
    conn.commit()

# достаём бонус
def get_bonuses(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT get_bonus FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# обновляем достаём бонус
def update_get_bonuses(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET get_bonus=get_bonus+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем 50 рублей
def add_50_rub(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance+50 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем реферала
def add_user_referal(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET referals=referals+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Отбавляем баланс
def minus_balance(count: int, user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance-(?) WHERE user_id=(?)', (count, user_id))
    conn.commit()

# Достаём комменты
def get_comments(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT comments FROM users WHERE user_id=(?)', (user_id,))
    return c.fetchone()

# Добавляем 20 рублей
def add_many_20(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance=balance+20 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем коммент
def add_comments(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET comments=comments+1 WHERE user_id=(?)', (user_id,))
    conn.commit()

# Добавляем общий коммент
def add_other_comments(user_id: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET all_comments=all_comments+1 WHERE user_id=(?)', (user_id,))
    conn.commit()
