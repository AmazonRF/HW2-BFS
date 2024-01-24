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
    
    start_node = list(tiny_graph_nx.nodes())[0]
    
    groundTruth = list(nx.bfs_edges(tiny_graph_nx, start_node))
    groundTruth = [start_node] + [v for u, v in groundTruth]

    my_bfs_path = tiny_graph_my.bfs(start_node)

    # with pytest.raises(ValueError):pass
    assert my_bfs_path == groundTruth

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
    pass
