k = int(input("Up to which number should I count the even numbers?"))

for i in range(1, k+1):
    if i % 2 == 0: 
        print(f"Number {i} is even!")
    else:
        print(f"Number {i} is NOT even!")
