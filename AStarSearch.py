from collections import namedtuple, deque

import PIL
from PIL import Image

import numpy as np

# Theta* algorithm
# Jump Point Search
#http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

class AStarSearch(object):

    def __init__(self):
        pass

class DijkstraSearch(object):

    def __init__(self):
        pass

class Graph(object):

    def __init__(self):
        pass

    # :   function Dijkstra(Graph, source):
    # 2:  for each vertex v in Graph:     // Initialization
    # 3:  dist[v] := infinity     // initial distance from source to vertex v is set to infinite
    # 4:  previous[v] := undefined    // Previous node in optimal path from source
    # 5:  dist[source] := 0   // Distance from source to source
    # 6:  Q := the set of all nodes in Graph  // all nodes in the graph are unoptimized - thus are in Q
    # 7:  while Q is not empty:   // main loop
    # 8:  u := node in Q with smallest dist[ ]
    # 9:  remove u from Q
    # 10:     for each neighbor v of u:   // where v has not yet been removed from Q.
    # 11:     alt := dist[u] + dist_between(u, v)
    # 12:     if alt < dist[v]    // Relax (u,v)
    # 13:     dist[v] := alt
    # 14:     previous[v] := u
    # 15:     return previous[ ] 

if __name__ == "__main__":


    inf = float('inf')
    Edge = namedtuple('Edge', 'start, end, cost')
     
    class Graph():
        def __init__(self, edges):
            self.edges = edges2 = [Edge(*edge) for edge in edges]
            self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
     
    def dijkstra(verts, edges, source, dest):
        assert source in verts
        dist = {vertex: inf for vertex in verts}
        previous = {vertex: None for vertex in verts}
        dist[source] = 0
        q = verts.copy()
        neighbours = {vertex: set() for vertex in verts}
        for start, end, cost in edges:
            neighbours[start].add((end, cost))
        #pp(neighbours)
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
        

    aStar = AStarSearch()

    connections = { 'A' : ['B', 'C'],
              'C' : ['A', 'B', 'D', 'E'],
              'D' : ['B', 'C', 'F'],
              'E' : ['C', 'F'],
              'F' : ['D', 'E']}

    weights = {'A' : [2, 3],
               'B' : [2, 3, 7],
               'C' : [3, 3, 1, 9],
               'D' : [7, 1, 4],
               'E' : [9, 1],
               'F' : [4, 1]}

    graph = Graph([("a", "b", 1),  ("b", "c", 2)])
    print(dijkstra(graph.vertices, graph.edges, "a", "c"))

    #print dijkstra(connections, weights, 'A', 'F')

    def find_path(graph, start, end, path=[]):
        path = path + [start]

        # Check it's not trivial
        if start == end:
            return path

        # Check the start node is in the graph
        if not graph.has_key(start):
            return None


        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath

        return None



    # graph = connections
    # print find_path(graph, 'A', 'F')


    im = PIL.Image.open("map.png")
    im = im.convert('1')
    im = im.resize((200, 200), PIL.Image.ANTIALIAS)
    pixels = list(im.getdata())
    im.show()
