# exercise 1

from datetime import datetime

# part 1
now = datetime.now().date()

age = 16
name = "Eleanor"

print(f"OMG {name}, you are {age} years old so you where born in {now.year - age}!")

print(now.month)

age = input("How old are you (in digits)? ") # ask user for their age
day_birth = input("Which day you were born on? ") # ask user for their birth day
month_birth = input("Which month you were born in (in digits)? ") # ask the user for their birth month


day_hours = (now.day - int(day_birth)) * 24 # calculate the amount of hours the user has lived (days' difference)
month_hours = (now.month - int(month_birth)) * 24 * 30 # calculate the amount of hours the user has lived (months' difference)
year_hours = int(age) * 365 * 24 # calculate the amount of hours the user has lived (years' difference)

hours_lived = day_hours + month_hours + year_hours

print(f"You have been alive for a total of {hours_lived} hours. Cool!")







