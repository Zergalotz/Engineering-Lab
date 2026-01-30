import sqlite3
# This reaches into your other file to get the database name
from database_manger import DB_NAME 

def read_telemetry():
    """Fetches and prints the last 10 logs from the database."""
    try:
        # 1. Connect to the 'Historian' file
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # 2. Ask for the data (SQL language)
        print(f"Reading from: {DB_NAME}...")
        cursor.execute("SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 10")
        rows = cursor.fetchall()
        
        # 3. Print the results
        print("\n--- [ CONROE WATER GRID: HISTORIAN DATA ] ---")
        if not rows:
            print("The database is empty. Send a message first!")
        else:
            for row in rows:
                # row[0]=ID, row[1]=Timestamp, row[2]=Topic, row[3]=Value
                print(f"ID: {row[0]} | Time: {row[1]} | {row[2]} | {row[3]} PSI")
            
        conn.close()
    except Exception as e:
        print(f"Audit failed: {e}")

if __name__ == "__main__":
    read_telemetry()