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


if __name__ == "__main__":
    aStar = AStarSearch()
    graph = { 'A' : ['B'],
              'B' : ['C']}

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

    print find_path(graph, 'A', 'C')