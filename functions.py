# -*- coding: utf-8 -*-
import itertools
import collections
import math
import csv




def Perturbation(gs):
    for i in range(1,len(gs.args)):
        if "%" in gs.args[i]:
            return gs.args[i]


def ModelName(gs):
    for i in range(1,len(gs.args)):
        if "export:" in gs.args[i]:
             return gs.args[i].replace('export:', '')

#get from ginssim/biolqm model the list of components and their max level
def get_list_of_components_and_max(model):
    lst = []
    for node in model.getComponents(): #Java function
        if not node.isInput(): #Java attribute check if input node exist
            lst += [[str(node.nodeID).split("'")[0],node.max]] #making a list of components
    # return list of ['Node Name' , Node Max size]
    return lst

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


def Check_Duplications2(list_of_values):
    value_dict = collections.defaultdict(int)
    for item in list_of_values:
        print "\n"*6,item,"\n"*6
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


#call function get_list_of_components_and_max
#export_list_to_csv(get_list_of_components_and_max(Get_Model(gs)),Output_file_name(gs))
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


#Opening the model
def Get_Model(gs):
    g = gs.open(gs.args[0]) #get the file
    return g.getModel() #get the model



# input     -> "a",2args
# output    -> "a%2"
def get_concatenation(a,z):
    return a+"%"+str(z) #return a string

#["x","x"] --> ["x,x"]
def Join_List_to_Strings(lst):
    o = []
    for b in lst :
        o.append(",".join(b))
    return o #return list of strings

#converting a list of perturbation to bioLQM pattern
def Convert_list_perturbation_to_bioLQM(lst):
    couples = []
    for i in lst: #lst of element
        couples_joined = []
        elements = []
        for j in i: #element to string
            couple = get_concatenation(j[0],j[1])
            elements.append(couple)
        Joined_Couple = ""
        for e in range(len(elements)):
            Joined_Couple = Joined_Couple + str(elements[e])
            if e != len(elements)-1:
                Joined_Couple = Joined_Couple + ","
        couples.append(Joined_Couple)
    for c in couples:
        couples_joined.append(c)
    return couples_joined


#get component list from a list of components and their max
def get_component(list_of_components_and_max):
    list_of_components = []
    for e in list_of_components_and_max:
        for i in range(e[1]):
            list_of_components.append([e[0],i])
    return list_of_components

def tuples_to_lists(the_tuples):
    the_lists = []
    for t in the_tuples:
        the_lists.append(list(t))
    return the_lists


#get from ginssim/biolqm model the list of components and their max level
def get_list_of_components_and_max(model):
    lst = []
    for node in model.getComponents(): #Java function
        if not node.isInput(): #Java attribute check if input node exist
            lst += [[str(node.nodeID).split("'")[0],node.max]] #making a list of components
    # return list of ['Node Name' , Node Max size]
    return lst

# *******************************************************
# list_of_components: [["a",1],["b",0]]
# Size : the size of the combinations in the output
# *******************************************************
def get_perturbations_list(model,size):
    # get list_of_components_and_max from the given model
    list_of_components_and_max = get_list_of_components_and_max(model)

    #declaration
    list_of_components = []
    list_of_components = get_component(list_of_components_and_max)

    #1 - itertools  make combinations tuples from the list of components given
    #2 - Converting tuples from the List Of Tuples to List of lists to allaw working with indexes
    list_of_perturbations = tuples_to_lists(list(itertools.combinations(list_of_components, size)))

    #removing duplicated elements from the list of perturbations
    cleaned_list_of_perturbations = Remove_duplcations(list_of_perturbations)

    #returning the list of string each string refer to combination of component and a state
    return cleaned_list_of_perturbations






#check if output is set as args
def Output_file_name(gs):
    try:
        for i in range(1,len(gs.args)+1):
            try:
                splited_args = str(gs.args[i]).split('.')
                if splited_args[1] == "csv":
                    return gs.args[i]
            except Exception as e:
                return "NO_EXPORT"
        return "NO_EXPORT"
    except Exception as e2:
        return "NO_EXPORT"


#check if output is set as args
def GetPattern(gs):
    for i in range(1,len(gs.args)+1):
        try:
            splited_args = str(gs.args[i]).split(':')
            if splited_args[0] == "pattern":
                patterns = splited_args[1].split(',')
                return patterns
        except Exception as e:
            return "NO_EXPORT"
    return "NO_EXPORT"


#exporting the list as csv file
#if output file name not set in parameters this function is ignored
def export_list_to_csv(list_to_export,filename):
    if filename != "NO_EXPORT":
        try:
            with open(filename, 'wb') as myfile:
                writer = csv.writer(myfile, lineterminator='\n', quoting=csv.QUOTE_ALL)
                writer.writerows(list_to_export)
        except Exception as e3:
            raise
        return True
    else:
        print list_to_export


def get_perturbations_list(model,sizes):
    lst = []
    # get list_of_components_and_max from the given model
    #1 - itertools  make combinations tuples from the list of components given
    #2 - Converting tuples from the List Of Tuples to List of lists to allaw working with indexes
    #removing duplicated elements from the list of perturbations
    #returning the list of string each string refer to combination of component and a state
    for size in sizes:
        lst += tuples_to_lists(list(itertools.combinations(get_component(get_list_of_components_and_max(model)), size)))
    return lst

def perts_list_to_strings(list_of_perturbations):
    out_list = []
    for perturbation in list_of_perturbations:
        perturbation_out = ""
        for comp_state in perturbation:
            perturbation_out += comp_state[0]+"%"+str(comp_state[1])
        out_list.append(perturbation_out)
    return out_list



def export_1D_list_to_csv(list_to_export,filename):
    if filename != "NO_EXPORT":
        try:
            with open(filename,'wb') as outfile:
                for pert in list_to_export:
                    outfile.write(pert)
                    outfile.write("\n")
        except Exception as e3:
            return "exported"
    else:
        return list_to_export



def Perturbation(gs):
    for i in range(1,len(gs.args)):
        if "%" in gs.args[i]:
            return gs.args[i]

def ModelName(gs):
    for i in range(1,len(gs.args)):
        if "export:" in gs.args[i]:
             return gs.args[i].replace('export:','')



#convert one perturbation from csv file to biolqm string
def csv_to_biolqm(csvfile):
    biolqm = ""
    biolqmlist = []
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        list_st = list(reader)
        for i in list_st:
            flag = 0
            for j in i:
                flag +=1
                biolqm += j
                if flag%2:
                    biolqm += "%"
        biolqmlist += biolqm
    return biolqm


#take as input the name of csv file and return a list of perturbation extracted from this file
def csv_to_biolqmlist(csvfile):
    biolqm = ""
    biolqmlist = []
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        line = []
        for i in list(reader):
            mut = ""
            for j in i:
                k = j[2:-1].split(",")
                mut += str(k[0][0:-1])+"%"+str(k[1][1:])
            line.append(mut)
    return line

#get the csv file name from the inputs args
def get_csv_from_arg(gs):
    for i in range(1,len(gs.args)+1):
        try:
            splited = gs.args[i].split(".")
            if splited[1] == "csv":
                return gs.args[i]
        except Exception as e:
            pass
    return False


def value_input(value):
    if len(value.split("-"))>1:
        return range(int(value.split("-")[0]),int(value.split("-")[1])+1)
    return [int(value)]




#genereate perturbation from a given size
def generate_perturbations(list_of_comp_and_values,size):
    combo_of_comp_and_values = [list(itertools.combinations(list_of_comp_and_values, size))]
    return Remove_duplcations(combo_of_comp_and_values)


#filtre stable states
def SOME_stable_states_satisfy_patterns(list_of_stable_states_per_perturbations, patterns):
    for pattern in patterns:
        valid_st_st_per_perturbation = []
        for perturbation in list_of_stable_states_per_perturbations:
            for stable_state in perturbation[1]:
                counter = 0
                for postion_of_value in range(len(stable_state)):
                    if pattern[postion_of_value] == "*" or stable_state[postion_of_value] == -1:
                        counter = counter + 1
                    if pattern[postion_of_value] != "*" and stable_state[postion_of_value] != -1:
                        if str(stable_state[postion_of_value]) == pattern[postion_of_value]:
                            counter = counter + 1
                if counter == len(stable_state):
                    valid_st_st_per_perturbation.append([list(perturbation[0]),stable_state])
    return valid_st_st_per_perturbation


#apply input value(s) on the Max of conponents
def filter_by_value(comp_and_max,values):
    o = []
    for i in range(len(comp_and_max)):
        for value in values:
            if value <= comp_and_max[i][1]:
                if o != []:
                    if [comp_and_max[i][0],value] != o[-1]:
                        o.append([comp_and_max[i][0],value])
                else:
                    o.append([comp_and_max[i][0],value])
    return o

#get steable state / pert
def stable_state_per_perturbation(model,list_of_perturbations):
    all_stable_state = []
    for i in list_of_perturbations:
        blqm_list_of_perturbations = Convert_list_perturbation_to_bioLQM(i)
    print "__"*9
    for position in range(len(blqm_list_of_perturbations)):
        stable_state_per_perturbation = []
        Perturbed_Model = Apply_Perturbation_to_model(model,blqm_list_of_perturbations[position])
        d = [] #for debuguing
        for dd in blqm_list_of_perturbations[position]: #for debuguing
            d.append(dd) #for debuguing
        stable_states = Get_List_of_Stable_states(Perturbed_Model)
        for stable_state in stable_states :
            stable_state_per_perturbation.append(stable_state)
        all_stable_state.append([list_of_perturbations[0][position],stable_state_per_perturbation])
    return all_stable_state




def get_perturbations_per_stable_states(gs,value,size):
    stable_state_per_perturbation(generate_perturbations(filter_by_value(get_list_of_components_and_max(Get_Model(gs)),value_input(value)),size))
