# # CLI
# class Graph:
#     def __init__(self):
#         # Initialize an empty dictionary to store the adjacency list
#         self.graph = {}

#     def add_vertex(self):
#         """Prompt the user to input a vertex to add to the graph."""
#         vertex = input("Enter the vertex to add: ")
#         if vertex not in self.graph:
#             self.graph[vertex] = []
#             print(f"Vertex {vertex} added.")
#         else:
#             print(f"Vertex {vertex} already exists.")

#     def remove_vertex(self):
#         """Prompt the user to input a vertex to remove from the graph."""
#         vertex = input("Enter the vertex to remove: ")
#         if vertex in self.graph:
#             # Remove all edges to this vertex from other vertices
#             for adjacent in list(self.graph[vertex]):
#                 self.graph[adjacent].remove(vertex)
#             # Remove the vertex from the graph
#             del self.graph[vertex]
#             print(f"Vertex {vertex} removed.")
#         else:
#             print(f"Vertex {vertex} does not exist.")

#     def add_edge(self):
#         """Prompt the user to input two vertices and add an undirected edge between them."""
#         vertex1 = input("Enter the first vertex: ")
#         vertex2 = input("Enter the second vertex: ")
#         if vertex1 in self.graph and vertex2 in self.graph:
#             if vertex2 not in self.graph[vertex1]:
#                 self.graph[vertex1].append(vertex2)
#             if vertex1 not in self.graph[vertex2]:
#                 self.graph[vertex2].append(vertex1)
#             print(f"Edge between {vertex1} and {vertex2} added.")
#         else:
#             print("One or both vertices not found.")

#     def remove_edge(self):
#         """Prompt the user to input two vertices and remove the edge between them."""
#         vertex1 = input("Enter the first vertex: ")
#         vertex2 = input("Enter the second vertex: ")
#         if vertex1 in self.graph and vertex2 in self.graph:
#             if vertex2 in self.graph[vertex1]:
#                 self.graph[vertex1].remove(vertex2)
#             if vertex1 in self.graph[vertex2]:
#                 self.graph[vertex2].remove(vertex1)
#             print(f"Edge between {vertex1} and {vertex2} removed.")
#         else:
#             print("One or both vertices not found.")

#     def display(self):
#         """Display the adjacency list of the graph."""
#         for vertex, edges in self.graph.items():
#             print(f"{vertex}: {edges}")

# # Example usage
# if __name__ == "__main__":
#     g = Graph()
    
#     while True:
#         print("\nMenu:")
#         print("1. Add Vertex")
#         print("2. Remove Vertex")
#         print("3. Add Edge")
#         print("4. Remove Edge")
#         print("5. Display Graph")
#         print("6. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             g.add_vertex()
#         elif choice == '2':
#             g.remove_vertex()
#         elif choice == '3':
#             g.add_edge()
#         elif choice == '4':
#             g.remove_edge()
#         elif choice == '5':
#             g.display()
#         elif choice == '6':
#             break
#         else:
#             print("Invalid choice. Please try again.")



# GUI
import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        try:
            if vertex not in self.graph:
                self.graph[vertex] = {}
                return f"Vertex {vertex} added."
            else:
                return f"Vertex {vertex} already exists."
        except Exception as e:
            return f"Error adding vertex: {e}"

    def remove_vertex(self, vertex):
        try:
            if vertex in self.graph:
                for adjacent in list(self.graph[vertex]):
                    del self.graph[adjacent][vertex]
                del self.graph[vertex]
                return f"Vertex {vertex} removed."
            else:
                return f"Vertex {vertex} does not exist."
        except Exception as e:
            return f"Error removing vertex: {e}"

    def add_edge(self, vertex1, vertex2, weight):
        try:
            if vertex1 in self.graph and vertex2 in self.graph:
                self.graph[vertex1][vertex2] = weight
                self.graph[vertex2][vertex1] = weight
                return f"Edge between {vertex1} and {vertex2} with weight {weight} added."
            else:
                return "One or both vertices not found."
        except Exception as e:
            return f"Error adding edge: {e}"

    def remove_edge(self, vertex1, vertex2):
        try:
            if vertex1 in self.graph and vertex2 in self.graph:
                if vertex2 in self.graph[vertex1]:
                    del self.graph[vertex1][vertex2]
                if vertex1 in self.graph[vertex2]:
                    del self.graph[vertex2][vertex1]
                return f"Edge between {vertex1} and {vertex2} removed."
            else:
                return "One or both vertices not found."
        except Exception as e:
            return f"Error removing edge: {e}"

    def display(self):
        try:
            result = ""
            for vertex, edges in self.graph.items():
                result += f"{vertex}: {edges}\n"
            return result
        except Exception as e:
            return f"Error displaying graph: {e}"

    def visualize(self, highlighted_edges=None, highlighted_nodes=None):
        """Visualize the graph with optional highlighted nodes and edges."""
        try:
            G = nx.Graph()
            for vertex, edges in self.graph.items():
                for adjacent, weight in edges.items():
                    G.add_edge(vertex, adjacent, weight=weight)

            pos = nx.spring_layout(G)
            plt.figure(figsize=(8, 6))
            nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15, font_weight='bold')

            if highlighted_edges:
                nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, edge_color='red', width=2)
            if highlighted_nodes:
                nx.draw_networkx_nodes(G, pos, nodelist=highlighted_nodes, node_color='orange', node_size=2000)

            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            plt.title("Graph Visualization", fontsize=18)
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error visualizing graph: {e}")

    def bfs(self, start_vertex):
        """Perform BFS traversal from a given start vertex."""
        try:
            visited = set()
            queue = deque([start_vertex])
            bfs_order = []
            highlighted_edges = []

            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    bfs_order.append(vertex)
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            highlighted_edges.append((vertex, neighbor))

            self.visualize(highlighted_edges=highlighted_edges, highlighted_nodes=bfs_order)
            return " -> ".join(bfs_order)
        except Exception as e:
            return f"Error performing BFS: {e}"

    def dfs(self, start_vertex):
        """Perform DFS traversal from a given start vertex."""
        try:
            visited = set()
            stack = [start_vertex]
            dfs_order = []
            highlighted_edges = []

            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    dfs_order.append(vertex)
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            highlighted_edges.append((vertex, neighbor))

            self.visualize(highlighted_edges=highlighted_edges, highlighted_nodes=dfs_order)
            return " -> ".join(dfs_order)
        except Exception as e:
            return f"Error performing DFS: {e}"

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weighted Graph GUI")
        self.graph = Graph()

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.graph_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Graph", menu=self.graph_menu)

        self.graph_menu.add_command(label="Add Vertex", command=self.add_vertex)
        self.graph_menu.add_command(label="Remove Vertex", command=self.remove_vertex)
        self.graph_menu.add_command(label="Add Edge", command=self.add_edge)
        self.graph_menu.add_command(label="Remove Edge", command=self.remove_edge)
        self.graph_menu.add_separator()
        self.graph_menu.add_command(label="Display Graph", command=self.display_graph)
        self.graph_menu.add_command(label="Visualize Graph", command=self.visualize_graph)
        self.graph_menu.add_separator()
        self.graph_menu.add_command(label="BFS", command=self.perform_bfs)
        self.graph_menu.add_command(label="DFS", command=self.perform_dfs)
        self.graph_menu.add_separator()
        self.graph_menu.add_command(label="Exit", command=root.quit)

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=20)

    def add_vertex(self):
        try:
            vertex = simpledialog.askstring("Input", "Enter the vertex to add:")
            if vertex:
                result = self.graph.add_vertex(vertex)
                self.output_text.insert(tk.END, result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding vertex: {e}")

    def remove_vertex(self):
        try:
            vertex = simpledialog.askstring("Input", "Enter the vertex to remove:")
            if vertex:
                result = self.graph.remove_vertex(vertex)
                self.output_text.insert(tk.END, result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error removing vertex: {e}")

    def add_edge(self):
        try:
            vertex1 = simpledialog.askstring("Input", "Enter the first vertex:")
            vertex2 = simpledialog.askstring("Input", "Enter the second vertex:")
            weight = simpledialog.askstring("Input", "Enter the weight of the edge:")
            if vertex1 and vertex2 and weight:
                try:
                    weight = float(weight)  # Convert weight to a float
                    result = self.graph.add_edge(vertex1, vertex2, weight)
                    self.output_text.insert(tk.END, result + "\n")
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter a valid number for the weight.")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding edge: {e}")

    def remove_edge(self):
        try:
            vertex1 = simpledialog.askstring("Input", "Enter the first vertex:")
            vertex2 = simpledialog.askstring("Input", "Enter the second vertex:")
            if vertex1 and vertex2:
                result = self.graph.remove_edge(vertex1, vertex2)
                self.output_text.insert(tk.END, result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error removing edge: {e}")

    def display_graph(self):
        try:
            result = self.graph.display()
            self.output_text.insert(tk.END, "Graph:\n" + result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying graph: {e}")

    def visualize_graph(self):
        try:
            self.graph.visualize()
        except Exception as e:
            messagebox.showerror("Error", f"Error visualizing graph: {e}")

    def perform_bfs(self):
        try:
            start_vertex = simpledialog.askstring("Input", "Enter the start vertex for BFS:")
            if start_vertex:
                result = self.graph.bfs(start_vertex)
                self.output_text.insert(tk.END, "BFS Traversal:\n" + result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error performing BFS: {e}")

    def perform_dfs(self):
        try:
            start_vertex = simpledialog.askstring("Input", "Enter the start vertex for DFS:")
            if start_vertex:
                result = self.graph.dfs(start_vertex)
                self.output_text.insert(tk.END, "DFS Traversal:\n" + result + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error performing DFS: {e}")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = GraphApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error running application: {e}")



# # BFS CLI
# from collections import deque, defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.graph and vertex2 in self.graph:
#             self.graph[vertex1].append(vertex2)
#             self.graph[vertex2].append(vertex1)

#     def bfs_tree(self, start):
#         """Perform BFS and return the Breadth-First Tree as a dictionary."""
#         visited = set()
#         bfs_tree = defaultdict(list)
#         queue = deque([start])
#         visited.add(start)

#         while queue:
#             current = queue.popleft()
#             for neighbor in self.graph[current]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     bfs_tree[current].append(neighbor)
#                     queue.append(neighbor)

#         return bfs_tree

#     def display(self):
#         for vertex, edges in self.graph.items():
#             print(f"{vertex}: {edges}")

# def print_bfs_tree(bfs_tree, start):
#     """Print the Breadth-First Tree."""
#     print(f"Breadth-First Tree starting from {start}:")
#     for vertex in bfs_tree:
#         print(f"{vertex}: {bfs_tree[vertex]}")

# # Example usage
# if __name__ == "__main__":
#     g = Graph()

#     # Add vertices
#     for v in ['A', 'B', 'C', 'D', 'E', 'F']:
#         g.add_vertex(v)

#     # Add edges
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     g.add_edge('B', 'E')
#     g.add_edge('C', 'F')

#     print("Graph:")
#     g.display()

#     # Perform BFS and get the Breadth-First Tree
#     start_vertex = 'A'
#     bfs_tree = g.bfs_tree(start_vertex)

#     print_bfs_tree(bfs_tree, start_vertex)




# # DFS CLI
# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.graph and vertex2 in self.graph:
#             self.graph[vertex1].append(vertex2)
#             self.graph[vertex2].append(vertex1)

#     def dfs_tree(self, start):
#         """Perform DFS and return the Depth-First Tree as a dictionary."""
#         visited = set()
#         dfs_tree = defaultdict(list)

#         def dfs(v):
#             visited.add(v)
#             for neighbor in self.graph[v]:
#                 if neighbor not in visited:
#                     dfs_tree[v].append(neighbor)
#                     dfs(neighbor)

#         dfs(start)
#         return dfs_tree

#     def display(self):
#         for vertex, edges in self.graph.items():
#             print(f"{vertex}: {edges}")

# def print_dfs_tree(dfs_tree, start):
#     """Print the Depth-First Tree."""
#     print(f"Depth-First Tree starting from {start}:")
#     for vertex in dfs_tree:
#         print(f"{vertex}: {dfs_tree[vertex]}")

# # Example usage
# if __name__ == "__main__":
#     g = Graph()

#     # Add vertices
#     for v in ['A', 'B', 'C', 'D', 'E', 'F']:
#         g.add_vertex(v)

#     # Add edges
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     g.add_edge('B', 'E')
#     g.add_edge('C', 'F')

#     print("Graph:")
#     g.display()

#     # Perform DFS and get the Depth-First Tree
#     start_vertex = 'A'
#     dfs_tree = g.dfs_tree(start_vertex)

#     print_dfs_tree(dfs_tree, start_vertex)