# shahdod and fayhaa were here
#we want hohos
USERNAME_MESSAGE = "Username: "
PASSWORD_MESSAGE = "Password: "
SECRET_MESSAGE = "Now enter your secret phrase for safekeeping: "
LOGIN_CHOICE = "1) Login"
REGISTER_CHOICE = "2) Register"
EXIT_CHOICE = "3) Exit"

# Initialize an empty dictionary as the database
database = {}


def username_exists(username):

    return username in database

def login():

    username = input(USERNAME_MESSAGE)

    if not username_exists(username):

        return 0 
    
    password = input(PASSWORD_MESSAGE)

    if password == database[username]["password"]:

        return username
    
    else:

        return -1 # Incorrect password


def register():

    global username

    username = input(USERNAME_MESSAGE)

    if username_exists(username):

        return -1 # Username already exists
    
    password = input(PASSWORD_MESSAGE)

    secret = input(SECRET_MESSAGE)

    database[username] = {"password": password, "secret": secret}

    return 1 # Registration successful

def choice():

    print("What would you like to do (^u^) ?")
    print("=============================")
    print(LOGIN_CHOICE)
    print(REGISTER_CHOICE)
    print(EXIT_CHOICE)
    v = int(input("> "))
    print("")
    return v


while True: 

    c = choice()
    match c:
        case 1:

            s = login()

            if s == 0:

                print("error: username not found ('o')")

            elif s == -1:

                print("error: incorrect password (;-;)")

            else:

                print(f"\nWelcome back \(>w<)/ {username}!")

                print("Your secret phrase is:")

                print(database[username]["secret"])

            continue

        case 2:

            s=register()

            if s == 1:

                print("\nSuccessfuly Registered! (UwU)")

            elif s==-1:

                print("error: username already exists ('-')")

            continue

        case 3:
        
            print("Thank You ('u')")

            break

        case _:

            print("error: invalid input")
