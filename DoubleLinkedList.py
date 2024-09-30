# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.next = None
#       self.prev = None

# class double_linked_list:
    
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def insertion_at_start(self,element):
#         new_node = Node(element)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
    
#     def insertion_at_last(self, element):
#         new_node = Node(element)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
    
#     def deletion_at_start(self):
#         if self.head == None:
#             print("Linked list is empty")
#         deleted_node = self.head
#         if self.head == self.tail:
#             self.head = self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#         return deleted_node.data
    
#     def deletion_at_end(self):
#         if self.head is None:
#             return None
#         deleted_node = self.tail
#         if self.head == self.tail:
#             self.head = self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#         return deleted_node.data
    
#     def traverse(self):
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.next
#         print("None")

# if __name__ == '__main__':
#   # Create a doubly linked list
#   linked_list = double_linked_list()
  
#   # Insert elements
#   ele = int(input("Enter element to insert at the beginning : "))
#   linked_list.insertion_at_start(ele)
#   ele = int(input("Enter element to insert at the end : "))
#   linked_list.insertion_at_last(ele)
#   ele = int(input("Enter element to insert at the beginning : "))
#   linked_list.insertion_at_start(ele)
#   ele = int(input("Enter element to insert at the end : "))
#   linked_list.insertion_at_last(ele)

# # Print the linked list
#   print("Doubly Linked List:")
#   linked_list.traverse()

# # Delete elements from beginning and end
#   deleted_data = linked_list.deletion_at_start()
#   if deleted_data:
#     print("Deleted from beginning:", deleted_data)
#   deleted_data = linked_list.deletion_at_end()
#   if deleted_data:
#     print("Deleted from end:", deleted_data)

# # Print the linked list after deletions
#   print("Doubly Linked List after deletions:")
#   linked_list.traverse()

# GUI Program
import tkinter as tk
from tkinter import messagebox

# Define Node and double_linked_list classes (same as provided in your code)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion_at_start(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insertion_at_last(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def deletion_at_start(self):
        if self.head is None:
            messagebox.showinfo("Info", "Linked list is empty")
            return None
        
        deleted_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        return deleted_node.data
    
    def deletion_at_end(self):
        if self.head is None:
            messagebox.showinfo("Info", "Linked list is empty")
            return None
        
        deleted_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        return deleted_node.data
    
    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Define the GUI class
class DoublyLinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List GUI")
        
        self.linked_list = double_linked_list()
        
        # Create input elements
        self.label1 = tk.Label(root, text="Enter element to insert at the beginning:")
        self.label1.pack()
        self.entry1 = tk.Entry(root)
        self.entry1.pack()
        
        self.insert_begin_button = tk.Button(root, text="Insert at Beginning", command=self.insert_at_beginning)
        self.insert_begin_button.pack()
        
        self.label2 = tk.Label(root, text="Enter element to insert at the end:")
        self.label2.pack()
        self.entry2 = tk.Entry(root)
        self.entry2.pack()
        
        self.insert_end_button = tk.Button(root, text="Insert at End", command=self.insert_at_end)
        self.insert_end_button.pack()
        
        self.delete_begin_button = tk.Button(root, text="Delete from Beginning", command=self.delete_from_beginning)
        self.delete_begin_button.pack()
        
        self.delete_end_button = tk.Button(root, text="Delete from End", command=self.delete_from_end)
        self.delete_end_button.pack()
        
        self.display_button = tk.Button(root, text="Traverse Linked List", command=self.display_linked_list)
        self.display_button.pack()
        
        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

    def insert_at_beginning(self):
        element = self.entry1.get()
        if element.isdigit():
            self.linked_list.insertion_at_start(int(element))
            self.output_label.config(text="Element inserted at the beginning.")
        else:
            self.output_label.config(text="Please enter a valid number.")
        self.entry1.delete(0, tk.END)

    def insert_at_end(self):
        element = self.entry2.get()
        if element.isdigit():
            self.linked_list.insertion_at_last(int(element))
            self.output_label.config(text="Element inserted at the end.")
        else:
            self.output_label.config(text="Please enter a valid number.")
        self.entry2.delete(0, tk.END)

    def delete_from_beginning(self):
        deleted_data = self.linked_list.deletion_at_start()
        if deleted_data is not None:
            self.output_label.config(text=f"Deleted from beginning: {deleted_data}")

    def delete_from_end(self):
        deleted_data = self.linked_list.deletion_at_end()
        if deleted_data is not None:
            self.output_label.config(text=f"Deleted from end: {deleted_data}")

    def display_linked_list(self):
        elements = self.linked_list.traverse()
        if elements:
            linked_list_str = " <-> ".join(map(str, elements)) + " <-> None"
            self.output_label.config(text=f"Doubly Linked List: {linked_list_str}")
        else:
            self.output_label.config(text="Doubly Linked List is empty.")

# Initialize the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = DoublyLinkedListGUI(root)
    root.mainloop()
