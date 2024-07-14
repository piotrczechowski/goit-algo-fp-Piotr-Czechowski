import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Default color for nodes

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val)  # Add node to the graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes, color_map):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [color_map.get(node, '#1296F0') for node in tree.nodes()]  # Default color if not visited

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_search(node, visited_nodes, color_map, current_color_index, color_palette):
    if node:
        visited_nodes.add(node.val)
        color_map[node.val] = color_palette[current_color_index]
        draw_tree(root, visited_nodes, color_map)
        current_color_index += 1

        depth_first_search(node.left, visited_nodes, color_map, current_color_index, color_palette)
        depth_first_search(node.right, visited_nodes, color_map, current_color_index, color_palette)

def breadth_first_search(root, visited_nodes, color_map, color_palette):
    queue = deque([root])
    current_color_index = 0

    while queue:
        node = queue.popleft()
        if node:
            visited_nodes.add(node.val)
            color_map[node.val] = color_palette[current_color_index]
            draw_tree(root, visited_nodes, color_map)
            current_color_index += 1

            queue.append(node.left)
            queue.append(node.right)

def generate_color_palette(num_colors):
    color_palette = []
    for i in range(num_colors):
        r = int(18 + (255 - 18) * (i / num_colors))
        g = int(150 + (255 - 150) * (i / num_colors))
        b = int(240 + (255 - 240) * (i / num_colors))
        color = f'#{r:02x}{g:02x}{b:02x}'
        color_palette.append(color)
    return color_palette

# Creating the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Displaying DFS
visited_nodes = set()
color_map = {}
color_palette = generate_color_palette(6)
print("Depth-First Search Traversal:")
depth_first_search(root, visited_nodes, color_map, 0, color_palette)

# Reset for BFS
visited_nodes = set()
color_map = {}
print("Breadth-First Search Traversal:")
breadth_first_search(root, visited_nodes, color_map, color_palette)
