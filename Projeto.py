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



fila = Queue(maxsize = len(l))

def insere_fila(contador):
    ind = 0
    for i in range(len(l)):
        for j in range(1, len(l[i])):
            l[i][j] = int(l[i][j])
        if l[i][1] == contador:
            fila.put(list(l[i]))
            ind = i
            #l.pop(ind)
            return l[i][0] and l.pop(ind)
    return 0


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
            fila.put(list(l[i]))
            ind = i
        l.pop(ind) 

insere_fila(0)
processando = fila.get()
q = int(input("Defina o tamanho do quantum: "))
quantum = q
while True:#len(l)>0 or not fila.empty():
    print("\n++++++++++++++++++++TEMPO %d+++++++++++++++++++++\n" %contador)
    #Verifica se tem chegada
    if contador > 0:
        chegada = insere_fila(contador)
        if chegada != 0:
            # o 0 serve so pra poder fazer comparacao
            #se tem chegada, entao faz print
            
            print("#[evento] CHEGADA <%s>" %chegada[0])
            chegada = 0


    #verifica se possui IO
    if len(processando) > 3:
        #se possui, verifica se ele nao atingiu 0
        if processando[3] == 0 :
            #se atingiu 0, mostra evento
            print("#[evento] OPERACAO I/O <%s>" %processando[0])
            #pop no processo IO que estava em andamento
            processando.pop(3)
            fila.put(list(processando))
            processando.clear()
            quantum = q
            

    if quantum == 0:
        print("#[evento] FIM QUANTUM <%s>" %processando[0])
        quantum = q
        if processando[2]>0:
                fila.put(list(processando))
                processando.clear()


    if processando and processando[2] == 0:
        quantum = q
        print("#[evento] ENCERRANDO <%s>" %processando[0])
        processando.clear()

    if not processando and fila.empty():
            print("ACABARAM OS PROCESSOS!!!")
            print("-----------------------------------")
            print("------- Encerrando simulacao ------")
            print("-----------------------------------")
            break

    if not processando and not fila.empty():   
            processando = fila.get()

    if fila.empty():
        print("Nao ha processos na fila")
    else:
        print("FILA: ", end="")
        for i in list(fila.queue):
             print("%s(%d)" %(i[0], i[2]), end=" ")
        print()

    if processando:
        print("CPU: %s(%d)" %(processando[0], processando[2]))



     
    if len(processando) > 3:
        for i in range(3, len(processando)):
            processando[i] -= 1 

    quantum -= 1

    processando[2] -= 1
    contador+=1

   


print("Acabou")


