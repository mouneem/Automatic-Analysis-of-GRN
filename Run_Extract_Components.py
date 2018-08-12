from Extract_Components import *
from Model import Get_Model

#call function get_list_of_components_and_max
export_list_to_csv(get_list_of_components_and_max(Get_Model(gs)),Output_file_name(gs))
