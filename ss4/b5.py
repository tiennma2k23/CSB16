print("Welcome to The Ultimate Sercurity System")
_user = input("Username: ")
_pass = input("Password: ")
if (_user == "admin" and _pass == "12345"):
    print("You are logged in, admin.")
else:
    print("Wrong username or password.")
