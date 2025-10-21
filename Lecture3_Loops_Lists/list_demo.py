friends = ["Rick", "Carl", "Daryl", "Maggie"]

for friend in friends:
    print(f"Hello {friend}!")
    
friends.insert(2, "Luke1")
friends.append("Luke2")
print("-"*20)
for friend in friends:
    print(f"Hello {friend}!")