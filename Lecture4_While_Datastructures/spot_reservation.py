total_capacity = 10
reserved_spots = 0 

user_name = input("What is your name? ")
spots_requested = int(input(f"How many spots do you want to reserve? ({total_capacity - reserved_spots} available) "))

while reserved_spots < total_capacity:
    if (reserved_spots + spots_requested) <= total_capacity:
        reserved_spots += spots_requested
        print(f"Ok {user_name}, {reserved_spots}/{total_capacity} spots are taken. I will gladly accept {total_capacity - reserved_spots} more...")
    else:
        print("Sorry, there are not enough spots available... :(")

    if reserved_spots == total_capacity:
        break

    user_name = input("What is your name? ")
    spots_requested = int(input(f"How many spots do you want to reserve? ({total_capacity - reserved_spots} available) "))
