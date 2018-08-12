from export_csv import *

#get from ginssim/biolqm model the list of components and their max level
def get_list_of_components_and_max(model):
    lst = []
    for node in model.getComponents(): #Java function
        if not node.isInput(): #Java attribute check if input node exist
            lst += [[str(node.nodeID).split("'")[0],node.max]] #making a list of components
    # return list of ['Node Name' , Node Max size]
    return lst

#call function get_list_of_components_and_max
#export_list_to_csv(get_list_of_components_and_max(Get_Model(gs)),Output_file_name(gs))
