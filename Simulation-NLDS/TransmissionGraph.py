import networkx as nx
import pandas as pd
import numpy as np
## Creating the transimmsion graph based on the multigraph to run the simulatin on
def TransmissionGraph(Data,Label_dict = {"Money":0.2,"Visit":0.3,"Kerosene":0.1,"Temple":0.25},
                 dropNode="",dropTop=0):
        
        # Initilizing output 
        out = list()
        # For every Graph in GraphList
        for G in Data:
            ############# Filtering Nodes #############
            if len(dropNode)!=0:
                # A dictionary of the node and the specific characteristics by which we want to filter
                listNodeAttr = nx.get_node_attributes(G,name=dropNode)
                # Find the threshold for that characteristics. Edges from a node with larger char, will drop.
                threshold = np.percentile(list(listNodeAttr.values()),100-dropTop)
                # List of nodes that must be quarantined!
                DropList = [k for k,v in listNodeAttr.items() if v>threshold ]
                # Removing edges from that node. Quarantining!
                for node in DropList:
                    edgelist = list(G.edges(node))
                    G.remove_edges_from(edgelist)

  
            ############# Correcting the weights of Edges #############
            for u,v,key,atrr in list(G.edges(data=True,keys=True)):
                # changing the weight
                G[u][v][key]['weight'] = Label_dict[atrr['label']]
                
     
            ############# Calculating overall transmission probability #############
            # Iterating over each two nodes that there is at least 1 edge between
            for (u,v) in list(set(G.edges())):
                # Keys : number of edges between this two nodes
                keys = list(G.get_edge_data(u,v).keys())
                # 1 - Transimision probability : each element for one edge
                noTransProb = [(1-G[u][v][i]['weight']) for i in keys]
                # The probability that at least one of the edges infects other people
                newWeight = np.round(1-np.prod(noTransProb),3)
                # Removind old edges: key by key
                for i in keys:
                    G.remove_edge(u,v,key=i)
                # Add new edge, which weight shows the transmission probability
                G.add_edges_from([(u,v)],weight=newWeight)
                
                
            ############# Dropping Edges with weight 0 ###########
            # Iterating over all edges
            for u,v,key,atrr in list(G.edges(data=True,keys=True)):
                # If the edge has a attribute which is in dropEdge list:
                if G[u][v][key]['weight']==0:
                    # We remove that edge
                    G.remove_edge(u,v,key=key)
                  
                
                
            # Appending modified Graph    
            out.append(nx.Graph(G))
        
        # Returning output
        return(out)