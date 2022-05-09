from ClaseConjunto import Conjunto
if __name__=='__main__':
    
    unObjetoA=Conjunto()
    unObjetoB=Conjunto()
    
    c=int(input('Ingrese cantidad de elementos del conjunto -A-: '))
    
    for i in range(c):
        unNum=int(input('Ingrese un numero para agregar al conjunto -A-: '))
        unObjetoA.Agregarnum(unNum)
        
    s=int(input('Ingrese cantidad de elementos del conjunto -B-: '))
    
    for i in range(s):
        unNum=int(input('Ingrese un numero para agregar al conjunto -B-'))
        unObjetoB.Agregarnum(unNum)
    
    