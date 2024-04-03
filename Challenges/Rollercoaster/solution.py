#Write a program that takes user's height as input and if it is greater than 120, allows to ride the rollercoaster
# <12 "5$", 12-18 "7$", >18 "12$"
#Ask if they want photos add 3$ to the bill if so.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height>=120:
  print("You can ride the rollercoaster!")
  if age<12:
    bill = 5
  elif age<=18:
    bill = 7
  else:
    bill = 12

  photos = input("Do you want a photo taken? Y or N.")
  if photos == "Y":
    bill += 3

  print(f"Your total bill is {bill}$")

else:
  print("Sorry!, you have to grow taller to ride.")
