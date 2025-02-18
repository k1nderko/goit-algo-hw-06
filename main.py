import networkx as nx
import matplotlib.pyplot as plt

# Завдання 1: Створення графа (модель метро)
G = nx.Graph()

# Додаємо вершини (станції метро)
stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(stations)

# Додаємо ребра (сполучення між станціями) з вагами
edges = [
    ("A", "B", 2), ("A", "C", 5),
    ("B", "D", 3), ("B", "E", 4),
    ("C", "F", 6),
    ("D", "G", 2), ("E", "G", 1),
    ("F", "H", 3), ("G", "H", 4)
]
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
edge_labels = {(u, v): w for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Метро міста")
plt.show()

# Аналіз графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))

# Завдання 2: DFS і BFS
start_node = "A"

# DFS
dfs_path = list(nx.dfs_preorder_nodes(G, source=start_node))
print("DFS обхід:", dfs_path)

# BFS
bfs_path = list(nx.bfs_tree(G, source=start_node))
print("BFS обхід:", bfs_path)

# Завдання 3: Алгоритм Дейкстри
shortest_paths = {}
for target in G.nodes():
    if target != start_node:
        path = nx.dijkstra_path(G, start_node, target, weight='weight')
        length = nx.dijkstra_path_length(G, start_node, target, weight='weight')
        shortest_paths[target] = (path, length)

print("Найкоротші шляхи від A:")
for target, (path, length) in shortest_paths.items():
    print(f"До {target}: Шлях - {path}, Довжина - {length}")
