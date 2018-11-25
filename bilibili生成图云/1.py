a1 = open("1.txt","r")
a2 = open("2.txt","r")
w = open("w","w")
a = []
b = []
for i in a1:
    a.append(i)
for i in a2:
    b.append(i)

for i2 in a:
    if i2 not in b:
        print(i2)
        w.write(i2)
