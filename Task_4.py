import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Binary Heap Implementation
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def build_tree(self):
        if not self.heap:
            return None

        nodes = [Node(key) for key in self.heap]
        for i in range(len(self.heap)):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(self.heap):
                nodes[i].left = nodes[left_index]
            if right_index < len(self.heap):
                nodes[i].right = nodes[right_index]
        return nodes[0]


def visualize_binary_heap(heap):
    tree_root = heap.build_tree()
    if tree_root:
        draw_tree(tree_root)
    else:
        print("Heap is empty")

heap = BinaryHeap()
elements = [15, 10, 20, 8, 12, 25]
for element in elements:
    heap.insert(element)

visualize_binary_heap(heap)
