def lose(BLOC,fin):
    nbr_list_max=len(BLOC)
    nbr_list = 0
    while nbr_list!=nbr_list_max:
        if  BLOC [nbr_list][0]==0:
            fin=fin+1
        nbr_list= nbr_list + 1
    return fin

fin=0
BLOC=[[0,10,1,1],[0,12,2,1],[6,15,2,1],[0,25,1,1]]
print(BLOC)
fin=lose(BLOC,fin)
print(fin)
if fin == 3:
    print("perdu")