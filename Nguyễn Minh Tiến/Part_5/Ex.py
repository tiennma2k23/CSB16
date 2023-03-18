# import random
# print("== FREAKING MATH CONSOLE ==")
# print("Give correct answers to get scores.")
# print("")
# str = "+-*/"
# score = 0
# while (True):
#     a = random.randint(1, 100)
#     b = random.randint(1, 100)
#     c = random.randint(1, 10000)
#     ch = random.randint(0, 3)
#     if (ch == 0):
#         kq = a+b
#     elif ch == 1:
#         kq = a-b
#     elif ch == 2:
#         kq = a*b
#     else:
#         kq = a/b
#     rand = random.randint(0, 1)
#     if (rand == 1):
#         print(a, str[ch], b, "=", kq)
#         select = int(input("1 for True, 0 for False: "))
#         if (select == 1):
#             score += 1
#             print("Score: ", score)
#             print("")
#         else:
#             print("Incorrect.")
#             break
#     else:
#         print(a, str[ch], b, "=", c)
#         ans = 0
#         if (kq == c):
#             ans = 1
#         select = int(input("1 for True, 0 for False: "))
#         if (select == ans):
#             score += 1
#             print("Score: ", score)
#             print("")
#         else:
#             print("Incorrect.")
#             break
# print("")
# print("== GAME OVER ==")
# print("Your total score is", score)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
d = int(input("Nhap d: "))
if a == b and b == c and c == d:
    print("Khong co")
else:
    # tim max 1
    max1 = max(a, b, c, d)
    max2 = min(a, b, c, d)
    if (max2 <= a and a != max1):
        max2 = a
    if (max2 <= b and b != max1):
        max2 = b
    if (max2 <= c and c != max1):
        max2 = c
    if (max2 <= d and d != max1):
        max2 = d
    print(max2)
