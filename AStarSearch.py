import PIL
from PIL import Image

import numpy as np

from graph import Graph
from search import Search
from image import ImageHandler



if __name__ == "__main__":

    im = PIL.Image.open("input-images/mark_maze_2.png")
    im_orig = im.convert('RGB')
    #im = im.convert('1')
    # im = im.resize((100, 100), PIL.Image.ANTIALIAS)

    graph_list = ImageHandler.fixed_size_cell_decomposition(im)
    graph = Graph(graph_list)

    display_image = np.array(im_orig)
    result = Search.dijkstra(graph.vertices, graph.edges, "0,0", "149,149")

    for node in result:
        print node
        x,y = node.split(",")
        x = int(x)
        y =  int(y)
        print("X, Y: {}, {}").format(x,y)
        display_image[x,y] = (255, 0, 0)
    
    im2 = Image.fromarray(display_image)
    im2.save("test.png")
    im2.show()
