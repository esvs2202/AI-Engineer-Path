has_ticket = False 
age = 18

if has_ticket:
    if age >= 18:
        print("Enjoy the movie !")
    else:
        print("Need supervision")
else:
    print("Go and get a ticket")

# lists

l = [1,"Sriram",56.00]

print(l)

l.append("Sahiti")

print(l)

# dictionaries
d = {"name":"Alice",
     "age":25,
     "city": "Newyork"}

print(d["name"])
print(d.get("age"))

# adding element
d["license"] = True 

print(d)

# tuples are immutable data structures in python

t = (1,2,3)

# t[3] = 4

# sets are the unordered collection of the unique objects

l = [1,1,1,2,2,3,4,5,5]

s = set(l)  # drops duplicates

print(s)

