print("Hello user!")
user_name = input("What is your name?")
user_age = int(input("What is your age?"))

voting_age = 18
years_voter = user_age - voting_age

output = user_name + ", you are allowed to vote for " + str(years_voter) + " Years."
print(output)
print(f"{user_name}, your are allowed to vote for {years_voter} years.")