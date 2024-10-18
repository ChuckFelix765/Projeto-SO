f = open("Teste.txt","r")

l = []

for x in f:
    res = [i for parte in x.split(',') for i in parte.split()]
    l.append(res)

print(l)

f.close()