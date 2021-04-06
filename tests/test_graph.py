import pytest
from challenges.graph.graph import Vertex, Graph, Edge


def test_Graph_exits():
    assert Graph


def test_Vertex_exits():
    assert Vertex


def test_Edge_exits():
    assert Edge


def test_create_graph():
    graph = Graph
    assert graph 


def test_add_vertex_pass():
    vertex = Vertex('a')
    actual =vertex.value
    expected = 'a'
    assert actual == expected


def test_add_vertex_fail():
    vertex = Vertex('a')
    actual =vertex.value
    expected = 'b'
    assert actual != expected


def test_add_vertex():
    graph = Graph()
    expected = 'a'
    actual = graph.add_vertex('a').value
    assert expected == actual

def test_add_edge_true():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    graph.add_edge(a, b)
    assert True

def test_size():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    expected = 2
    actual = graph.size()
    assert actual == expected

def test_size_fail():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    expected = 3
    actual = graph.size()
    assert actual != expected


def test_get_vertices():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    graph.add_edge(a, b, 11)
    actual = graph.get_vertices()
    assert actual == ['a', 'b']


def test_get_vertices_multiple():
    trip = Graph()
    city1 = trip.add_vertex('Seattle')
    city2 = trip.add_vertex('Portland')
    city3 = trip.add_vertex('San Francisco')
    city4 = trip.add_vertex('Salt Lake City')
    city5 = trip.add_vertex('Spokane')
    trip.add_edge(city1, city2, 11)
    trip.add_edge(city2, city3, 12)
    trip.add_edge(city3, city4, 13)
    trip.add_edge(city4, city5, 14)
    trip.add_edge(city5, city1, 15)
    actual = trip.get_vertices()
    assert actual == ['Seattle', 'Portland', 'San Francisco', 'Salt Lake City', 'Spokane']