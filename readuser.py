import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_mysql"
    )
    print("database connected to mysql successfully:")
except mysql.connector.Error as err:
    print(f"Error : {err}")
    exit()
    
cursor = connection.cursor()

#read(select ) operation
def read_user():
    try:
        query = "SELECT * FROM friend where id>1"
        cursor.execute(query)
        friends = cursor.fetchall()
        for friend in friends:
            print(friend)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
read_user()