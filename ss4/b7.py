import turtle as t
a = int(input("do dai canh 1: "))
b = int(input("do dai canh 2: "))
c = int(input("do dai canh 3: "))
if (a > b):
    tmp = a
    a = b
    b = tmp
if (a > c):
    tmp = a
    a = c
    c = tmp
if (b > c):
    tmp = b
    b = c
    c = tmp
# kiemtratamgiac
if ((a < (b+c) and (a > c-b)) and (b < (a+c) and b > c-a) and (c < (a+b) and c > b-a)):
    if (a == b & b == c):
        print("The 3 line segments can form an equilateral triangle.")
        for i in range(3):
            t.forward(a)
            t.left(120)
        t.mainloop()

    elif (a*a+b*b == c*c):
        print("The 3 line segments can form a right triangle.")
    else:
        print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")
