import turtle as t
n = int(input("Input number of edges: "))
r = 360/n
for i in range(n):
    t.forward(100)
    t.left(r)
t.mainloop()
