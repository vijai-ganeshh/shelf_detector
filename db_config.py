import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ganeshh@1234',
    'database': 'shelf_detector_db'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    cursor.close()
    conn.close()

def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records