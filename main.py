import sqlite3
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Фільми (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Назва TEXT,
        Режисер TEXT,
        Рік_випуску INTEGER,
        Бюджет REAL,
        Оцінка REAL
    )
''')

data = [
    ('Барбі', 'Ґрета Ґервіґ', 2023, 145.0, 3.0),
    ('Загублене місто', 'Аарон Ні, Адам Ні', 2022, 68.0, 3.3),
    ('Шпіон', 'Пол Фіг', 2015, 65.0, 4.4),
    ('Аладін', 'Гай Річі', 2019, 183.0, 4.0),
    ('Пірати Карибського моря: Прокляття Чорної перлини', 'Гор Вербінскі', 2003, 140.0, 4.5)
]
cursor.executemany('INSERT INTO Фільми (Назва, Режисер, Рік_випуску, Бюджет, Оцінка) VALUES (?,?,?,?,?)', data)
conn.commit()

cursor.execute('SELECT * FROM Фільми')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('SELECT * FROM Фільми WHERE Оцінка >= 4.0')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('UPDATE Фільми SET Оцінка = 4.7 WHERE Назва = ?', ('Аладін',))
conn.commit()

cursor.execute('SELECT * FROM Фільми')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('SELECT * FROM Фільми WHERE Оцінка >= 4.0')
result = cursor.fetchall()
for row in result:
    print(row)

