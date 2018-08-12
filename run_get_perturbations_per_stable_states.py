#!/usr/bin/python
from functions import *


def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)


def saveModel(model,name):
    lqm.saveModel(model, str(name)+".ginml", "ginml")


def Get_Model_per_perturbations(model, list_of_perturbations):
    list_of_models = []
    for pert in list_of_perturbations:
        list_of_models.append([Apply_Perturbation_to_model(model,pert),pert])
    return list_of_models

def Get_Stable_States_of_Models_per_Perturbation(list_of_models):
    list_of_stable_states = []
    for model in list_of_models:
        #get service for stable states -- Java function
        ssrv = gs.service("stable")
        #get service for model -- Java function
        searcher = ssrv.getStableStateSearcher(model[0])
        searcher.run() # -- Java function
        #get stable states list as java obejctfrom collections import defaultdict
        paths = searcher.getPaths() # -- Java function
        for p in paths:
        # for each stabe state do:
            #extract the stable state from the java object1
            values = paths.getPath() # -- Java function
            # the object extracted is an array
            x = values.tolist() #convertiong the array to a list and adding to the output list of lists
            list_of_stable_states.append([x,model[1]])
    return list_of_stable_states


def filter_perturbations_by_stable_states_pattern(list_of_stable_states,list_of_patterns):
    list_of_pert = []
    for stable_state in list_of_stable_states:
        for pattern in list_of_patterns:
            counter = 0
            for pointer in range(len(pattern)):
                if str(pattern[pointer]) == str(stable_state[0][pointer]) or stable_state[0][pointer] == -1 or pattern[pointer] == "*" :
                    counter +=1
            if counter == len(pattern):
                if stable_state[1] not in list_of_pert:
                    print stable_state
                    list_of_pert.append(stable_state[1])
    return list_of_pert


#print stable_state_per_perturbation(gs,["AKT2%1","AKT2%0"])["***201011"]
print export_1D_list_to_csv(filter_perturbations_by_stable_states_pattern(Get_Stable_States_of_Models_per_Perturbation(Get_Model_per_perturbations(Get_Model(gs),perts_list_to_strings(get_perturbations_list(Get_Model(gs),Perturbation_size(gs))))),GetPattern(gs)), Output_file_name(gs))
