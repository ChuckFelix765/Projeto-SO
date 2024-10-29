from asyncio.windows_events import NULL
from queue import Empty, Queue

f = open("Teste.txt","r")
l = []
for x in f:
    res = [i for parte in x.split(',') for i in parte.split()]
    l.append(res)

print(l)


f.close()

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
ind = 0
fila = Queue(maxsize = len(l))
for i in range(len(l)):
    for j in range(1, len(l[i])):
        l[i][j] = int(l[i][j])
    if l[i][1] == 0:
        fila.put(l[i])
        ind = i
l.pop(ind)

quantum = 4
processando = []
contador = 0
#nada implementado ainda
print("=================================================")
print("========INICIANDO ESCALONADOR ROUND ROBIN========")
print("=================================================")

def evento(contador, quantum):
    #chegada
    ind = 0
    for i in range(len(l)):
        for j in range(1, len(l[i])):
            l[i][j] = int(l[i][j])
        if l[i][1] == contador:
            fila.put(l[i])
            ind = i
        l.pop(ind) 
    # 



while len(l)>0 or not fila.empty():
    print("++++++++++++++++++++TEMPO %d+++++++++++++++++++++" %contador)
    
    if len(processando) > 2:
        print("#[evento] OPERACAO I/O <%s>" %processando[0])
        if processando[3] == 0:
            processando.pop(3)
            if processando[2]>0:
                fila.put(processando)
                processando = []

    if quantum == 0:
        print("#[evento] FIM QUANTUM <%s>" %processando[0])
        quantum = 4
        if processando[2]>0:
                fila.put(processando)
                processando = []




    if fila.empty():
        print("Nao ha processos na fila")
    else:
        print(list(fila.queue))
        print()
    if not processando:   
        processando = fila.get()
        cont_p = 0

    print("CPU: ", processando)
     
    if len(processando) > 2:
        processando[3] -= 1

    quantum -= 1
    cont_p += 1
    processando[2] -= 1
    contador+=1
    exit




