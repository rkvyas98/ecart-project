from users import user_panel
from admins import admin_panel
import db_connection
# import admins

cur = db_connection.db.cursor()

# =====Starting of Program Execution!=====
cur_user = None

def prog_execution():
    print("\nWelcome to the Ecart!")
    print("=======================\n\n")
    print("Enter 1 if you are already a user.\nOr if you are a new user enter 2 to register yourself.\n")
    user_auth = int(input())

    if user_auth == 1:
        print("You are going to login section.")
        login_func()

    elif user_auth == 2:
        print("You are going to registration section.")
        print('''How do you want to register?\n
        1. Enter 1 to register as a Admin
        2. Enter 2 to register as a user
        ''')
        reg_inp = int(input())
        if reg_inp == 1:
            insert_admin()
        elif reg_inp == 2:
            insert_user()
        else:
            print("Wrong choice!")
             
    else:
        print("Wrong choice!")



def login_func():
    username = input("Enter your email for Login: ")
    user_type = input("Enter 'a' for admin login and 'u' for user login: ")
    pass1 = input("Enter your password: ")
    cur.execute("select email from login where email = %s AND user_type = %s AND pass1 = %s",(username,user_type,pass1))
    user = cur.fetchone()
    if user == None:
        print("No user found. Please Register yourself.")
    elif username == user[0]:
        print("You Are successFully Logged In as: ",username)
        if user_type == 'a':
            admin_panel()
        if user_type == 'u':
            user_panel()

def insert_admin():
    fname = input("Enter your First Name: ")
    lname = input("Enter your Last Name: ")
    contact_no = input("Enter your Contact Number: ")
    address = input("Enter your Address: ")
    email = input("Enter your Email: ")
    pass1 = input("Enter the password: ")

    query = "INSERT INTO admin_registration (fname, lname, contact_no, address, email, pass1) VALUES (%s,%s,%s,%s,%s,%s)"
    args = (fname,lname,contact_no,address,email,pass1)
    cur.execute(query, args)

    # Inserting in login table
    cur.execute("INSERT INTO login (email, pass1, user_type) VALUES (%s, %s, 'a')",(email, pass1))
    
    db_connection.db.commit()
    print("\nYou are successfully Registered!\nNow you can Login")
    inp = int(input("\nDo you want to login now?\nEnter 1 to login now otherwise enter 2: "))
    if inp == 1:
        login_func()
    else:
        pass


def insert_user():
    fname = input("Enter your First Name: ")
    lname = input("Enter your Last Name: ")
    contact_no = input("Enter your Contact Number: ")
    address = input("Enter your Address: ")
    email = input("Enter your Email: ")
    pass1 = input("Enter the password: ")

    query = "INSERT INTO user_registration (fname, lname, contact_no, address, email, pass1) VALUES (%s,%s,%s,%s,%s,%s)"
    args = (fname,lname,contact_no,address,email,pass1)
    cur.execute(query, args)

    # Inserting in login table
    cur.execute("INSERT INTO login (email, pass1, user_type) VALUES (%s, %s, 'u')",(email, pass1))

    db_connection.db.commit()
    print("\nYou are successfully Registered!\nNow you can Login")
    inp = int(input("\nDo you want to login now?\nEnter 1 to login now otherwise enter 2: "))
    if inp == 1:
        login_func()
    else:
        pass


prog_execution()

# admins.add_item()


# insert_admin()
# insert_user()

