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

def delete_user(id):
    try:
        query = "DElETE FROM friend WHERE id = %s"
        values = (id,)
        cursor.execute(query,values)
        connection.commit()
        print("Record deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error : {err}")

id = int(input("Enter the ID you want tot delete: "))
delete_user(id)