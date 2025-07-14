import random

list_of_chars = ["A","J","L","c","m","e"]
password_list = []

while True:
    user_num = int(input("how many characters do you want in your password"))
    if user_num > 0:
        break

for _ in range(user_num):
    char = random.choice(list_of_chars)
    password_list.append(char)

password = "".join(password_list)
print(password)
