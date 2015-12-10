def start():
    While True:
        a=[]    #Matriz 1
        b=[]    #Matriz 2
        nr_linhasA= int(input ("introduza o numero de linhas da primeira Matriz\n"))
        nr_colunasA= int(input ("introduza o numero de colunas da primeira Matriz\n"))
        nr_colunasB= int(input("o numero de colunas da segunda Matriz tem de ser\n"+str(nr_colunasA)+"\nintroduza o numero de colunas da segunda Matriz\n"))
        
        for i in range(nr_linhasA):
            a.append (tuple(input("introduza a linha "+str(i+1)+" da primeira matriz separando as entradas por virgulas\n").split(",")))
        for j in range(nr_colunasA):
            b.append(tuple(input("introduza a linha "+str(j+1)+" da segunda matriz separando as entradas por virgulas\n").split(",")))
        
        print ("primeira matriz e")
        escreve_matriz(a)
        print("a segunda matriz e")
        escreve_matriz(b)
        print("a multiplicação da")
        MM(a,b)
#fim start

def mul_matriz (a,b):
    ''' mul_matriz: matrix x matrix -> matrix (result of the multiplication)'''
    s=[]
    for l in range (len(a)):
        v=[] 
        v=[0,]*len(a)
        s.append(v[:])        
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                s[i][j] += int(a[i][k]) * int(b[k][j])
    return s
# fim mul_matriz

def escreve_matriz (m):
    for i in range (len(m)):
        print(m[i])
#fim escreve_matriz

def MM(a,b):
    escreve_matriz(mul_matriz(a,b))
#fim MM

start()
