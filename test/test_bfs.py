# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc..)
    """
    tiny_graph_nx = nx.read_adjlist("./data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    tiny_graph_my = graph.Graph("./data/tiny_network.adjlist")
    
    ##### test breadth-first traversal ########
    start_node = list(tiny_graph_nx.nodes())[0]
    
    groundTruth = list(nx.bfs_edges(tiny_graph_nx, start_node))
    groundTruth = [start_node] + [v for u, v in groundTruth]

    my_bfs_path = tiny_graph_my.bfs(start_node)
    assert my_bfs_path == groundTruth

    ##### test not exist node ########
    start_node = 'Yifei Chen"
    my_bfs_path = tiny_graph_my.bfs(start_node)
    assert my_bfs_path == None

    ##### test empty graph ########
    tiny_graph_my = graph.Graph("./data/emptyGraph.adjlist")

    with pytest.raises(AttributeError):
        tiny_graph_my.node

    #question, if multi path?

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    tiny_graph_nx = nx.read_adjlist("/Users/yifeichen/Desktop/winter24/HW2-BFS/data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    tiny_graph_my = graph.Graph("/Users/yifeichen/Desktop/winter24/HW2-BFS/data/citation_network.adjlist")
    
    ##### connected ########
    
    start_node = 'Hani Goodarzi'
    end_node  = 'Lani Wu'

    my_bfs_path = tiny_graph_my.bfs(start_node,end_node)

    are_connected = nx.has_path(G, start_node, end_node)
    if are_connected:
        nx_path = nx.shortest_path_length(tiny_graph_nx, source=start_node, target=end_node)
        assert len(my_bfs_path) == nx_path
    else:
        nx_path = None
        assert my_bfs_path == nx_path

    

    ##### not connected ########
    start_node = '34356065'
    end_node  = '34970257'

    my_bfs_path = tiny_graph_my.bfs(start_node,end_node)

    are_connected = nx.has_path(G, start_node, end_node)
    if are_connected:
        nx_path = nx.shortest_path_length(tiny_graph_nx, source=start_node, target=end_node)
        assert len(my_bfs_path) == nx_path
    else:
        nx_path = None
        assert my_bfs_path == nx_path


