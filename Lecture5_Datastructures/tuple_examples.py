person1 = ("Jane", "Doe", 31, True)
person2 = ("Martina", "Musterfrau", 34, False)
person3 = ("Max", "Mustemann", 35, True)
persons = [person1, person2, person3]

first_name, last_name, age, joins = person1
print(first_name)

for first_name, last_name, age, joins in persons:
    print(f"Name: {last_name}, Age: {age}")

