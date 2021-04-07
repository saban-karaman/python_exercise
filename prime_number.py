# prime number generator
prime_number = [2, 3, 5, 7]
def prime_checker(number):
  if number in prime_number:
    print(f"your number is prime number")
  elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    print(f"your number is prime number")
  else:
    print(f"your number is not prime number")  
n = int(input("Check this number: "))
prime_checker(number=n)
