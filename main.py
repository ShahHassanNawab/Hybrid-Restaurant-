
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
Rmenu = {
    1: {"name": "Half chicken Karahi", "price": 1000},
    2: {"name": "Full chicken Karahi", "price": 1600},
    3: {"name": "Fish per KG", "price": 800},
    4: {"name": "Chicken Malai Boti", "price": 750},
    5: {"name": "Special Bairyani", "price":550 },
    6: {"name": "Naan/Roti", "price": 30}
}

cart=[]

def welcome():
    print("*"*50)
    print("        Welcome to Hybrid Resturent             ")
    print("*"*50)


def hybrid():
    print("""
    1) Fast food
    2) Desi Food Resturent 
    2) Hotel 
    """)

def DesiRes():
    print("""
        1) Half chicken Karahi        Rs 1000
        2) Full chicken Karahi        Rs 1600
        3) Fish per KG                Rs 800
        4) Chicken Malai Bot          Rs 750
        5) Special Bairyani           Rs  550
        6) Naan/Roti                  Rs  30
    """)

    while True:

        choice = int(input("Enter food choice : "))
        if choice == 0:
                break
        
        if choice not in Menu:
            print("Invalid Choice")
            continue

        quantity = int(input ("Enter quantity"))
        cart.append({
            "name": Rmenu[choice]["name"],
            "price":Rmenu[choice]["price"],
            "quantity": quantity
        })

        print("Added Sucessfully ")
        
    
# ========================================================================================================
def hotel():
    
    print("""Only Booking Room  System
    1) Standard Room 
    2) Delux Room
    3) Exit
 """)

    charges = 0
    choice = int(input("Enter Room Choice: "))

    if choice == 1:
        print("""Standard Room Select Rent per day is 2000
        Common featue of standard Room is 
        1) 2 Single bed
        2) Free Wifi
        3) Drinking Water
        """)


        days = int(input("Enter Number of days to stay: "))
        bill = 2000*days

        print("="*30)
        print("Total Bill is : ",bill)
        print("="*30)

    elif choice == 2:
        print("""Delux Room select Rent per day 5000
        Deluxe Room Features
        1) Free Wifi
        2) Sitting Area
        3) Mini refrigerator
        4) Air conditioning / heating
        5) Tea/coffee maker
        6) Smart TV / LED TV
        7) Private bathroom with hot & cold water
        """)


        days = int(input("Enter number of day to stay: "))
        bill = 5000*days

        print("="*30)
        print("Total Bill : ", bill)
        print("="*30)

    elif choice ==3:
        print("Thanks")
        
    else:
        print("Invilid number you enter ")

    
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
    
    print(f"{'Item':<25}{'Qty':<10}{'Price':<10}{'Total'}")

    for item in cart:
        total = item["price"]*item["quantity"]

        G_total += total 
        print(f"{item["name"]:<25}{item["quantity"]:<10}{item["price"]:<10}{total}")

        print("*"*30)
        print("Final Bill: ", G_total)

    print("*"*30)


# ===================================================================================================
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
        

    print("""
        1) Fast food
        2) Desi Food Resturent 
        2) Hotel 
        """)

    choice = int(input("Enter Your choice: "))

    if choice == 1:
        print("#"*40)
        print("          Welcome to fast Food ")
        print("#"*40)
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

    elif choice == 2:
        print("#"*40)
        print("Welcome to Resturent")
        print("#"*40)

        DesiRes()
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

    elif choice == 3:
        print("#"*40)
        print("Welcome to Hotel")
        print("#"*40)






