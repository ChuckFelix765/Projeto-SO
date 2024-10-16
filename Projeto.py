f = open("Teste.txt","r")
for x in f:
    print("Sem split: ",x)
    esp = x.split()
    print("Com Split: ",esp)
    vir = x.split(",")
    print("com split: ",vir)
f.close()