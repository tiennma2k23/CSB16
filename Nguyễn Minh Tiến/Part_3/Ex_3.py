n = int(input("Input a month: "))
if (n == 2):
    print("This month has ", 28, "days")
elif n < 8:
    if n % 2 == 0:
        print("This month has ", 30, "days")
    else:
        print("This month has ", 31, "days")
else:
    if n % 2 == 0:
        print("This month has ", 31, "days")
    else:
        print("This month has ", 30, "days")
