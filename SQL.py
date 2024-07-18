import sys
import mysql.connector
import argparse

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='favoreat'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

def execute_query(conn, cursor, query):
    try:
        cursor.execute(query)
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            conn.commit()
            print("Query executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Execute an SQL query on the database.")
    parser.add_argument("query", nargs='+', help="The SQL query to execute")
    
    args = parser.parse_args()
    query = ' '.join(args.query)
    
    conn = connect_to_database()
    cursor = conn.cursor()
    
    execute_query(conn, cursor, query)
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
