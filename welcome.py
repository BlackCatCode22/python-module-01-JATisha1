# welcome.py
import datetime

# for getting thr the current time
current_time = datetime.datetime.now().time()

# check condition
if current_time.hour < 12:
    greeting = "Good morning"
elif 12 <= current_time.hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Ask for the user's name
name = input("Enter your name: ")

# Print the  greeting
print(f"{greeting}, {name}!")
