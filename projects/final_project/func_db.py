# Список функций для работы с базой данных через Python 

# вставка запсии
cur.execute(
    "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
    ("Иван Иванов", "ivan@example.com", 30)
)
conn.commit() #  Каждая операция изменения данных должна быть подтверждена через commit():

# массовая запись
users_data = [
    ("Анна Смирнова", "anna@example.com", 28),
    ("Максим Козлов", "maxim@example.com", 35),
    ("Елена Васильева", "elena@example.com", 24)
]

cur.executemany(
    "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
    users_data
)
conn.commit()

# получение данных

# Выполнение запроса
cur.execute("SELECT id, name, email FROM users LIMIT 10")

# fetchone() - получить одну строку
first_row = cur.fetchone()
print(first_row)  # (1, 'Иван', 'ivan@example.com')

# fetchmany(n) - получить n строк
cur.execute("SELECT id, name, email FROM users")
five_rows = cur.fetchmany(5)
for row in five_rows:
    print(row)

# fetchall() - получить все строки
cur.execute("SELECT id, name, email FROM users")
all_rows = cur.fetchall()
print(f"Всего строк: {len(all_rows)}")
