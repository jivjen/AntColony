import networkx as nx
import matplotlib.pyplot as plt
import acopy
import numpy as np
from PrintingPlugin import PrintingPlugin 

G = nx.Graph()

# ADD YOUR ADJACENCY MATRIX HERE

# aa = np.matrix([[0, 3, 5, 7, 11, 13, 11], 
#                 [3, 0, 7, 11, 7, 15, 15], 
#                 [5, 7, 0, 3, 5, 16, 11], 
#                 [7, 11, 3, 0, 16, 5, 13], `
#                 [11, 7, 5, 16, 0, 7, 15], 
#                 [13, 15, 16, 5, 7, 0, 11], 
#                 [11, 15, 11, 13, 15, 11, 0]]) 

# aa = np.matrix([[0, 4, 4, 1, 1000, 1000, 5, 6, 1000, 1000, 1000, 1000, 1000], 
#                 [4, 0, 1, 5, 3, 1000, 1000, 1000, 3, 1000, 1000, 1000, 1000], 
#                 [4, 1, 0, 2, 1, 1000, 1000, 1000, 1000, 1000, 1000, 1, 1000], 
#                 [1, 5, 2, 0, 2, 1000, 1000, 1000, 3, 1000, 1000, 1000, 1000], 
#                 [1000, 3, 1, 2, 0, 1, 1, 1000, 4, 1000, 1000, 1000, 1000], 
#                 [1000, 1000, 1000, 1000, 1, 0, 1000, 4, 4, 1, 1000, 1000, 2], 
#                 [5, 1000, 1000, 1000, 1, 1000, 0, 3, 6, 1000, 1000, 1000, 1000], 
#                 [6, 1000, 1000, 1000, 1000, 4, 3, 0, 1000, 1000, 1000, 1000, 1000], 
#                 [1000, 3, 1000, 3, 4, 4, 6, 1000, 0, 1000, 3, 6, 1000], 
#                 [1000, 1000, 1000, 1000, 1000, 1, 1000, 1000, 1000, 0, 1000, 1000, 2], 
#                 [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 3, 1000, 0, 5, 1000], 
#                 [1000, 1000, 1, 1000, 1000, 1000, 1000, 1000, 6, 1000, 5, 0, 1000], 
#                 [1000, 1000, 1000, 1000, 1000, 2, 1000, 1000, 1000, 2, 1000, 1000, 0]])

aa = np.matrix([[0, 3, 2, 4, 5, 3, 5, 7, 11], 
                [3, 0, 5, 6, 2, 4, 4, 4, 1], 
                [2, 5, 0, 3, 1, 6, 3, 2, 4], 
                [4, 6, 3, 0, 1, 1, 1, 2, 4], 
                [5, 2, 1, 1, 0, 1, 4, 6, 3], 
                [3, 4, 6, 1, 1, 0, 1, 6, 5], 
                [5, 4, 3, 1, 4, 1, 0, 7, 2], 
                [7, 4, 2, 2, 6, 6, 7, 0, 5], 
                [11, 1, 4, 4, 3, 5, 2, 5, 0]])

G = nx.from_numpy_matrix(aa)


print(G)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=G.edges,
                       width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()

A = nx.adjacency_matrix(G)
adjacency_matrix = A.todense()
import acopy
solver = acopy.Solver(rho=.03, q=1)
colony = acopy.Colony(alpha=1, beta=3)

solver.add_plugin(PrintingPlugin(adjacency_matrix))

tour = solver.solve(G,colony,gen_size=90,limit = 500)
print("FINALLY")
print(tour)
print(tour.path)

