class Conjunto:
    __lista=[]
    def __init__(self):
       self.__lista=[]
    def getConjunto(self):
        return self.__lista
    def Agregarnum(self,unNum):
        if num not in self.getConjunto():
            self.__lista.append(unNum)
    def __add__(self,otroConjunto):
        for i in range(len(otroConjunto.getConjunto())):
            if