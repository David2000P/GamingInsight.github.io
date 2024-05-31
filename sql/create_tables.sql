import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('quiz.db')

# Einen Cursor erstellen
c = conn.cursor()

# Eine Tabelle erstellen
c.execute('''CREATE TABLE IF NOT EXISTS quiz
             (id INTEGER PRIMARY KEY, frage TEXT, antwort TEXT)''')

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()
