import pytest

from Search import dfs

@pytest.mark.parametrize('graph, node, expected',
    [
        ({'A': (['B', 'C']),
         'B': (['A', 'D', 'E']),
         'C': (['A', 'F']),
         'D': (['B']),
         'E': (['B', 'F']),
         'F': (['C', 'E'])},'Q','error')
    ])
def test_NonExistent_Node(graph, node, expected):
    assert str (dfs(graph,node)) == expected

@pytest.mark.parametrize('graph, node, expected',
    [
        ({'A': (['B', 'C']),
         'B': (['A', 'D', 'E']),
         'C': (['A', 'F']),
         'D': (['B'])},'F','error')
    ])
def test_Unconnected_Node(graph, node, expected):
    assert str (dfs(graph,node)) == expected

@pytest.mark.parametrize('graph, node, expected',
    [
        ({'A': (['A'])},'A','error')
    ])
def test_Endless_Graph(graph, node, expected):
    assert str (dfs(graph,node)) == expected

def test_docs():
    assert open('DOCS.md') != None

def test_license():
    assert open('LICENSE') != None

@pytest.mark.parametrize('graph, node, expected',
    [
        ({} ,'A','error')
    ])
def test_Empty_Graph(graph, node, expected):
    assert str (dfs(graph,node)) == expected

@pytest.mark.parametrize('graph, node, expected',
    [
        ({'A': (['A']),'B':(['A'])},'A','error')
    ])
def test_Couple_Vertex(graph, node, expected):
    assert str (dfs(graph,node)) == expected

@pytest.mark.parametrize('graph, node, expected',
    [
        ({'A': (['A']),'B':(['A'])},123,'error')
    ])
def test_Incorrect_Data(graph, node, expected):
    assert str (dfs(graph,node)) == expected