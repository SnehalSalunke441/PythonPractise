#pypi.org

a = ("A", "B", "C")
b = ("Rose", "Mogra", "Lotus")

x = zip(a,b)
print(tuple(x))

dict1 = {
    "Snehal" : 39,
    "Vaishnavi" : 40,
    "Sakshi" : 41
}

print(dict1["Snehal"])

d1 = {0:"hello" , True:"dear" , "two":"world"}
# d2 = {["just","testing","you"]:"value"}    #Gives error, cause key shouldbe immutable

del(d1)