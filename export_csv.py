import csv

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


def csv_to_biolqm(csvfile):
    biolqm = ""
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        list_st = list(reader)
    for  i in list_st:
        biolqm = biolqm+str(list_st[0])+"%"+str(list_st[1])
    return biolqm
