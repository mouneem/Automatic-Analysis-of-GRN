# -*- coding: utf-8 -*-

def Apply_Perturbation_to_model(model,perturbation):
    return lqm.modifyModel(model,"perturbation",perturbation)

def Perturbation(gs):
    for i in range(1,len(gs.args)):
        if "%" in gs.args[i]:
            return gs.args[i]

def ModelName(gs):
    for i in range(1,len(gs.args)):
        if "export:" in gs.args[i]:
             return gs.args[i].replace('export:', '')
