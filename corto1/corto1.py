

def fileAppend(b,fileName = 'collatz.txt'):

    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'a') #Abrir para agregar a archivo existente
    print(b)
    archivo.write(str(b)+'\n') #Escribe la lista b que contiene la suceción de turno
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura

def fileBorrar(fileName = 'collatz.txt'):
    archivo = open(fileName,'w') #Abrir para agregar a archivo existente
    archivo.write('')
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura


    #914

def NumParImpar(n):
    num=n       #variable que almacena el número en turno
    b=[]        #lista que guarda la sucesión de turno
    b.append(int(num))  #se agrega a la lista el número que será desglozado
    while num != 1:     #mientras no se llegue a 1 el while segura funcionando
        residuo=num%2
        if (residuo==0):
            num=num/2   
        else:
            num=3*num+1
        b.append(int(num))
    fileAppend(b)
    #print(b)

fileBorrar()    #se borra lo que este escrito en el documento collatz.txt

for i in range(2,915):
    NumParImpar(i)
   