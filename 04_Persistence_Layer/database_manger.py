import sqlite3

DB_NAME = "conroe_water_grid.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME) # This is the "phone call". Your active connection between the db and the python script.
    cursor = conn.cursor() # this is the hand the moves to specific spot to read or write data. Use it to run commands.
    # We store: Unique ID, Time, The Sensor Topic, and the Pressure Value
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            topic TEXT,
            payload REAL
        )
    ''')
    # The execute is the send button. It says "ah, run this sql in the db."
    conn.commit() # The save button.  Changes are not offically added until you commit them.
    conn.close() # End the "phone call". 
    print(f"Historian Initialized: {DB_NAME}")

if __name__ == "__main__":
    initialize_database()