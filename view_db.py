import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 'message' tablosunu oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
''')

# Test verilerini ekle
cursor.execute("INSERT INTO message (content) VALUES ('Test Message 1')")
cursor.execute("INSERT INTO message (content) VALUES ('Test Message 2')")

# Değişiklikleri kaydet
conn.commit()

# Veritabanındaki 'message' tablosundaki tüm verileri seç
cursor.execute('SELECT * FROM message')
rows = cursor.fetchall()

# Tablodaki verileri ekrana yazdır
for row in rows:
    print(row)

# Bağlantıyı kapat
conn.close()
