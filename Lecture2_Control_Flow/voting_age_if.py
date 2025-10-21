print("Hello user!")
user_name = input("What is your name?")
user_age = int(input("What is your age?"))

voting_age = 18

if user_age < voting_age:
    waiting_years = voting_age - user_age
    print(f"Sorry, you are not old enough to vote. Please wait {waiting_years} years.")
elif user_age == voting_age:
    print(f"Congrats {user_name}, this will be your first time voting!")
else:
    years_voter = user_age - voting_age
    print(f"{user_name}, your are allowed to vote for {years_voter} years.")
