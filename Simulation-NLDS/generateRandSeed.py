import numpy as np
import networkx as nx

## Function to geneate seed
def generateRandSeed(num,Graph):
    """ A simple function to generate random seed """
    out = np.random.choice(list(range(Graph.number_of_nodes())),num,replace=False)    
    return(out)