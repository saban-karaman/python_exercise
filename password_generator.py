#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
counter = nr_letters + nr_symbols + nr_numbers
for pass_letters in range(0, nr_letters):
  random_letters = random.choice(letters)
  password.insert(pass_letters, random_letters)
for pass_numbers in range(0, nr_numbers):
  random_numbers = random.choice(numbers)
  password.insert(random.randint(0, counter), random_numbers)
for pass_symbols in range(0, nr_symbols):
  random_symbols = random.choice(symbols)
  password.insert(random.randint(0, counter), random_symbols)
you = str(password[0])
for x in range(1, len(password)):  
  you += str(password[x])
 
print(f"Here is your password : '{you}''")