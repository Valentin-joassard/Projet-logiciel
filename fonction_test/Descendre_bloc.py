def Descendre_Bloc(BLOC):
    nbr_list_max=len(BLOC)
    nbr_list = 0
	
    while nbr_list!=nbr_list_max:
	    BLOC [nbr_list][1]=BLOC [nbr_list][1] -1
	    nbr_list= nbr_list + 1
    return BLOC

BLOC=[[1,10,1,1],[5,12,2,1],[6,15,2,1],[22,25,1,1]]
print(BLOC)
BLOC=Descendre_Bloc(BLOC)
print(BLOC)