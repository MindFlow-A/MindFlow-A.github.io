import random

length = int(input("Length of the password"))

char = "abcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+"

for i in range(length):
    print(random.choice(char))
