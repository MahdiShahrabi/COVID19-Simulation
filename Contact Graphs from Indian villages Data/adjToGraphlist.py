import pandas as pd
import networkx as nx
import glob
import os


## Function to read a type of adjency matrixes of Indian villages, and then create a list
def adjToGraphlist(name,path):
    
    # Location of data
    all_files = sorted(glob.glob(path + "/*"+name+"*.csv"),key=os.path.getmtime)


    li = []
    
    # Reading all adjecny matrixes based on the name
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=None)
        li.append(df)
    
    GraphList=list()
    
    #Converting each adj to a networkx garph object
    for i in range(len(li)):
        GraphList.append(nx.from_pandas_adjacency(li[i]))
        
    return(GraphList)