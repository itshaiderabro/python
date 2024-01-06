price = {
    "January": 2322,
    "Febuary": 3223,
    "March": 54324,
    "April": 2311
         }
try:
    print(price["April"]+price["March"]+price["Febuary"])
    
    price.update({"May": 342})
    for i in price:
        print(i)
       
    print(price)
except TypeError:
    print("problem")
heroes = ["Ali", "Haider", "Akash", "Salman"]
print(len(heroes))
heroes.append("Asgher")
heroes.pop()
heroes.insert(1, "Aamir")
heroes.append("Asgher")
print(heroes)

heroes[1:3]=["Faraz"]
print(heroes)

max = int(input("Max number do you wanna square: "))

num = []
for i in range(max+1):
    if i % 2 == 0:
     num.append(i)

print(num)
def merge(arr1, arr2):
   # Merge two array 
   #  removing duplicates
   # sorting
   return sorted(set(arr1 + arr2))
a = [3, 34, 43, 2,6,6,3,6,4,1,5,63,]
b = [ 2,5 ,353 ,8,3,2,4,5,63]
c = merge(a, b)
print(c)