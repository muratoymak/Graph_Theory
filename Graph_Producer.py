import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import numpy as np

def Graph_converter(number_of_vertices, probability_of_connectivity):
    edges_list_of_graph = []
    edges_list_of_complement_of_graph = []
    connectivity = [0, 1]
    list_of_vertices = []
    p = []
    p.append(1 - probability_of_connectivity)
    p.append(probability_of_connectivity)
    for i in range(1, number_of_vertices + 1):
        list_of_vertices.append(i)
        for j in range(i + 1, number_of_vertices + 1):
            connectivity_value = np.random.choice(connectivity, p=p)
            if connectivity_value == 1:
                edges_list_of_graph.append((i, j))
            elif connectivity_value == 0:
                edges_list_of_complement_of_graph.append((i,j))
    G_1 = nx.Graph()
    G_1.add_nodes_from(list_of_vertices)
    G_1.add_edges_from(edges_list_of_graph)
    G_2 = nx.Graph()
    G_2.add_nodes_from(list_of_vertices)
    G_2.add_edges_from(edges_list_of_complement_of_graph)
    return G_1, G_2

def Graph_illustrator(Graph_G, number_of_vertices):
    plt.figure(figsize=(number_of_vertices, number_of_vertices))
    nx.draw(Graph_G, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=15)
    plt.show()

def Graph_Complement_illustrator(Graph_G, number_of_vertices):
    plt.figure(figsize=(number_of_vertices, number_of_vertices))
    nx.draw(Graph_G, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=15)
    plt.show()

#Show a basic interface
print(30*"*")
print("Welcome the graph producer!!!")

while True:
    n = input("Please enter 'E' to exit\nIn order to continue, enter the number of nodes n: ")
    if n == 'E':
        print("Finished.")
        break
    try:
        n = int(n)
        probability = float(eval(input("Enter the probability of connectivity: ")))
        if not (probability <= 1 and probability >= 0):
            print("Probability out of range error!!!")
            continue
    except:
        print("Please enter a valid node number!")
        continue

    our_graph, complement_of_graph = Graph_converter(n, probability)
    Graph_illustrator(our_graph, n)
    Graph_Complement_illustrator(complement_of_graph, n)

