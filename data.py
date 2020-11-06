from tkinter import *
import mysql.connector
import os
root =Tk()
root.geometry("400x600")

#connect to mysql
mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password = 'gughanguhan123@',
    database = "datascience",
    auth_plugin='mysql_native_password')

#checking connection
#print(mydb)

#creating cursor
my_cursor = mydb.cursor()

#create database
#my_cursor.execute("CREATE DATABASE datascience ")


# Test
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor :
    #print(db)

# Createing my table :
#my_cursor.execute("CREATE TABLE cult(username VARCHAR(255),password VARCHAR(255))")

frame1 = LabelFrame(root,text='',bg='gold')
frame1.pack(padx=15,pady=15)

login_frame = LabelFrame(frame1,text='login')
login_frame.pack(padx=5,pady=5)

user_label = Label(login_frame,text='user_name:',fg='green')
user_label.grid(row=0,column=0,sticky=W)

password_label = Label(login_frame,text='Password:',fg='green')
password_label.grid(row=1,column=0,sticky=W)



user = Entry(login_frame,width=40,borderwidth=5)
user.grid(row=0,column=1,padx=5,pady=5)

password = Entry(login_frame,width=40,borderwidth=5)
password.grid(row=1,column=1,padx=5,pady=5)



def login():
    mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password = 'gughanguhan123@',
    database = "datascience",
    )
    


    my_cursor = mydb.cursor()

    v = user.get()
    w = password.get()
    sql = "INSERT INTO cult(username, password) VALUES (%s, %s)"
    val = (v, w)
    my_cursor.execute(sql, val)


    print("1 record inserted, ID:", my_cursor.lastrowid)
    print(my_cursor.rowcount, "was inserted.")
    mydb.commit()
    import os
    command = 'client.py'
    os.system(command)
    

def query():
    
    mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password = 'gughanguhan123@',
    database = "datascience",
    )
    


    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM cult")
    records = my_cursor.fetchall()
    print(records)
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    querry_label = Label(root,text=print_records)
    querry_label.pack()



def delete():
    

     mydb = mysql.connector.connect(
     host= 'localhost',
     user= 'root',
     password = 'gughanguhan123@',
     database = "datascience",
     )
     c = mydb.cursor()
     c.execute('DELETE FROM cult',);

     print('We have deleted', c.rowcount, 'records from the table.')

        #commit the changes to db			
     mydb.commit()
        #close the connection
     mydb.close()



    

login_button = Button(login_frame,text='LOGIN',command=login)
login_button.grid(row=2,column=0,columnspan=3)

show_button = Button(login_frame,text='SHOW',command=query)
show_button.grid(row=3,column=0,columnspan=3)

delete_button = Button(login_frame,text='DELETE',command=delete)
delete_button.grid(row=4,column=0,columnspan=3)

root.mainloop()
    
root.mainloop()
