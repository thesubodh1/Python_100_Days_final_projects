import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","#","$","%","&","(",")","*","+"]

new_password = []
password = ""
print("Welcome to PyPassword Generator!")

num_letters = int(input("How many letters would you like in your Password:- "))
num_numbers = int(input("How many numbers would you like in your Password:- " ))
num_symbols = int(input("How many symbols would you like in your Password:- "))

for _ in range(num_letters):
    new_password.append(random.choice(letters))

for _ in range(num_numbers):
    new_password.append(random.choice(numbers))

for _ in range(num_symbols):
    new_password.append(random.choice(symbols))

random.shuffle(new_password)

for letters in new_password:
    password += "".join(letters)
print(f"Your Final Password is: {password}")