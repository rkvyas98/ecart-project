import db_connection
# import home

cur = db_connection.db.cursor()


def admin_panel():
    print("\nAdmin Panel")
    print("===========\n")
    print('''
    1. Add Item
    2. Update Item
    3. Delete Item
    4. Total sale
    5. Customers Details
    6. Product summary
    7. Logout
    ''')
    inp = int(input())
    if inp == 1:
        add_item()
    elif inp == 2:
        update_item()
    elif inp == 3:
        delete_item()
    elif inp == 4:
        total_sales()
    elif inp == 5:
        customer_details()
    elif inp == 6:
        product_details()
    elif inp == 7:
        logout()
    else:
        print("Wrong choice!")


def add_item():
    print("---ADD ITEM SECTION---")
    product_name = input("Enter Product Name: ")
    product_price = int(input("Enter Product Price: "))
    product_cat = input("Enter Product category: ")
    product_desc = input("Description about the product: ")
    query = "INSERT INTO products(product_name, product_price, product_cat, product_desc) VALUES (%s, %s, %s, %s)"
    args = (product_name,product_price,product_cat,product_desc)
    cur.execute(query, args)

    db_connection.db.commit()

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass
    

def update_item():
    print("---UPDATE ITEM SECTION---")
    product_id = int(input("Enter the item product id you want to update: "))
    print('''
    1. Update Name
    2. Update Price
    3. Update category
    4. Update desc
    ''')
    inp = int(input())
    if inp == 1:
        product_name = input()
        cur.execute("UPDATE products SET product_name = %s WHERE product_id = %s ;", (product_name, product_id))
    elif inp == 2:
        product_price = int(input())
        cur.execute("UPDATE products SET product_price = %s WHERE product_id = %s ;", (product_price, product_id))
    elif inp == 3:
        product_cat = input()
        cur.execute("UPDATE products SET product_cat = %s WHERE product_id = %s ;", (product_cat, product_id))
    elif inp == 4:
        product_desc = input()
        cur.execute("UPDATE products SET product_desc = %s WHERE product_id = %s ;", (product_desc, product_id))
    else:
        print("Wrong choice.")

    db_connection.db.commit()
    print("Item updated successfully.")
    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass

def delete_item():
    print("---DELETE ITEM SECTION---")
    product_name = input("Enter Product Name: ")
    product_cat = input("Enter Product category: ")
    query = "DELETE FROM products where (product_name = %s AND product_cat = %s)"
    args = (product_name,product_cat)
    cur.execute(query, args)
    db_connection.db.commit()

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass


def total_sales():
    print("---TOTAL SALES OF ITEM SECTION---")
    product_name = input("Enter Product Name: ")
    product_cat = input("Enter Product category: ")
    query = "SELECT product_sales FROM products where (product_name = %s AND product_cat = %s)"
    args = (product_name,product_cat)
    cur.execute(query, args)
    sales = cur.fetchone()

    if sales == None:
        print("No product found with this name and category.")
    else:
        print(f"Number of sales for {product_name} is: ",sales[0])

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass

def customer_details():
    print("---CUSTOMER DETAIL SECTION---")
    user_id = int(input("Enter the user id of customer: "))
    query = f"select * FROM user_registration WHERE (user_id = {user_id})"
    cur.execute(query)
    user = cur.fetchmany()
    print(user)
    
    if user == []:
        print("No user found with this user id.")
    else:
        print("Customer's Id:", user[0][0])
        print("Customer's First Name:", user[0][1])
        print("Customer's Last Name:", user[0][2])
        print("Customer's Phone number:", user[0][3])
        print("Customer's Address:", user[0][4])
        print("Customer's Email:", user[0][5])
        print("Customer's Registration date:", user[0][7])

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass


def product_details():
    print("---PRODUCT DETAIL SECTION---")
    product_id = int(input("Enter the Product id: "))
    query = f"select * FROM products WHERE (product_id = {product_id})"
    cur.execute(query)
    product = cur.fetchmany()
    
    if product == []:
        print("No product found with this Product id.")
    # print(product)
    else:
        print("Product Id:", product[0][0])
        print("Product name:", product[0][1])
        print("Product price:", product[0][2])
        print("Product category:", product[0][3])
        print("Product description:", product[0][4])
        print("Product sales:", product[0][5])

    inpp = input("\nEnter 1 to go back to user panel: ")
    if inpp == '1':
        admin_panel()
    else:
        pass
    
def logout():
    print("You are successfully Logged out!")
    # home.prog_execution()


# admin_panel()
# logout()
# product_details()
# customer_details()
# total_sales()
# delete_item()
# add_item()