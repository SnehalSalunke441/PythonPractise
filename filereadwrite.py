f = open("sunny.txt","r")
f1 = open("sunny2.txt", "w")
for line in f:
    token = line.split(' ')
    f1.write(line + "wordcount:  " + str(len(token)))
    print()
f.close()
f1.close()
