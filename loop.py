import random

def main():
    num = get_num()
    hello(num)

def get_num():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            return n 
    
def hello(n):
    for _ in range(n):
        print("welcome")
    
main()
family = ["Imran", "Kamran", "Salman", "Ali", "Akash", "Asgher" ]
for i in family:
    print(i)
print(family[4])  
#len for length
for i in range(len(family)):
    print(i+1,  family[i])

#Dictionary dict
Student = {
    "Ali": "Tandojam",
    "Sarwech": "Karachi",
    "Javeria": "Jamshoro",
    "Adnan" : "Tandojam"
}
for s in Student:
    print(s, Student[s], sep=", ")
#list of dictionary 
person = [
    {"name": "Ali Haider", "Father's Name": "Hamadullah", "Caste":"Abro"},
    {"name": "Faraz", "Father's Name": "Qaim", "Caste":"Massan"},
    {"name": "Saqib", "Father's Name": "M. Amin", "Caste":None}# None for null value

]
for p in person:
    print(p["name"], p["Father's Name"], p["Caste"], sep=", ")

#Nested looop
def main():
    print_Colomn(3)
    print_row(4)
    print_Sqr(6)

def print_Sqr(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def print_row(row):
    #for _ in range(row):
        print("?" * row)

def print_Colomn(n):
 for _ in range(n):
     print("#")

main()

max = int(input("what is max number to make even number: "))
num = []
for i in range(max + 1):
    if i % 2 == 0:
        num.append(i)

pas = int(input("how many letter do want to make pass? "))
for i in range(pas):
    i = random.randint(1, 9)
    print(i)

print(num)