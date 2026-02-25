import sqlite3 as sql
from model_optimizer import WakeUpModel, GrabFromInternet

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

# i need to optimize this part later !
def Listing(words, definitions):
    conn = sql.connect("Storage.db")
    c = conn.cursor()
    
    if words and definitions:
        result = c.execute(""" SELECT word, definition FROM VAULT """).fetchall()
        return "\n\n".join([f"**{row[0]}** — {row[1]}" for row in result])
    
    elif words and not definitions:
        result = c.execute(""" SELECT word FROM VAULT """).fetchall()
        return "\n\n".join([f"• {row[0]}" for row in result])
    
    elif not words and definitions:
        result = c.execute(""" SELECT definition FROM VAULT """).fetchall()
        return "\n\n".join([f"• {row[0]}" for row in result])
    
    else:
        total = c.execute(""" SELECT COUNT(*) FROM VAULT """).fetchall()[0]
        return f"Vault Stats\n\nTotal words: <b> {total[0]} </b>"

def DeletingWord(word):
    conn = sql.connect("Storage.db")
    c = conn.cursor()
    
    exists = c.execute(f"SELECT word FROM VAULT WHERE word = '{word}'").fetchone()
    
    if exists:
        c.execute(f"DELETE FROM VAULT WHERE word = '{word}'")
        conn.commit()
        return f"**{word}** has been deleted from your vault."
    else:
        return f"**{word}** was not found in your vault."

def GrabingTheMeaning(word, command, ai_usage):
    conn = sql.connect("Storage.db")
    c = conn.cursor()
    definition = c.execute(f""" SELECT definition from VAULT WHERE word = '{word}'; """).fetchone()
    
    if definition is None and command == "add":
        if ai_usage == True:
            meaning = WakeUpModel(word)
        else:
            meaning = GrabFromInternet(word)
        
        ans = AddingNewOne(word, meaning)
        return ans
    
    elif definition is None and command == "meaning":
        if ai_usage == True:
            meaning = WakeUpModel(word)
        else:
            meaning = GrabFromInternet(word)
        return f"You never searched for '{word}' before. Use .add '{word}' to add it to your vault.\n But the meaning is: <span style='color: #FCFC4E;'>{meaning}</span>"
    else:
        return definition[0]
