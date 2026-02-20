import sqlite3 as sql
from model_optimizer import WakeUpModel

# Create connections =>
conn = sql.connect("Storage.db")
c = conn.cursor()

# Creating the table for words and their definnitions =>
c.execute(""" CREATE TABLE IF NOT EXISTS VAULT(
            word_id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT VARCHAR(30) UNIQUE, definition TEXT) """)

c.execute(""" CREATE TABLE IF NOT EXISTS examples(
            example_id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_id INTEGER NOT NULL, sentence TEXT NOT NULL,
            FOREIGN KEY (word_id) REFERENCES VAULT(word_id) ON DELETE CASCADE) """)

def AddingNewOne(word, definition):
    conn = sql.connect("Storage.db")
    c = conn.cursor()
    try:
        c.execute(""" INSERT INTO VAULT(word, definition) VALUES("{}", "{}"); """.format(word, definition))
        conn.commit()
        return definition
    except Exception as e:
        return f"this is the error we are getting: \n {e}"


def GrabingTheMeaning(word, command):
    conn = sql.connect("Storage.db")
    c = conn.cursor()
    definition = c.execute(f""" SELECT definition from VAULT WHERE word = '{word}'; """).fetchone()
    
    if definition is None and command == "add":
        meaning = WakeUpModel(word)
        ans = AddingNewOne(word, meaning)
        return ans
    
    elif definition is None and command == "meaning":
        meaning = WakeUpModel(word)
        return f"You never searched for '{word}' before. Use .add '{word}' to add it to your vault.\n But the meaning is: {meaning}"
    else:
        return definition[0]
