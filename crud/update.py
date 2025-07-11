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

def update_user(id,firstname,lastname,mobileno):
    try:
        query = "UPDATE friend SET firstname=%s, lastname=%s, mobileno=%s WHERE id=%s"
        values = (firstname,lastname, mobileno,id)
        cursor.execute(query,values)
        connection.commit()
        print("Record updated successfully")
    except mysql.connector.Error as err:
        print(f"Error : {err}")
id = int(input("Enter ID: "))
first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")
mobileno = input("Enter Mobile Number: ")       
update_user(id,first_name,last_name,mobileno)