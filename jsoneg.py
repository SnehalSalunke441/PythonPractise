import json

book = {}
book['tom'] = {
    'name' : 'Tom',
    'address' : '1 red street , NY',
    'phone' : 9898989
}

book['jerry'] = {
    'name' : 'Jerry',
    'address' : '11 blue street , NY',
    'phone' : 567656
}


str1 = json.dumps(book)   #dump 's' =  string
print(str1)

with open("book.txt", "w") as f:
    f.write(str1)
