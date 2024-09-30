# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.next = None

# class single_linked_list:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insertion_at_start(self,element):
#           new_node = Node(element)
#           new_node.next = self.head
#           self.head = new_node
#           # new_node_add = add
          
#   # def at_middle(self, prev_link, next_add, new_node_add, element):
#   #     if prev_link 
#     #     self.new_node = element
#     #     self.prev_link = new_node_add
#     #     self.new_node_link = next_add

#     def insertion_at_last(self, element):
#         new_node = Node(element)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
    
#     def deletion_at_start(self):
#         if self.head == None:
#             print("Linked list is empty")
#         else:
#             deleted_node = self.head
#             self.head = self.head.next
#             return deleted_node.data
        
#     def deletion_at_end(self):
#         if self.head is None:
#             print("Linked list is empty")
#         if self.head.next is None:
#             deleted_node = self.head
#             self.head = None
#             return deleted_node.data
#         current = self.head
#         while current.next.next:
#             current = current.next
#         deleted_node = current.next
#         current.next = None
#         return deleted_node.data
    
#     def traverse(self):
#       current = self.head
#       while current:
#           print(current.data, end=" -> ")
#           current = current.next
#       print("None")

# linked_list = single_linked_list()

# # Insert elements
# linked_list.insertion_at_start(50)
# linked_list.insertion_at_last(30)
# linked_list.insertion_at_start(20)
# linked_list.insertion_at_last(10)

# # Print the linked list
# print("Linked list:")
# linked_list.traverse()

# # Delete elements from beginning and end
# deleted_data = linked_list.deletion_at_start()
# if deleted_data:
#   print("Deleted from beginning:", deleted_data)
# deleted_data = linked_list.deletion_at_end()
# if deleted_data:
#   print("Deleted from end:", deleted_data)

# # Print the linked list after deletions
# print("Linked list after deletions:")
# linked_list.traverse()

# GUI Program
import tkinter as tk
from tkinter import messagebox

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_start(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def insertion_at_last(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def deletion_at_start(self):
        if self.head is None:
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.data
        
    def deletion_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        return deleted_node.data
    
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class LinkedListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List GUI")
        
        self.linked_list = SingleLinkedList()
        
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)
        
        self.label = tk.Label(self.frame, text="Element:")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        
        self.element_entry = tk.Entry(self.frame)
        self.element_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.insert_start_button = tk.Button(self.frame, text="Insert at Start", command=self.insert_at_start)
        self.insert_start_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.insert_end_button = tk.Button(self.frame, text="Insert at End", command=self.insert_at_end)
        self.insert_end_button.grid(row=1, column=1, padx=5, pady=5)
        
        self.delete_start_button = tk.Button(self.frame, text="Delete from Start", command=self.delete_from_start)
        self.delete_start_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.delete_end_button = tk.Button(self.frame, text="Delete from End", command=self.delete_from_end)
        self.delete_end_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.traverse_button = tk.Button(self.frame, text="Traverse", command=self.traverse_list)
        self.traverse_button.grid(row=3, column=0, columnspan=2, pady=5)
        
        self.output = tk.Text(self.frame, width=50, height=10)
        self.output.grid(row=4, column=0, columnspan=2, pady=10)
    
    def insert_at_start(self):
        element = self.element_entry.get()
        if element:
            self.linked_list.insertion_at_start(element)
            self.element_entry.delete(0, tk.END)
            messagebox.showinfo("Info", "Element inserted at the start.")
        else:
            messagebox.showerror("Error", "Please enter an element.")
    
    def insert_at_end(self):
        element = self.element_entry.get()
        if element:
            self.linked_list.insertion_at_last(element)
            self.element_entry.delete(0, tk.END)
            messagebox.showinfo("Info", "Element inserted at the end.")
        else:
            messagebox.showerror("Error", "Please enter an element.")
    
    def delete_from_start(self):
        deleted_element = self.linked_list.deletion_at_start()
        if deleted_element:
            messagebox.showinfo("Info", f"Deleted element from start: {deleted_element}")
        else:
            messagebox.showerror("Error", "Linked list is empty.")
    
    def delete_from_end(self):
        deleted_element = self.linked_list.deletion_at_end()
        if deleted_element:
            messagebox.showinfo("Info", f"Deleted element from end: {deleted_element}")
        else:
            messagebox.showerror("Error", "Linked list is empty.")
    
    def traverse_list(self):
        elements = self.linked_list.traverse()
        self.output.delete('1.0', tk.END)
        if elements:
            self.output.insert(tk.END, " -> ".join(map(str, elements)) + " -> None")
        else:
            self.output.insert(tk.END, "Linked list is empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()
