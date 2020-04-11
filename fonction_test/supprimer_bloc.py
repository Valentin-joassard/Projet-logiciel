BLOC=[[1,10,1,1],[5,12,2,1],[6,15,2,1],[22,25,1,1]]
# x y type valeur
def supprimer_bloc(BLOC,num_list_del):
    del BLOC[num_list_del]
    return BLOC