age = 67
required_age = 18

if age >= required_age:
    print("You are allowed to enter")

# This is an example with more alternatives
if age >= required_age and age <= 65:
    print("You are allowed to enter!")
    print("You get no discount")
    print("Have fun")
elif age >= required_age and age >= 65:
    print("You are allowed to enter!")
    print("You are entitled for a discount")
else:
    print("Sorry, but you are not old enough.")
    print("Please try again when you are old enogh")

print("This is now outside")
