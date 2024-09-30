# # # CLI
# import numpy as np
# import math
# import networkx as nx
# import matplotlib.pyplot as plt
# from itertools import permutations
# class TspBruteForce:
#     def __init__(self, distanceMatrix, colleges):
#         self.distanceMatrix = distanceMatrix
#         self.colleges = colleges
#         self.numCities = len(distanceMatrix)
#     def calculateTotalDistance(self, route):
#         totalDistance = 0
#         for i in range(len(route) - 1):
#             totalDistance += self.distanceMatrix[route[i]][route[i + 1]]
#         totalDistance += self.distanceMatrix[route[-1]][route[0]]  # Return to start
#         return totalDistance
#     def solve(self):
#         minDistance = math.inf
#         optimalRoute = None
#         for perm in permutations(range(self.numCities)):
#             currentDistance = self.calculateTotalDistance(perm)
#             if currentDistance < minDistance:
#                 minDistance = currentDistance
#                 optimalRoute = perm
#         return optimalRoute, minDistance
# class TspGreedy:
#     def __init__(self, distanceMatrix, colleges):
#         self.distanceMatrix = distanceMatrix
#         self.colleges = colleges
#         self.numCities = len(distanceMatrix)
#     def findNearestCity(self, currentCity, unvisitedCities):
#         nearestCity = None
#         minDistance = float('inf')
#         for city in unvisitedCities:
#             if self.distanceMatrix[currentCity][city] < minDistance:
#                 minDistance = self.distanceMatrix[currentCity][city]
#                 nearestCity = city
#         return nearestCity
#     def solve(self, startCity=0):
#         visitedCities = [startCity]

#         unvisitedCities = set(range(self.numCities)) - {startCity}
#         totalDistance = 0
#         currentCity = startCity
#         while unvisitedCities:
#             nearestCity = self.findNearestCity(currentCity, unvisitedCities)
#             totalDistance += self.distanceMatrix[currentCity][nearestCity]
#             currentCity = nearestCity
#             visitedCities.append(currentCity)
#             unvisitedCities.remove(currentCity)
#         totalDistance += self.distanceMatrix[currentCity][startCity]  # Return to start
#         visitedCities.append(startCity)
#         return visitedCities, totalDistance
# def drawMainGraph(distanceMatrix, colleges):
#     numCities = len(distanceMatrix)
#     G = nx.Graph()
#     for i in range(numCities):
#         for j in range(i + 1, numCities):
#             G.add_edge(colleges[i], colleges[j], weight=distanceMatrix[i][j])
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True)
#     edge_labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#     plt.title("Distance Graph Between Colleges")
#     plt.show()
# def printRoute(route, distance, method, colleges):
#     route_str = " -> ".join(colleges[i] for i in route)
#     print(f"{method} Route: {route_str} | Total Distance: {distance}")
# if __name__ == "__main__":
#     numCities = int(input("Enter the number of colleges: "))
#     colleges = []
#     for i in range(numCities):
#         college_name = input(f"Enter the name of college {i + 1}: ")
#         colleges.append(college_name)
#     print("Enter the distance matrix (separated by spaces, row by row):")
#     distanceMatrix = []
#     for i in range(numCities):
#         row = list(map(int, input(f"Row {i + 1}: ").split()))
#         distanceMatrix.append(row)
#     drawMainGraph(distanceMatrix, colleges)

#     tspBruteForce = TspBruteForce(distanceMatrix, colleges)
#     bruteForceRoute, bruteForceMinDistance = tspBruteForce.solve()
#     printRoute(bruteForceRoute, bruteForceMinDistance, "Brute-Force", colleges)
#     tspGreedy = TspGreedy(distanceMatrix, colleges)
#     greedyRoute, greedyMinDistance = tspGreedy.solve(startCity=0)
#     printRoute(greedyRoute, greedyMinDistance, "Greedy", colleges)




# GUI
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class TspBruteForce:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_colleges = len(distance_matrix)
    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # Return to start
        return total_distance
    def solve(self):
        min_distance = math.inf
        optimal_route = None
        for perm in permutations(range(self.num_colleges)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                optimal_route = perm
        return optimal_route, min_distance
class TspGreedy:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_colleges = len(distance_matrix)
    def find_nearest_college(self, current_college, unvisited_colleges):
        nearest_college = None
        min_distance = float('inf')
        for college in unvisited_colleges:
            if self.distance_matrix[current_college][college] < min_distance:
                min_distance = self.distance_matrix[current_college][college]
                nearest_college = college
        return nearest_college
    def solve(self, start_college=0):
        visited_colleges = [start_college]
        unvisited_colleges = set(range(self.num_colleges)) - {start_college}
        total_distance = 0
        current_college = start_college
        while unvisited_colleges:
            nearest_college = self.find_nearest_college(current_college, unvisited_colleges)
            total_distance += self.distance_matrix[current_college][nearest_college]
            current_college = nearest_college
            visited_colleges.append(current_college)
            unvisited_colleges.remove(current_college)
        total_distance += self.distance_matrix[current_college][start_college]
        return visited_colleges, total_distance
    
def print_route(route, distance, algorithm_name, college_names):
    """Print the route and distance for a given algorithm."""
    route_str = " -> ".join(college_names[college] for college in route)
    return f"{algorithm_name} Route: {route_str}\nTotal Distance: {distance}\n"
def draw_route_graph(route, distance_matrix, college_names, algorithm_name, frame, start_college):
    num_colleges = len(route)
    college_positions = {i: (np.cos(2 * np.pi * i / num_colleges), np.sin(2 * np.pi * i / num_colleges)) for i in range(num_colleges)}
    G_route = nx.DiGraph()
    for i in range(len(route)):
        G_route.add_node(route[i], pos=college_positions[route[i]])
    for i in range(len(route) - 1):
        G_route.add_edge(route[i], route[i + 1], weight=distance_matrix[route[i]][route[i + 1]])
    G_route.add_edge(route[-1], route[0], weight=distance_matrix[route[-1]][route[0]])  # Return to start
    pos_route = nx.get_node_attributes(G_route, 'pos')
    fig, ax = plt.subplots(figsize=(6, 6))
    node_colors = ['lightblue' if node != start_college else 'orange' for node in G_route.nodes()]
    nx.draw(G_route, pos_route, with_labels=True, labels={i: college_names[i] for i in range(len(college_names))},
            node_color=node_colors, edge_color='gray', node_size=1000, font_size=12, ax=ax, arrows=True)
    edge_labels = {(route[i], route[i + 1]): f'{distance_matrix[route[i]][route[i + 1]]}' for i in range(len(route) - 1)}
    edge_labels[(route[-1], route[0])] = f'{distance_matrix[route[-1]][route[0]]}'
    nx.draw_networkx_edge_labels(G_route, pos_route, edge_labels=edge_labels, font_color='red', ax=ax)
    plt.title(f"{algorithm_name} Route")
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return canvas

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solution(Brute-Force & Greedy)")
        self.create_widgets()
    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Left frame for graphs
        self.graph_frame = tk.Frame(main_frame)
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        # Right frame for user inputs
        self.input_frame = tk.Frame(main_frame)
        self.input_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
        # Horizontal separator line
        separator = tk.Frame(main_frame, height=2, bg="black")
        separator.pack(side=tk.TOP, fill=tk.X)
        self.name_label = tk.Label(self.input_frame, text="Traveling Salesman Problem Solver Shiva", font=("Arial", 14), fg="blue")
        self.name_label.pack(side=tk.TOP, pady=10)
        self.num_colleges_label = tk.Label(self.input_frame, text="Enter number of colleges:")
        self.num_colleges_label.pack(side=tk.TOP)
        self.num_colleges_entry = tk.Entry(self.input_frame)
        self.num_colleges_entry.pack(side=tk.TOP)
        self.college_names_label = tk.Label(self.input_frame, text="Enter college names (comma-separated):")
        self.college_names_label.pack(side=tk.TOP)
        self.college_names_entry = tk.Entry(self.input_frame)
        self.college_names_entry.pack(side=tk.TOP)
        self.distance_matrix_label = tk.Label(self.input_frame, text="Enter the distance matrix (comma-separated rows):")
        self.distance_matrix_label.pack(side=tk.TOP)
        self.distance_matrix_entry = tk.Text(self.input_frame, height=10, width=40)
        self.distance_matrix_entry.pack(side=tk.TOP)
        self.solve_button = tk.Button(self.input_frame, text="Solve TSP", command=self.solve_tsp)
        self.solve_button.pack(side=tk.LEFT, pady=10)
        self.reset_button = tk.Button(self.input_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.RIGHT, pady=10)

        self.output_label = tk.Label(self.input_frame, text="", justify="left")
        self.output_label.pack(side=tk.TOP)
        self.canvas_brute_force = None
        self.canvas_greedy = None
    def solve_tsp(self):
        try:
            num_colleges = int(self.num_colleges_entry.get())
            college_names = self.college_names_entry.get().split(',')
            distance_matrix_input = self.distance_matrix_entry.get("1.0", tk.END).strip().splitlines()
            distance_matrix = [list(map(int, row.split(','))) for row in distance_matrix_input]
            if self.canvas_brute_force:
                self.canvas_brute_force.get_tk_widget().destroy()
            if self.canvas_greedy:
                self.canvas_greedy.get_tk_widget().destroy()
            tsp_brute_force = TspBruteForce(distance_matrix)
            brute_force_route, brute_force_min_distance = tsp_brute_force.solve()
            brute_force_result = print_route(brute_force_route, brute_force_min_distance, "Brute-Force", college_names)
            tsp_greedy = TspGreedy(distance_matrix)
            greedy_route, greedy_min_distance = tsp_greedy.solve(start_college=0)
            greedy_result = print_route(greedy_route, greedy_min_distance, "Greedy", college_names)
            self.output_label.config(text=brute_force_result + "\n" + greedy_result)
            start_college = 0
            self.canvas_brute_force = draw_route_graph(brute_force_route, distance_matrix, college_names, "Brute-Force", self.graph_frame, start_college)
            self.canvas_greedy = draw_route_graph(greedy_route, distance_matrix, college_names, "Greedy", self.graph_frame, start_college)
        except Exception as e:
            self.output_label.config(text=f"Error: {str(e)}")
    def reset(self):
        self.num_colleges_entry.delete(0, tk.END)
        self.college_names_entry.delete(0, tk.END)
        self.distance_matrix_entry.delete("1.0", tk.END)
        self.output_label.config(text="")
        if self.canvas_brute_force:
            self.canvas_brute_force.get_tk_widget().destroy()
            self.canvas_brute_force = None
        if self.canvas_greedy:
            self.canvas_greedy.get_tk_widget().destroy()
            self.canvas_greedy = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()