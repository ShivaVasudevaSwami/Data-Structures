# CLI
import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Create a heap with nodes for each character
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Merge nodes until only one tree remains
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Remove the node with the smallest frequency
        right = heapq.heappop(heap)  # Remove the next smallest frequency
        merged = Node(freq=left.freq + right.freq)  # Create a new node with the sum of both frequencies
        merged.left = left  # Assign the left child
        merged.right = right  # Assign the right child
        heapq.heappush(heap, merged)  # Push the merged node back into the heap

    return heap[0]  # Return the root of the Huffman tree

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix  # Assign code to character
        generate_codes(node.left, prefix + "0", codebook)  # Traverse left with "0"
        generate_codes(node.right, prefix + "1", codebook)  # Traverse right with "1"
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)  # Count frequencies of each character
    root = build_huffman_tree(frequencies)  # Build Huffman tree
    codebook = generate_codes(root)  # Generate Huffman codes
    encoded_data = ''.join(codebook[char] for char in data)  # Encode the data

    return encoded_data, codebook

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}  # Reverse codebook for decoding
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit  # Build current code
        if current_code in reverse_codebook:  # If code matches a character
            decoded_data += reverse_codebook[current_code]  # Decode character
            current_code = ""  # Reset current code

    return decoded_data

# Example usage
if __name__ == "__main__":
    data = input("Enter the data to be encoded: ")  # Take input from the user
    print("Original data:", data)

    encoded_data, codebook = huffman_encoding(data)
    print("Encoded data:", encoded_data)
    print("Codebook:", codebook)

    decoded_data = huffman_decoding(encoded_data, codebook)
    print("Decoded data:", decoded_data)





# GUI
# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
from collections import Counter
import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

# Function to generate Huffman codes
def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# Huffman encoding function
def huffman_encoding(data):
    if not data:
        return "", {}, None
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook, root

# Huffman decoding function
def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""
    return decoded_data

# Calculate the size of the data
def calculate_size(data):
    return len(data) * 8

# Calculate the compression difference
def calculate_compression_difference(original_data, encoded_data):
    original_size = calculate_size(original_data)
    compressed_size = len(encoded_data)
    difference = original_size - compressed_size
    return original_size, compressed_size, difference

# Calculate spacing for tree nodes
def calculate_spacing(node_count):
    base_dx = 100
    base_dy = 60
    root_child_dy = 80
    if node_count <= 20:
        dx = base_dx
        dy = base_dy
        root_child_dy = 80
    elif node_count <= 50:
        dx = base_dx * (node_count ** 1.5)
        dy = base_dy
        root_child_dy = base_dy + (node_count ** 0.5)
    elif node_count <= 100:
        dx = base_dx * (node_count ** 2)
        dy = base_dy
        root_child_dy = base_dy + (node_count ** 0.7)
    else:
        dx = base_dx * (node_count ** 2.5)
        dy = base_dy
        root_child_dy = base_dy + (node_count ** 0.8)
    dx = min(max(dx, 150), 1500)
    dy = min(max(dy, 60), 1000)
    return dx, dy, root_child_dy

# Draw the Huffman tree on canvas
def draw_tree(canvas, node, x, y, dx, dy, root_child_dy, level=0):
    if node is not None:
        node_color = "lightgreen" if node.char is not None else "lightblue"
        node_text = f'{node.char}' if node.char else f'{node.freq}'
        node_radius = 15
        canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill=node_color, outline="black", width=2)
        canvas.create_text(x, y, text=node_text, fill="black", font=("Arial", 10, "bold"))
        if node.left:
            left_x = x - dx
            left_y = y + (root_child_dy if level == 0 else dy)
            canvas.create_line(x, y + node_radius, left_x, left_y - node_radius, arrow=tk.LAST, fill="blue", width=2)
            canvas.create_text((x + left_x) / 2, (y + left_y) / 2, text="0", fill="red", font=("Arial", 8, "bold"))
            draw_tree(canvas, node.left, left_x, left_y, dx / 2, dy, root_child_dy, level + 1)
        if node.right:
            right_x = x + dx
            right_y = y + (root_child_dy if level == 0 else dy)
            canvas.create_line(x, y + node_radius, right_x, right_y - node_radius, arrow=tk.LAST, fill="blue", width=2)
            canvas.create_text((x + right_x) / 2, (y + right_y) / 2, text="1", fill="red", font=("Arial", 8, "bold"))
            draw_tree(canvas, node.right, right_x, right_y, dx / 2, dy, root_child_dy, level + 1)

# Function to count the nodes in the Huffman tree
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Global variables to store encoded data and codebook
encoded_data_global = ""
codebook_global = {}

def encode_data():
    global encoded_data_global, codebook_global
    
    data = input_text.get("1.0", "end-1c")
    if not data:
        messagebox.showwarning("Input Error", "Please enter data to encode.")
        return

    # Clear previous outputs
    encoded_output.config(state=tk.NORMAL)
    encoded_output.delete("1.0", tk.END)  # Clear encoded data box
    encoded_output.config(state=tk.DISABLED)

    codebook_output.config(state=tk.NORMAL)
    codebook_output.delete("1.0", tk.END)  # Clear codebook box
    codebook_output.config(state=tk.DISABLED)

    original_size_output.config(state=tk.NORMAL)
    original_size_output.delete("1.0", tk.END)  # Clear original size box
    original_size_output.config(state=tk.DISABLED)

    compressed_size_output.config(state=tk.NORMAL)
    compressed_size_output.delete("1.0", tk.END)  # Clear compressed size box
    compressed_size_output.config(state=tk.DISABLED)

    size_difference_output.config(state=tk.NORMAL)
    size_difference_output.delete("1.0", tk.END)  # Clear size difference box
    size_difference_output.config(state=tk.DISABLED)

    decoded_output.config(state=tk.NORMAL)
    decoded_output.delete("1.0", tk.END)  # Clear decoded output box
    decoded_output.config(state=tk.DISABLED)

    # Encode the new input data
    encoded_data, codebook, root = huffman_encoding(data)
    original_size, compressed_size, difference = calculate_compression_difference(data, encoded_data)
    
    # Store the encoded data and codebook globally
    encoded_data_global = encoded_data
    codebook_global = codebook

    # Update outputs with new data
    encoded_output.config(state=tk.NORMAL)
    for i in range(0, len(encoded_data), 50):  # Adjust line length if needed
        encoded_output.insert(tk.END, encoded_data[i:i + 50] + '\n')
    encoded_output.config(state=tk.DISABLED)

    codebook_output.config(state=tk.NORMAL)
    for char, code in codebook.items():
        codebook_output.insert(tk.END, f'{char}: {code}\n')
    codebook_output.config(state=tk.DISABLED)

    original_size_output.config(state=tk.NORMAL)
    original_size_output.insert(tk.END, f"{original_size} bits")
    original_size_output.config(state=tk.DISABLED)

    compressed_size_output.config(state=tk.NORMAL)
    compressed_size_output.insert(tk.END, f"{compressed_size} bits")
    compressed_size_output.config(state=tk.DISABLED)

    size_difference_output.config(state=tk.NORMAL)
    size_difference_output.insert(tk.END, f"{difference} bits")
    size_difference_output.config(state=tk.DISABLED)

    # Clear the canvas and draw the new tree
    canvas.delete("all")
    node_count = count_nodes(root)
    dx, dy, root_child_dy = calculate_spacing(node_count)
    draw_tree(canvas, root, canvas.winfo_width() // 2, 40, dx, dy, root_child_dy)
    canvas.config(scrollregion=canvas.bbox("all"))

def decode_data():
    global encoded_data_global, codebook_global
    
    if not encoded_data_global or not codebook_global:
        messagebox.showwarning("Decode Error", "No encoded data or codebook available. Please encode data first.")
        return

    decoded_data = huffman_decoding(encoded_data_global, codebook_global)

    # Display the decoded data
    decoded_output.config(state=tk.NORMAL)
    decoded_output.delete("1.0", tk.END)  # Clear the decoded output box
    decoded_output.insert(tk.END, decoded_data)
    decoded_output.config(state=tk.DISABLED)

    # Clear all other fields and boxes
    encoded_output.config(state=tk.NORMAL)
    encoded_output.delete("1.0", tk.END)
    encoded_output.config(state=tk.DISABLED)

    codebook_output.config(state=tk.NORMAL)
    codebook_output.delete("1.0", tk.END)
    codebook_output.config(state=tk.DISABLED)

    original_size_output.config(state=tk.NORMAL)
    original_size_output.delete("1.0", tk.END)
    original_size_output.config(state=tk.DISABLED)

    compressed_size_output.config(state=tk.NORMAL)
    compressed_size_output.delete("1.0", tk.END)
    compressed_size_output.config(state=tk.DISABLED)

    size_difference_output.config(state=tk.NORMAL)
    size_difference_output.delete("1.0", tk.END)
    size_difference_output.config(state=tk.DISABLED)

    # Clear the canvas
    canvas.delete("all")

    # Clear the input text area
    input_text.delete("1.0", tk.END)

    # Reset focus to the input text area
    input_text.focus_set()

# GUI Application
root = tk.Tk()
root.title("Huffman Coding Visualization")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.N, tk.S, tk.W, tk.E))

input_label = ttk.Label(frame, text="Enter Data:")
input_label.grid(row=0, column=0, sticky=tk.W)

input_text = tk.Text(frame, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=2, pady=5)

encode_button = ttk.Button(frame, text="Encode", command=encode_data)
encode_button.grid(row=2, column=0, pady=5, sticky=tk.W)

decode_button = ttk.Button(frame, text="Decode", command=decode_data)
decode_button.grid(row=2, column=1, pady=5, sticky=tk.E)

encoded_label = ttk.Label(frame, text="Encoded Data:")
encoded_label.grid(row=3, column=0, sticky=tk.W)

encoded_frame = ttk.Frame(frame)
encoded_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
encoded_output = tk.Text(encoded_frame, height=10, width=40, wrap=tk.NONE, state=tk.DISABLED)
encoded_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
encoded_scroll_y = tk.Scrollbar(encoded_frame, orient=tk.VERTICAL, command=encoded_output.yview)
encoded_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
encoded_output.config(yscrollcommand=encoded_scroll_y.set)

codebook_label = ttk.Label(frame, text="Codebook:")
codebook_label.grid(row=5, column=0, sticky=tk.W)

codebook_frame = ttk.Frame(frame)
codebook_frame.grid(row=6, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
codebook_output = tk.Text(codebook_frame, height=10, width=40, wrap=tk.NONE, state=tk.DISABLED)
codebook_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
codebook_scroll_y = tk.Scrollbar(codebook_frame, orient=tk.VERTICAL, command=codebook_output.yview)
codebook_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
codebook_output.config(yscrollcommand=codebook_scroll_y.set)

original_size_label = ttk.Label(frame, text="Original Data Size:")
original_size_label.grid(row=7, column=0, sticky=tk.W)

original_size_output = tk.Text(frame, height=1, width=20, state=tk.DISABLED)
original_size_output.grid(row=7, column=1, sticky=tk.E)

compressed_size_label = ttk.Label(frame, text="Compressed Data Size:")
compressed_size_label.grid(row=8, column=0, sticky=tk.W)

compressed_size_output = tk.Text(frame, height=1, width=20, state=tk.DISABLED)
compressed_size_output.grid(row=8, column=1, sticky=tk.E)

size_difference_label = ttk.Label(frame, text="Size Difference:")
size_difference_label.grid(row=9, column=0, sticky=tk.W)

size_difference_output = tk.Text(frame, height=1, width=20, state=tk.DISABLED)
size_difference_output.grid(row=9, column=1, sticky=tk.E)

decoded_label = ttk.Label(frame, text="Decoded Data:")
decoded_label.grid(row=10, column=0, sticky=tk.W)

decoded_output = tk.Text(frame, height=10, width=40, state=tk.DISABLED)
decoded_output.grid(row=11, column=0, columnspan=2, pady=5)

# Background color for canvas_frame
canvas_frame = ttk.Frame(root, style="Tree.TFrame")
canvas_frame.grid(row=0, column=1, rowspan=12, padx=10, pady=10, sticky=(tk.N, tk.S, tk.E, tk.W))

# Frame to contain the canvas and horizontal scrollbar
canvas_with_scrollbar_frame = ttk.Frame(canvas_frame)
canvas_with_scrollbar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_with_scrollbar_frame, bg="lightgray")  # Set the background color here
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Horizontal scrollbar inside the canvas_with_scrollbar_frame
scroll_x = tk.Scrollbar(canvas_with_scrollbar_frame, orient=tk.HORIZONTAL, command=canvas.xview)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
canvas.config(xscrollcommand=scroll_x.set)

# Removed vertical scrollbar

tree_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=tree_frame, anchor="nw")

# Apply styles for ttk widgets
style = ttk.Style()
style.configure("Tree.TFrame", background="lightblue")  # Background color for the tree frame

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
canvas_frame.grid_rowconfigure(0, weight=1)
canvas_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
