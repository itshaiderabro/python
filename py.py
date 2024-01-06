print("hello world!")
name =  input("what is your Name?").title().capitalize()
#remove whitespace from str even we can do it in single line
#name = name.strip().title() we can also split this name into first and last name 
#first, last = name.split(" ")
#print(first)

#you can seprate the arguments by comma.
print("hello,", name)
print("hey " + name + " your name is beautiful!")
#when we pass some arguements in function that's called parameter.
print("hello, ", end="") #end="" that end of this program and move to next line
print("hello, ", name, sep=";"+ "there is some mistake" )
print(name)
#if you tell the python that these are some specail character/format str F so it in {} this bracket well show that. F tells the python for specail character
#print(f"hello, {name}")
#You can discribe the data type by only int str float etc.
x= int(input("what is the vlaue of X?"))
y =  float(input("What is value of Y?"))
#Round is the function to round off
z = round(x + y)
print(f"{z:,}")#f for formatted str and :, is for US numberic system that , after evry three letter
print(round(x/y,3))# we can use same thing by f str (f"{z:.2f}")




