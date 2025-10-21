friends = ["Rick", "Carl", "Daryl", "Maggie"]

mixed_list = ["Rick", 0.97, 4, True]

for element in mixed_list: 
    print(f"Element {element} has type {type(element)}")
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,]
]

for row in matrix: 
    for i_j in row:
        print(i_j)
    print("-------")