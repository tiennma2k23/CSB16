print("== Registration ==")
username = input("Username: ")
password = input("Password: ")
while (True):
    repeat_password = input("Repeat password: ")
    if (repeat_password == password):
        break
    else:
        print("Passwords not match. Please input again.")
email = input("Email: ")
print("Registered successfully.")
