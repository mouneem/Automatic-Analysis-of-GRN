#Opening the model
def Get_Model(gs):
    g = gs.open(gs.args[0]) #get the file
    return g.getModel() #get the model
