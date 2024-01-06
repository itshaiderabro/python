def main():
    name = input("What is your name?")
    hello(name)

def hello(to="World"):
    print("hello,", to)

def cal():
    x = int(input("what is x?"))
    print("x squared is", square(x))

def square(n):
    return n *n #pow(n, 2) n**2

main()
cal()

#campare conditions 
x = int(input("what's x? "))
y = int(input("what's y? "))
if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y")
else :
    print("x is equal to y")
#OR NOT etc
if x < y or x > y :
    print("x is not equal to y")


#LOOPS 
#while loop
i = 0
while i <= 3: 
    print(i)
    i += 1
#for loop
for i in range(3):#[0, 1, 2] this is every difficult way to use this loop 
    print("hello...!")
#easiest way to print something again and agian
print("welcome \n" * 3, end="")

#user input
while True:
    n = int(input("what's n? "))
    if n > 0:
        break
''' if n < 0:
        continue
    if n > 0:
        break'''
for _ in range(n):
    print("Hello")
    