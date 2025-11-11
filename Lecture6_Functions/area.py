def area(height, width, print_result=False):
    print("Calculating area... ")
    a = height * width
    
    if print_result:
        print(f"Area: {a}")
    return a

my_area = area(100, 150)
print("I'm here")
print(my_area)

my_area2 = area(10, 5, print_result=True)

max_area_to_build = 0.25

print(f"You are allowed to build on {my_area * max_area_to_build} sqm.")