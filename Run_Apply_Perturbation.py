# -*- coding: utf-8 -*-
from Model import Get_Model
from Apply_Perturbations import Perturbation
from Apply_Perturbations import ModelName

def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

def saveModel(model,name):
    lqm.saveModel(model, str(name)+".ginml", "ginml")

saveModel(Apply_Perturbation_to_model(Get_Model(gs),Perturbation(gs)), ModelName(gs))
