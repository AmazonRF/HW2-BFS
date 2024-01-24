import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
            """
            TODO: write a method that performs a breadth first traversal and pathfinding on graph G

            * If there's no end node input, return a list nodes with the order of BFS traversal
            * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
            * If there is an end node input and a path does not exist, return None

            start is assigned start node
            end is assigned end node, is optional, if end = None then traversal, if not find the shortest distance

            """
            graph_ = self.graph  #this variable stores the input graph
            
            if start not in graph_:
                return None  # Start node not in the graph
            if end not in graph_ and end != None:
                return None  # End node not in the graph

            visited = []
            save_level_node = []    #this variable save the save level node as the level order, basically this is my queue
            save_level_node.append(start)

            #1 child only can have 1 mom but 1 mom can have multi child, so in here child is keyword mom is value
            child_Mom = {start: None}

            while len(save_level_node)>0:
                # print(save_level_node)
                current_node = save_level_node.pop(0)
                if current_node not in visited:
                    visited.append(current_node)
                # print("!!",visited)


                if current_node == end:
                    path = []
                    while current_node is not None:
                        path.append(current_node)
                        #find mother
                        current_node = child_Mom[current_node]
                    return path[::-1]  #invert the order
                    

                for neighbor in graph_.neighbors(current_node):
                    if neighbor not in visited:
                        visited.append(neighbor)
                        save_level_node.append(neighbor)
                        child_Mom[neighbor] = current_node
            if current_node not in visited:
                visited.append(current_node)
            if end == None:
                return visited  # No end give
            else:
                return None  #No path exist
        
            





