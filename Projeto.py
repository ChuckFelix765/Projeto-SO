f = open("Teste.txt","r")

l = []
dit = []

for x in f:
    res = [i for parte in x.split(',') for i in parte.split()]
    l.append(res)

print(l)

for i in range(len(l)):
    dic = {
        l[i][0] : i+1
    }
    dit.append(dic)


print(dit[0])

for i in range(len(l)):
    for j in range(len(l[i])):
        print(" ",l[i][j],end="")
    print()

f.close()