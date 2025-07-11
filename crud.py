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



#create  insert operation
def insert_data():
    id = int(input("Enter ID: "))
    first_name = input("Enter FirstName: ")
    last_name = input("Enter LastName: ")
    mobileno = input("Enter Mobile Number: ")
    try:
        query = "INSERT INTO friend ( id, firstname, lastname, mobileno) VALUES (%s, %s, %s, %s)"
        values = (id, first_name, last_name, mobileno)
        cursor.execute(query,values)
        connection.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error : {err}")
        
insert_data()

# cursor.close()
# connection.close()

# #read(select ) operation
# def read_user():
#     try:
#         query = "SELECT * FROM friend"
#         cursor.execute(query)
#         friends = cursor.fetchall()
#         for friend in friends:
#             print(friend)
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
def read_user():
    try:
        query = "SELECT * FROM friend"
        cursor.execute(query)
        friends = cursor.fetchall()
        for friend in friends:
            print(friend)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
read_user()

cursor.close()
connection.close()
# read_user()
# #delete
# cursor = connection.cursor()

# def delete_user():
#     try:
#         query = "DElETE FROM friend WHERE id = %s"
#         values = (id,)
#         cursor.execute(query,values)
#         connection.commit()
#         print("Record deleted successfully")
#     except mysql.connector.Error as err:
#         print(f"Error : {err}")

# delete_user()  
# # update
# def update_user(id,firstname,lastname,mobileno):
#     try:
#         query = "UPDATE  friend SET firstname=%s, lastname=%s, mobileno=%s WHERE id=%s"
#         values = (firstname,lastname, mobileno,id)
#         cursor.execute(query,values)
#         connection.commit()
#         print("Record updated successfully")
#     except mysql.connector.Error as err:
#         print(f"Error : {err}")
        
# update_user()