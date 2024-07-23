import sys
import mysql.connector

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
    if len(sys.argv) < 2:
        print("Usage: python SQL-new.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "INSERT":
        if len(sys.argv) != 8:
            print("Usage: python SQL-new.py INSERT <shop_name> <category_id> <lunch_price> <dinner_price> <access> <thumbnail_path>")
            sys.exit(1)
        shop_name = sys.argv[2]
        category_id = sys.argv[3]
        lunch_price = sys.argv[4]
        dinner_price = sys.argv[5]
        access = sys.argv[6]
        thumbnail_path = sys.argv[7]
        query = f"INSERT INTO favoreat (shop_name, category_id, lunch_price, dinner_price, access, thumbnail_path) VALUES ('{shop_name}', '{category_id}', '{lunch_price}', '{dinner_price}', '{access}', '{thumbnail_path}')"

    elif command == "SELECT":
        query = "SELECT * FROM favoreat"

    elif command == "UPDATE":
        if len(sys.argv) != 5:
            print("Usage: python SQL-new.py UPDATE <target_name> <column_name> <new_value>")
            sys.exit(1)
        target_name = sys.argv[2]
        column_name = sys.argv[3]
        new_value = sys.argv[4]
        query = f"UPDATE favoreat SET {column_name} = '{new_value}' WHERE shop_name = '{target_name}'"

    elif command == "DELETE":
        if len(sys.argv) != 3:
            print("Usage: python SQL-new.py DELETE <shop_name>")
            sys.exit(1)
        shop_name = sys.argv[2]
        query = f"DELETE FROM favoreat WHERE shop_name = '{shop_name}'"

    else:
        print("Invalid command")
        sys.exit(1)

    conn = connect_to_database()
    cursor = conn.cursor()
    execute_query(conn, cursor, query)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

# INSERTの場合
# python SQL-new.py INSERT "江戸前うなぎ店" "1" "1000" "2000" "access1" "path/to/thumbnail"

# SELECTの場合
# python SQL-new.py SELECT

# UPDATEの場合
# python SQL-new.py UPDATE "江戸前うなぎ店" "lunch_price" "1500"

# DELETEの場合
# python SQL-new.py DELETE "江戸前うなぎ店"

