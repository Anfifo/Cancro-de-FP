def mandatos (nr_mandatos,nr_votos):
    dep=[0,]*len(nr_votos)   #mandatos atribuidos
    div=[1,]*len(nr_votos)   #lsita dos divisores
    lista_nr_votos=list(nr_votos)   
    k=1
    for i in range(nr_mandatos):               
        l=0
        j = maxind(lista_nr_votos)
        
        if len(j) >= 2 :
            for k in range(len(j)):     
                if max1>nr_votos[j[k]]: 
                    max1=nr_votos[j[k]]
                    l=k               
            
        dep[j[l]]=dep[j[l]]+1  
        div[j[l]]=div[j[l]]+1        
        lista_nr_votos[j[l]]= nr_votos[j[l]]/div[j[l]] 
    return tuple(dep)

def maxind(lista):
    '''A funcao "maxind" retorna a posicao de um maximo numa lista qualquer'''
    lista_max=[]
    for i in range(len(lista)):                             
        if lista[i]==max(lista):
            lista_max = lista_max + [i]
    return lista_max

