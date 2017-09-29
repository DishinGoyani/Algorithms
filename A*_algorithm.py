"""
Created on Fri Sep 29 14:23:56 2017

A* (stric) Algorithm

"""

# Graph Structure : Start

# Store successor of each node
graph = {
          'S' : ['A','B'],
	  'A' : ['B','C','D'],
          'B' : ['C'],
          'C' : ['D'],
          'D' : []
        }
        
# Store successor cost of each node
graph_cost = {
          'S' : [1,4],
	  'A' : [2,5,12],
          'B' : [2],
          'C' : [3],
          'D' : []
        }

# Store heuristic value of each node
heuristic_val = {
        'S':7, 'A':6, 'B':2, 'C':1, 'D':0
        }
# Graph Structure : End

# optimam_path_pop Function  : Start    
def optimam_path_pop(open_list):
    """ Find Optimam path based on Fscore value and also pop(remove) it from 
        open list. """
    
    # Take first path as a optimam for comparisan from open list
    min_path = open_list[0]
    min_index = 0
    
    # Take one-by-one path from open list and compare it's heuristic value
    # Heuristic value store at last position of each path(ex. min_path[-1])
    for index,value in enumerate(open_list):
        if min_path[-1] > value[-1]:
            min_path, min_index = value, index;

    # return optimal path and pop from open list        
    return open_list.pop(min_index)
# optimam_path_pop Function  : End


# A_stric Function  : Start
def A_stric(graph, graph_cost, heuristic_val, start, goal):
    """ A_stric Function is Find Out Most optimam path from graph
        by Apply A* algorithm """
    
    # Fscore cost Function : Start inner function
    def Fscore(path):
        """ Fscore Function To find F(n) = g(n)+h(n) Total cost
            for given path """
        
        cost = 0
        # Find total cost For all nodes in path
        for i in range( len(path)-2 ):
            index = graph[path[i]].index(path[i+1])
            cost += graph_cost[path[i]][index]
        # return Fscore = total cost + heuristic value    
        return cost + heuristic_val[path[-2]]
    # Fscore cost Function : End
    
    
    # Initialize open_list with start node
    open_list = [[start,0]]
    node = optimam_path_pop(open_list)

    # Check current optimam path is goal if not expand successor node and
    # add into open list
    while node[-2] != goal:
        # Expand successor and store it to open_list
        print('successor : ' + str(graph[node[-2]]))
        print()
        for i in graph[node[-2]]:
            # Temporary node to find it's Fscore value
            node_t = list(node)
            node_t.insert(-1,i)
            
            # call Fscore() Function
            f_value = Fscore(node_t)
            
            # store fvalue in temporary node last position of list
            node_t[-1] = f_value
            
            
            # add successor to openlist with Fscore
            open_list.append(node_t)
            print('Openlist Add - ' + str(i) +' : '+ str(open_list))
        
        # Find new optimal path from openlist
        node = optimam_path_pop(open_list)
        print()
        print('Expand : '+ str(node))
        print()
        print('--------------------------------------------------')
        print()
        
    # if optimal goal path is found return path
    print('------------------- Optimal Path -----------------')
    return node
# A_stric Function  : End
            
# call A_stric function
print('\t   ' + str(A_stric(graph, graph_cost, heuristic_val, 'S', 'D')))
