#Syntex error 
#ValueError is runtime error
try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not integer")