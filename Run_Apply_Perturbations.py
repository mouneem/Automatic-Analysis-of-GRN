#!/usr/bin/python
from functions import *


def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)


def saveModel(model,name):
    lqm.saveModel(model, str(name)+".ginml", "ginml")


#appluy a list of perturbation on a model
def apply_list_of_pert(gs,csv_file,Output_file_name):
    counter = 1
    model = Get_Model(gs)
    list_of_pert = csv_to_biolqmlist(csv_file)
    for perturbation in list_of_pert:
        counter += 1
        saveModel(Apply_Perturbation_to_model(model,perturbation),str(Output_file_name+str(counter)))
    return True


apply_list_of_pert(gs,get_csv_from_arg(gs),ModelName(gs))
