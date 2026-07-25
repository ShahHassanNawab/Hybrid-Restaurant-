
users = []
Menu  = {
    1: {"name": "Burger", "price": 450},
    2: {"name": "Fries", "price": 200},
    3: {"name": "Small Pizza", "price": 600},
    4: {"name": "Medium Pizza", "price": 1000},
    5: {"name": "Large Pizza", "price": 1600},
    6: {"name": "Shawarma", "price": 350},
    7: {"name": "Cold Drinks", "price": 120}
}


cart=[]

def welcome():
    print("*"*50)
    print("        Welcome to Hybrid Resturent             ")
    print("*"*50)


# ========================================================================================================
def register():
    username = input("Enter user Name: ")
    email = input("Enter email")
    password = input("Enter Password")
    phonenNo = int(input("Enter Phone Number: "))

    user ={
        "User Name: ": username,
        "email: ": email,
        "Password: ":password,
        "phonenNo: ": phonenNo
}

    users.append(user)
    print("Register Sucessfully")


def login():
    email = input("Enter email")
    password = input("Enter Password")

    for user in users:
        if user["email"] == email and user["Password"] == password:
            print("Login Sucessfully")
            return
        
        print("Invilid email or password")

# =======================================================================================================
def Fast_Food_menu():
    print("Welcome to resturent")
    print('''Resturent Menu
    1) Burger           Rs: 450
    2) Fries            Rs: 200
    3) Small Pizza      Rs: 600
    4) Medium Pizza     Rs: 1000
    5) Large Pizza      Rs: 1600
    6) Shawarma         Rs: 350
    5) Cold Drinks      Rs: 120
    ''')


def Add_Food_To_Cart():
    Fast_Food_menu()
    while True:

        choice = int(input("""Enter Food Choice (0 to Exit):
    """))

        if choice == 0:
            break

        if choice not in Menu:
            print("Invalid Choice")
            continue

        quantity = int(input("Enter Quantity: "))

        # Add item to cart here...
        cart.append({
                    "name": Menu[choice]["name"],
                    "price": Menu[choice]["price"],
                    "quantity": quantity
                })
        
        print(Menu[choice]["name"])
        print("Food Added Successfully!\n")


def view_cart():
   
    G_total = 0
    
    print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total'}")

    for item in cart:
        total = item["price"]*item["quantity"]

        G_total += total 
        print(f"{item["name"]:<15}{item["quantity"]:<8}{item["price"]:<10}{total}")

        if G_total >= 6000:
            discount = G_total*0.20
            final_bill = G_total- discount
            print("Final Bill With 20 % Discount: ", final_bill)
            print("-"*30)
           
        else:
            print("No Discount")
            print("-"*30)
            print("Final Bill", G_total)

    print("-"*30)

# ===================================================================================================

def main():
    welcome()

    print("""
If you are new please Register 
1) Register
2) Login
""")

    choice = int(input("Entre 1 for Register and 2 for login: " ))
    if choice == 1:
        register()
        
    elif choice == 2:
        login()
    else:
        print("Invilid Number")

    while True: 
        print("""
    1) Add Food
    2) View Bill 
    3) Exit 
    """)
        choice = int(input("Enter 1 FOR FOOD and 2 for bill: "))

        if choice == 1:
            Add_Food_To_Cart()
        elif choice ==2: 
            view_cart()
        elif choice == 3:
            print("Thank for visiting ")
            break
        else:
            print ("Invilid Nuber you Enter ")

main()

