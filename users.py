from admins import logout
import db_connection

cur = db_connection.db.cursor()

def user_panel():
    print("\nAdmin Panel")
    print("===========\n")
    print('''
    1. View Item
    2. Order Item
    3. Check Cart
    4. User Profile
    5. Logout
    ''')
    inp = int(input())
    if inp == 1:
        view_items()
    elif inp == 2:
        order_item()
    elif inp == 3:
        cart()
    elif inp == 4:
        user_profile()
    elif inp == 5:
        logout()
    else:
        print("Wrong choice!")

def view_items():
    print("---PRODUCT SECTION---")
    query = f"select product_id, product_name, product_price FROM products"
    cur.execute(query)
    products = cur.fetchall()
    
    print(products)

    if products == []:
        print("No product found.")
    # print(product)
    else:
        count = 1
        for n in products:
            print("Product No:-", count)
            print("Product id:", (n[0]))
            print("Product name:", (n[1]))
            print("Product price:", (n[2]))
            print("---------")
            count +=1

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        user_panel()
    else:
        pass

def order_item():
    print('''
    Enter 1 to buy a item
    Enter 2 to go back.
    ''')
    inp = int(input())
    if inp == 1:
        product_id = int(input("Enter id of product you want to buy: "))
        user_id = int(input("Enter your user id: "))
        order_address = input("Enter your address: ")
        # query1 = f"UPDATE products SET product_sales = product_sales + 1 (WHERE product_id = {product_id})"
        query1 = f"UPDATE products SET product_sales = product_sales + 1 WHERE products.product_id = {product_id};"
        cur.execute(query1)

        query2 = f"SELECT product_price from products where products.product_id = {product_id} ;"
        cur.execute(query2)
        order_amt = cur.fetchone()
        query3 = "INSERT INTO orders(product_id, user_id, order_amt, order_address) VALUES (%s, %s, %s, %s)"
        args3 = (product_id, user_id, order_amt[0], order_address)
        cur.execute(query3,args3)
        db_connection.db.commit()
        print("You ordered item successfully.")

    elif inp == 2:
        user_panel()
    else:
        print("Wrong Choice.")

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        user_panel()
    else:
        pass

def cart():
    print("---CART SECTION---")
    user_id = int(input("Enter your user id: "))
    cur.execute(f"SELECT * from orders where user_id = {user_id}")
    order_details = cur.fetchall()
    print("Your cart items:\n")
    order_amt = 0
    for order in order_details:
        print("Product id:", order[1])
        cur.execute(f"SELECT product_name from products where products.product_id = {order[1]}")
        product_name = cur.fetchone()
        print("Product name:", product_name[0])
        order_amt += order[4]
    print("\nCart Total Amount:",order_amt)

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        user_panel()
    else:
        pass

def user_profile():
    user_id = int(input("Enter the user id of customer: "))
    print("---Your Profile---")
    query = f"select * FROM user_registration WHERE (user_id = {user_id})"
    cur.execute(query)
    user = cur.fetchmany()
    # print(user)
    
    if user == []:
        print("No user found with this user id.")
    else:
        print("Id:", user[0][0])
        print("First Name:", user[0][1])
        print("Last Name:", user[0][2])
        print("Phone number:", user[0][3])
        print("Address:", user[0][4])
        print("Email:", user[0][5])
        print("Registration date:", user[0][7])
    
    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        user_panel()
    else:
        pass

    
def logout():
    print("You are successfully Logged out!")


# user_panel()
# user_profile()
# cart()
# order_item()
# view_items()