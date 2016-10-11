import PIL
from PIL import Image
import numpy as np

class ImageHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def fixed_size_cell_decomposition(im):
        # Create the graph - find the 8- wise connected components - check fringes
        graph_list = []
        considered_nodes = [] # optimisation
        # Conevrt the image to a numpy array
        image_arr = np.array(im)
        for row, val in enumerate(image_arr):
            for col, val2 in enumerate(val):

                # |-------|
                # |a  b  c|
                # |d  *  e|
                # |f  g  h|
                # |-------|
                # a_coord = (row-1, col-1)
                # h_coord = (row+1, col+1)
                # The value of white space
                use_4_connection = True
                white_col = False
                if np.array_equal(image_arr[row, col], white_col):
                    node_name = str(row) + "," + str(col)
                    considered_nodes.append(node_name)
                    for x_i in range(row-1, row+2):
                        for y_i in range(col-1, col+2):
                            if (x_i, y_i) != (row, col):
                                # Check if they hit the edges
                                # Check if they're connected and add to graph
                                is_4_connected = ((x_i != row and y_i == col) or (x_i == row and y_i != col)) if use_4_connection else True
                                if(x_i >= 0 and x_i < image_arr.shape[1] and 
                                   y_i >= 0 and y_i < image_arr.shape[0] and
                                   is_4_connected):
                                    if np.array_equal(image_arr[x_i, y_i], white_col):
                                        inner_node_name = str(x_i) + "," + str(y_i)
                                        if inner_node_name not in considered_nodes:
                                            graph_list.append((node_name, inner_node_name, 1))
                elif np.array_equal(image_arr[row, col], np.array([0, 0, 0])):
                    pass
        return graph_list

        


if __name__ == "__main__":
    pass