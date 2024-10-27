from asyncio.windows_events import NULL
from queue import Empty


f = open("Teste.txt","r")
l = []
for x in f:
    res = [i for parte in x.split(',') for i in parte.split()]
    l.append(res)

print(l)


f.close()

fila = []

'''
Lembrando:
index 0 -> P_ID
index 1 -> Tempo de chegada
index 2 -> Duração
index 3+ -> I/O
'''

# transforma todos os valores de String -> Int 
# para poder subtrair quando implementar o resto
# também coloca o processo que chega no instante 0 na fila
for i in range(len(l)):
    for j in range(1, len(l[i])):
        l[i][j] = int(l[i][j])
    if l[i][1] == 0:
        fila.append(l[i])
    

contador = 0
#nada implementado ainda
print("=================================================")
print("========INICIANDO ESCALONADOR ROUND ROBIN========")
print("=================================================")

while len(fila) > 0:
    print("++++++++++++++++++++TEMPO %d+++++++++++++++++++++", contador)
    for i in fila: 
        print(i[0])
    
    print()


    contador+=1
    exit

def mostra_fila(fila):
    if len(fila) < 1:
        return "Nao ha processos na fila"
    return ("%s",fila)
        

