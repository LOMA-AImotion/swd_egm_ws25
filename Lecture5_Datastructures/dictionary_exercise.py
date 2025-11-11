shopping_list = dict() 

user_response = input("Do you want to add an item (yes/no)? ")

while user_response !=  "no":
    item = input("Item: ")
    quantity = int(input("Quantity: "))

    shopping_list[item] = quantity

    user_response = input("Do you want to add an item (yes/no)? ")

print(shopping_list)
print(f"Keys: {shopping_list.keys()}")
print(f"Values: {shopping_list.values()}")
