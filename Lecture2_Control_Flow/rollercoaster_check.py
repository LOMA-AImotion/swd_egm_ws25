user_height = int(input("Please enter your height (in cm): "))

minimum_height = 150

if user_height > minimum_height:
    print("You are allowed to ride!")
    print("Please pay the fare!")
else:
    print("Sorry, but you are not tall enough to ride!")