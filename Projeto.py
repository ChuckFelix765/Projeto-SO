import pandas as pd
import matplotlib.pyplot as plt
from asyncio.windows_events import NULL
from queue import Queue

f = open("Teste.txt","r")
l = []
for x in f:
    res = [i for parte in x.split(',') for i in parte.split()]
    l.append(res)

colunas = max(len(row) for row in l)
for row in l:
     while len(row) < colunas:
          row.append(0)

df = pd.DataFrame(l)
df.columns = ['Nome', 'Entrada', 'Duracao'] + [f'I/O{i}' for i in range(colunas - 3)]
df['Entrada'] = pd.to_numeric(df['Entrada'])
df['Duracao'] = pd.to_numeric(df["Duracao"])

print(l)


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
filapid = [] #------------------

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

insere_fila(0)
processando = fila.get()
q = int(input("Defina o tamanho do quantum: "))
quantum = q

plt.ion()
fig, ax = plt.subplots()
ax.set_xlabel('Tempo')
ax.set_ylabel('Processos')
ax.set_title('Gráfico de Gantt')

while True:#len(l)>0 or not fila.empty():
    print("\n++++++++++++++++++++TEMPO %d+++++++++++++++++++++\n" %contador)

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
    #Verifica se tem chegada
    if contador > 0:
        chegada = insere_fila(contador)
        if chegada != 0:
            # o 0 serve so pra poder fazer comparacao
            #se tem chegada, entao faz print
            
            print("#[evento] CHEGADA <%s>" %chegada[0])
            chegada = 0
            

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
            if processando:
                 ax.barh(processando[0], processando[2], left=contador, color='skyblue')
                 plt.draw()
                 plt.pause(0.1)
    filapid.append(processando[0])

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



print("Ordem de execução dos processos: ", filapid)

plt.ioff()
plt.show()
