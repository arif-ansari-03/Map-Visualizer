import numpy as np
import csv

def read_data(file_path):  
    rows = []
    with open(file_path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

    data = np.asarray(rows)
    data = data.T[[6, 7]]
    data = data.T

    label = data[0]
    data = data[1:]
    newdata = []
    
    for row in data:
        f = 0
        for x in row:
            try:
                float(x)
            except:
                f = 1
                break
        if not f:
            newdata.append(tuple([float(x) for x in row]))

    return newdata