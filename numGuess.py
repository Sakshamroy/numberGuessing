#importing libaries and number range
import random
secret = random.randint(1, 100)

attempts = 0 # defining no of attempts 
max_attempts = 10  # maximum number of guesses allowed
print("Welcome to the Number Guessing Game!")
print("Myself:- Saksham")

#define weather guessing no is prime or not for hints 
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n ** 0.5) +1,2):#finding prime number other than 2 
        if n % i == 0:
            return False
    return True
def generate_hints(secret):
    hints = []
    #generating hints for gussing number 
    if secret % 2 == 0:#for odd and even numbers
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")

    if is_prime(secret):#for prime numbers 
        hints.append("The number is prime.")
    else:
        hints.append("The number is not prime")
    
    if secret % 3 == 0:
        hints.append("The number is divisible by 3")
    if secret % 5 == 0:
        hints.append("The number is divisible by 5")
    if secret % 10 == 0:
        hints.append("The number is divisible by 10")
    return hints

#taking user input

hints = generate_hints(secret)
while True:
    
    user_input = input("Guess a number (1-100):")#this "reveal" feature add with help of
        
    guess = int(user_input)
    
    attempts += 1

    if attempts > max_attempts:
        print(f"Game Over! You've used all attempts. The number was {secret}")
        break

    if guess == secret:
        print(f"correct! You've guessed the number {secret} in {attempts} attempts.")
        break
    elif guess < secret:
        if secret - guess > 15:
            print("too low! think bigger ")
        else:
            print("Low! but you're close")
        if attempts <= len(hints):
            print("Hint:", hints[attempts-1])
        else:
            print("Hint:", hints[-1])
    else:
        if guess - secret < 15:
            print("Too high! ")
        else:
            print ("High little less ")
        if attempts <= len(hints):
            print("Hint:", hints[attempts-1])
        else:
            print("Hint:", hints[-1])
print("Thanks for playing!")

