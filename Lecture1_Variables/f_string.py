age_user = input("Please enter you age...")

# do calculcations here...

age_user = int(age_user)
current_year = 2025
estimated_birth_year = current_year - age_user

user_statement = "The estimated birth year is " + str(estimated_birth_year) + "!!"

print(user_statement)
print("The estimated birth year is", estimated_birth_year, "!!")

user_statement_formatted = f"The estimated birth year is {estimated_birth_year}!!"
print(user_statement_formatted)

print(f"The estimated birth year is {estimated_birth_year}!!")
