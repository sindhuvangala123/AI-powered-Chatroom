import random

# Get user's name
name = input("What's your name? ")
print(f"Hi there {name}!")

# Ask about hobbies
hobbies = input("What are your hobbies? ")
hresponses = ["Nice!", "Nice", "My hobby is chatting!", "My hobbies are chatting, and reading."]
print(random.choice(hresponses))

# Ask about the user's mood
mood = input("What is your mood today? ")

if mood.lower() == "angry":
    print("Oh!")
elif mood.lower() == "happy":
    print("Me too!")
else:
    print("Okay.")

# Ask for the name again
name1 = input("Can you please tell me your name again? ")
print("Okay, now I remember.")

# Ask for the user's age
num1 = 18  # Define age threshold
age = input("Can you also tell me your age? ")

# Convert the age input to an integer for comparison
try:
    age = int(age)
    if age < num1:
        print("So, you're a kid.")
    elif age > num1:
        print("That means you are an adult.")
    else:
        print("You're exactly at the threshold age.")
except ValueError:
    print("Please enter a valid number for age.")

# Random response about age
aresponses = ["I'm a day old", "I am 1 day old"]
print(random.choice(aresponses))
