from asyncio.windows_events import NULL
from queue import Empty


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

print(dit)

#l[0] = o P_id
#l[1] = o tempo de chegada
#l[2] = a duracao
#l[3+] = indica o(s) momento(s) que ocorre a operacao I/O, separador por virgula


quantum = 4
contador = 0
fila = []


print()
for i in range(len(l)):
    if l[i][1] == '0':
        fila.append(l[i])

print(fila)


while len(fila) != 0:


    l.pop(0)
    print("Rodando")
print("Acabou")

