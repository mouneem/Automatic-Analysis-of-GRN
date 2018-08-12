from Extract_Components import get_list_of_components_and_max
from Model import Get_Model
import itertools
import collections
import math
from export_csv import *


#Check if the input is range or int
def Perturbation_size(gs):
    for i in range(1,len(gs.args)):
        splited_arg = str(gs.args[i]).split("-")
        if len(splited_arg)>1:
            return range(int(splited_arg[0]),int(splited_arg[1])+1)
        try:
            size = int(gs.args[i])
            return [size]
        except ValueError:
            pass
    return [2]

#check duplicated items
#return boolean : true if an element exist in the list !
def Check_Duplications(list_of_values):
    value_dict = collections.defaultdict(int)
    for item in list_of_values:
        value_dict[item] += 1
    return any(val > 1 for val in value_dict.values())

#removing duplicated elements from the list of perturbations
def Remove_duplcations(list_of_perturbations):
    List_of_Duplicated_Elements = []
    for i in range(len(list_of_perturbations)):
        lst = []
        for j in list_of_perturbations[i]:
            lst.append(j[0])
        #checking for duplication in the list of combinations
        if Check_Duplications(lst):
            List_of_Duplicated_Elements.append(i)
        #end of if
    #end of for
    i = 0 # i = postion of the element to keep
    list_of_perturbationss_cleaned = [] # the output
    for i in range(len(list_of_perturbations)):
        if i not in List_of_Duplicated_Elements:
            list_of_perturbationss_cleaned.append(list_of_perturbations[i])
    #return
    return list_of_perturbationss_cleaned


#convert tuple to list
def tuples_to_lists(the_tuples):
    the_lists = []
    for t in the_tuples:
        the_lists.append(list(t))
    return the_lists

#get component list from a list of components and their max
def get_components(list_of_components_and_max):
    list_of_components = []
    for element in list_of_components_and_max:
        for i in range(element[1]+1):
            list_of_components.append([element[0],i])
    return list_of_components

#combination
def cobmine_perturbations(list_of_components,sizes):
    combos = []
        combo = []
        combo = Remove_duplcations(tuples_to_lists(list(itertools.combinations(list_of_components, size))))
        combos = combos + combo
    return combos


export_list_to_csv(cobmine_perturbations(get_components(get_list_of_components_and_max(Get_Model(gs))),Perturbation_size(gs)),Output_file_name(gs))
