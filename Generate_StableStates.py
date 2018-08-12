# -*- coding: utf-8 -*-
def Get_List_of_Stable_states(gs,model):
    list_of_stable_states = []
    #get service for stable states -- Java function
    ssrv = gs.service("stable")

    #get service for model -- Java function
    searcher = ssrv.getStableStateSearcher(model)
    searcher.run() # -- Java function

    #get stable states list as java obejctfrom collections import defaultdict

    paths = searcher.getPaths() # -- Java function
    for p in paths:
    # for each stabe state do:
        #extract the stable state from the java object1
        values = paths.getPath() # -- Java function
        # the object extracted is an array
        x = values.tolist() #convertiong the array to a list and adding to the output list of lists
        list_of_stable_states.append(x)

    return list_of_stable_states
