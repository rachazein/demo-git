#Ecrire l'algorithme de la suite de fibonacci:
#C'est une suite définie par Un = Un-1 + Un-2


def fibonacci(n:int):
   if n==1:
       return 1
   if n==2:
       return 1
   u0=0
   u1=1
   for x in range (3,n+1):
        un=u0+u1
        u0=u1
        u1=un
        return un
