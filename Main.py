import customtkinter as ctk
import subprocess

# Create the main window
root = ctk.CTk()
root.title("Data Structure")

# Set a fixed width and height for all buttons
button_width = 20
button_height = 3

# Create a frame to hold the buttons, centered in the window
frame = ctk.CTkFrame(root)
frame.pack(expand=True)  # Allow the frame to expand and center in the window

# Function to execute the stack GUI file
def run_adt():
    subprocess.run(["python", "Python/DataStructures/AbstractDatatypes.py"])  # Replace with "python3" if needed
    
def run_so():
    subprocess.run(["python", "Python/DataStructures/StackOperations.py"])
    
def run_sll():
    subprocess.run(["python", "Python/DataStructures/SingleLinkedList.py"])
    
def run_dll():
    subprocess.run(["python", "Python/DataStructures/DoubleLinkedList.py"])
    
def run_q():
    subprocess.run(["python", "Python/DataStructures/Queue.py"])
    
def run_pq():
    subprocess.run(["python", "Python/DataStructures/PriorityQueue.py"])
    
def run_pqhq():
    subprocess.run(["python", "Python/DataStructures/PriorityQueueHeapq.py"])
    
def run_bt():
    subprocess.run(["python", "Python/DataStructures/TreeOperations.py"])
    
def run_hcbt():
    subprocess.run(["python", "Python/DataStructures/HuffmanCodingBinaryTree.py"])
    
def run_gh():
    subprocess.run(["python", "Python/DataStructures/Graph.py"])
    
def run_htch():
    subprocess.run(["python", "Python/DataStructures/HashTable(CollisionHandling).py"])
    
def run_htnc():
    subprocess.run(["python", "Python/DataStructures/HashTable(No_Collision).py"])
    
# Create 12 buttons manually and place them in a vertical layout within the frame
ADT = ctk.CTkButton(frame, text="Abstract Data Types", width=button_width, height=button_height, command=run_adt)
ADT.pack(padx=10, pady=5)

StackOperations = ctk.CTkButton(frame, text="Stack Operations", width=button_width, height=button_height, command=run_so)
StackOperations.pack(padx=10, pady=5)

SingleLinkedList = ctk.CTkButton(frame, text="Single Linked List", width=button_width, height=button_height, command=run_sll)
SingleLinkedList.pack(padx=10, pady=5)

DoubleLinkedList = ctk.CTkButton(frame, text="Double Linked List", width=button_width, height=button_height, command=run_dll)
DoubleLinkedList.pack(padx=10, pady=5)

QueueOperations = ctk.CTkButton(frame, text="Queue Operations", width=button_width, height=button_height, command=run_q)
QueueOperations.pack(padx=10, pady=5)

PriorityQueueOperations = ctk.CTkButton(frame, text="Priority Queue", width=button_width, height=button_height, command=run_pq)
PriorityQueueOperations.pack(padx=10, pady=5)

PQHeapqOperations = ctk.CTkButton(frame, text="Priority Queue Heapq", width=button_width, height=button_height, command=run_pqhq)
PQHeapqOperations.pack(padx=10, pady=5)

BinaryTreeOperations = ctk.CTkButton(frame, text="Binary Tree", width=button_width, height=button_height, command=run_bt)
BinaryTreeOperations.pack(padx=10, pady=5)

HCBTOperations = ctk.CTkButton(frame, text="Huffman Coding Binary Tree", width=button_width, height=button_height, command=run_hcbt)
HCBTOperations.pack(padx=10, pady=5)

GraphOperations = ctk.CTkButton(frame, text="Graph Operations", width=button_width, height=button_height, command=run_gh)
GraphOperations.pack(padx=10, pady=5)

HashTableCollison = ctk.CTkButton(frame, text="Hash Table Collision", width=button_width, height=button_height, command=run_htch)
HashTableCollison.pack(padx=10, pady=5)

HashTableNoCollision = ctk.CTkButton(frame, text="Hash Table No Collision", width=button_width, height=button_height, command=run_htnc)
HashTableNoCollision.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
