print("== Registration ==")
username = input("Username: ")
while (True):
    password = input("Password: ")
    chu = False
    so = False
    for i in range(len(password)):
        ch = password[i]
        if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            chu = True
        if (ch >= '0' and ch <= '9'):
            so = True
    if (len(password) < 8 or chu == False or so == False):
        print("Invalid password. Please input again.")
    else:
        break
while (True):
    repeat_password = input("Repeat password: ")
    if (repeat_password == password):
        break
    else:
        print("Passwords not match. Please input again.")
while (True):
    email = input("Email: ")
    ok1 = False  # @
    ok2 = False  # .
    for i in range(len(email)):
        ch = email[i]
        if (ch == '@'):
            ok1 = True
        if (ch == '.'):
            ok2 = True
    if (ok1 and ok2):
        break
    else:
        print("Invalid email. Please input again.")
print("Registered successfully.")
