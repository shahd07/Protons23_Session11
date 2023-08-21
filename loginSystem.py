# Define constants for messages and choices
USERNAME_MESSAGE = "Username: "
PASSWORD_MESSAGE = "Password: "
SECRET_MESSAGE = "Now enter your secret phrase for safekeeping: "
LOGIN_CHOICE = "1) Login"
REGISTER_CHOICE = "2) Register"
EXIT_CHOICE = "3) Exit"

# Initialize an empty dictionary as the database
database = {}

# Define a function to check if a username exists in the database
def username_exists(username):
    return username in database

# Define a function to handle user login
def login():
    username = input(USERNAME_MESSAGE)
    if not username_exists(username):
        return 0 # Username not found
    password = input(PASSWORD_MESSAGE)
    if password == database[username]["password"]:
        return username # Login successful
    else:
        return -1 # Incorrect password

# Define a function to handle user registration
def register():
    username = input(USERNAME_MESSAGE)
    if username_exists(username):
        return -1 # Username already exists
    password = input(PASSWORD_MESSAGE)
    secret = input(SECRET_MESSAGE)
    database[username] = {"password": password, "secret": secret}
    return 1 # Registration successful






while True: #loop runs forever till break
    c = printingOutAllChoicesAndReturnUserChoice()
    match c:
        case 1:

            s = fun2()
            if s == 0:
                print("error: username not found")
            elif s == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {s}!")
                print("Your secret phrase is:")
                print(database[s]["secret"])
            continue
        case 2:
            s=fun1()
            if s == 1:
                print("\nSuccessfuly Registered!")
            elif s==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
