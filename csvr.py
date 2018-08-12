import csv

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
        # for i in list_st:
        #     flag = 0
        #     for j in i:
        #         flag +=1
        #         biolqm += j
        #         if flag%2:
        #             biolqm += "%"
        # biolqmlist += biolqm
    return line

print csv_to_biolqmlist("file.csv")
