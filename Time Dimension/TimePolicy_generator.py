import networkx as nx
import random

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

############################
def TimePolicy_generator(Graph,Maximum_Time=10000,
    method = {'name':'','divide':{'group_num':2},'node_centrality':{'how':'degree','prc':10,'group_num':2}}):
    
    # Size of Graph
    lng = Graph.number_of_nodes()
    
    Nodes_dict =  dict(Graph.nodes(data=True))
    Nodes_list = list(Nodes_dict)
    
    if method['name'] is 'divide':
        # Assigning groups
        random.shuffle(Nodes_list)
        group_num = method['divide']['group_num']
        List = chunkIt(Nodes_list, group_num)
        group_node = {k:v for (k,v) in zip(list(range(1,group_num+1)),List)}
        
        time_node = {k:set(group_node[i%group_num+1]) for (k,i) in zip(list(range(1,Maximum_Time+1)),list(range(1,Maximum_Time+1)))}
        return(time_node)
    
    elif method['name'] is 'node_centrality':
        Dict = method['node_centrality']
        how = Dict['how']
        prc = Dict['prc']
        group_num = Dict['group_num']
        
        func_centrality = {'degree':nx.degree_centrality,'eigen':nx.eigenvector_centrality}
        sorted_cen = sorted(func_centrality[how](Graph).items(), key=lambda item: item[1],reverse=True)
        central_nodes = [x[0] for x in sorted_cen[0:int(prc/100*len(sorted_cen))]]

        Nodes_list_updated = [x for x in Nodes_list if x not in central_nodes]
        random.shuffle(Nodes_list_updated)
        List = chunkIt(Nodes_list_updated, group_num)
        group_node = {k:v for (k,v) in zip(list(range(1,group_num+1)),List)}
        time_node_temp = {k:set(group_node[i%group_num+1]) for (k,i) in zip(list(range(1,Maximum_Time+1)),list(range(1,Maximum_Time+1)))}
        time_node = {x[0]:x[1].union(central_nodes) for x in time_node_temp.items()}
        return(time_node)
        
    else:
        raise ValueError('Wrong input for method["name"]!')
    