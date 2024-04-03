#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to tip calculator!")
bill = float(input("Enter the bill amount: "))
people = int(input("Enter the number if people: "))
tip = int(input("How much would you like to pay? 10, 12 or 15: "))
tip_c = 1+(tip/100)
share = (bill / people) * tip_c
share_rd = format(share, ".2f")
print(share_rd)
