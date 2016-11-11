from collections import deque

class Search(object):
    
    def __init__(self):
        pass

    @staticmethod
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

    # Theta* algorithm
    # Jump Point Search
    #http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
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
    @staticmethod
    def dijkstra(verts, edges, source, dest):
        inf = float('inf')
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
                if alt < dist[v]:   # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

# A STAR PSEUDOCODE
# TODO: Implement!
# function A*(start, goal)
#     // The set of nodes already evaluated.
#     closedSet := {}
#     // The set of currently discovered nodes still to be evaluated.
#     // Initially, only the start node is known.
#     openSet := {start}
#     // For each node, which node it can most efficiently be reached from.
#     // If a node can be reached from many nodes, cameFrom will eventually contain the
#     // most efficient previous step.
#     cameFrom := the empty map

#     // For each node, the cost of getting from the start node to that node.
#     gScore := map with default value of Infinity
#     // The cost of going from start to start is zero.
#     gScore[start] := 0 
#     // For each node, the total cost of getting from the start node to the goal
#     // by passing by that node. That value is partly known, partly heuristic.
#     fScore := map with default value of Infinity
#     // For the first node, that value is completely heuristic.
#     fScore[start] := heuristic_cost_estimate(start, goal)

#     while openSet is not empty
#         current := the node in openSet having the lowest fScore[] value
#         if current = goal
#             return reconstruct_path(cameFrom, current)

#         openSet.Remove(current)
#         closedSet.Add(current)
#         for each neighbor of current
#             if neighbor in closedSet
#                 continue        // Ignore the neighbor which is already evaluated.
#             // The distance from start to a neighbor
#             tentative_gScore := gScore[current] + dist_between(current, neighbor)
#             if neighbor not in openSet  // Discover a new node
#                 openSet.Add(neighbor)
#             else if tentative_gScore >= gScore[neighbor]
#                 continue        // This is not a better path.

#             // This path is the best until now. Record it!
#             cameFrom[neighbor] := current
#             gScore[neighbor] := tentative_gScore
#             fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)

#     return failure

# function reconstruct_path(cameFrom, current)
#     total_path := [current]
#     while current in cameFrom.Keys:
#         current := cameFrom[current]
#         total_path.append(current)
#     return total_path
