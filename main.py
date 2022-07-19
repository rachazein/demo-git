#Ecrire l'algorithme de la suite de fibonacci:
#C'est une suite définie par Un = Un-1 + Un-2


def fibonacci(nb_entier:int):
    """
    une fonction qui calcule la suite de fibonacci pour un nombre entier 
    elle prend un seul argument n de type int
    """
    if nb_entier==1:
        return 1
    if nb_entier==2:
        return 1
    elt_0=0
    elt_1=1
    for x in range (3,nb_entier+1):
         elt_n=elt_0+elt_1
         elt_0=elt_1
         elt_1=elt_n
         return elt_n
