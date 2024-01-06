def main():
    y = int(input("What's y? "))
    if is_even(y):
        print("Even")
    else: 
        print ("odd")


def is_even(n):
   
     #return True if n % 2 == 0 else False
    return (n % 2 == 0)
'''
    if n % 2 == 0: 
        return True
    else: 
        return False 
   '''
    
main()

name = input("What is your name? ")
match name:
    case "Ali" | "jawad":
        print("your favaourite color is black")
    case "faraz":
        print("your favourite color is white")
    case _ :
        print("who?")

        
grade = int(input("Score: "))
if 80 <= grade <=  100:
    print("Grade A")
elif grade >= 70 and grade <=  90:
    print("Grade B")
elif grade >= 60 and grade <=  70:
    print("Grade C")
else: 
    print("Grade F")
x = int(input("What is x? "))
if x % 2 == 0:
    print(x, "is even")
else :
    print(x,"is odd")