# # Aim: Stack with insertion, deletion, traversal operations.
# class Stack_Operations:
#     def __init__(self, size):
#         self.array = [None] * size  # Initialize array with None values
#         self.top = -1  # Stack is empty
#         self.size = size  # Define the size of the stack
    
#     def insertion(self, element):
#         if self.top >= self.size - 1:  # If stack is full
#             print("Stack Overflow")
#         else:
#             self.top += 1
#             self.array[self.top] = element

#     def deletion(self):
#         if self.top == -1:  # If stack is empty
#             print("Stack Underflow")
#         else:
#             element = self.array[self.top]
#             print("Last Element which you have inserted is deleted")
#             self.top -= 1
#             del element
    
#     def peek(self):
#         if self.top == -1:  # If stack is empty
#             print("Stack Underflow")
#         else:
#             print("Last Element that you inserted is: ", self.array[self.top])

#     def print_stack(self):
#         print("Stack elements:")
#         for item in self.array[::-1]:
#             print(item)
    
#     def traverse(self):
#         if self.top == -1:  # If stack is empty
#             print("Stack is empty")
#         else:
#             print("Traversing stack elements:")
#             for i in range(self.top + 1):
#                 print(self.array[i])

# stackOp = Stack_Operations(5)
# stackOp.insertion(1)
# stackOp.insertion(2)
# stackOp.insertion(3)
# stackOp.insertion(4)
# stackOp.insertion(5)
# stackOp.insertion(6)
# stackOp.peek()
# stackOp.deletion()
# stackOp.print_stack()
# stackOp.traverse()


# Aim: Stack with insertion, deletion, traversal operations with GUI.
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk

class Stack_Operations:
    def __init__(self, size):
        self.array = [None] * size  # Initialize array with None values
        self.top = -1  # Stack is empty
        self.size = size  # Define the size of the stack
    
    def insertion(self, element):
        if self.top >= self.size - 1:  # If stack is full
            print("Stack Overflow")
        else:
            self.top += 1
            self.array[self.top] = element

    def deletion(self):
        if self.top == -1:  # If stack is empty
            print("Stack Underflow")
        else:
            element = self.array[self.top]
            print("Last Element which you have inserted is deleted")
            self.top -= 1
            return element
    
    def peek(self):
        if self.top == -1:  # If stack is empty
            return None
        else:
            return self.array[self.top]

    def print_stack(self):
        print("Stack elements:")
        for item in self.array[::-1]:
            print(item)
    
    def traverse(self):
        if self.top == -1:  # If stack is empty
            return "Stack is empty"
        else:
            elements = [str(self.array[i]) for i in range(self.top + 1)]
            return "\n".join(elements)

    def get_stack(self):
        return self.array[:self.top + 1]

class StackApp:
    def __init__(self, root, stack):
        self.stack = stack
        self.root = root
        self.root.title("Stack Operations")

        self.frame = ctk.CTkFrame(root)
        self.frame.pack(pady=20)

        self.listbox = tk.Listbox(self.frame, width=30, height=10)
        self.listbox.pack(side=ctk.LEFT, padx=20)

        self.scrollbar = ctk.CTkScrollbar(self.frame, orientation="vertical")
        self.scrollbar.configure(command=self.listbox.yview)
        self.scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)

        self.entry = ctk.CTkEntry(root)
        self.entry.pack(pady=10)

        self.button_frame = ctk.CTkFrame(root)
        self.button_frame.pack(pady=10)

        self.insert_button = ctk.CTkButton(self.button_frame, text="Insert", command=self.insert_element)
        self.insert_button.pack(side=ctk.LEFT, padx=5)

        self.delete_button = ctk.CTkButton(self.button_frame, text="Delete", command=self.delete_element)
        self.delete_button.pack(side=ctk.LEFT, padx=5)

        self.peek_button = ctk.CTkButton(self.button_frame, text="Peek", command=self.peek_element)
        self.peek_button.pack(side=ctk.LEFT, padx=5)

        self.traverse_button = ctk.CTkButton(self.button_frame, text="Traverse", command=self.traverse_elements)
        self.traverse_button.pack(side=ctk.LEFT, padx=5)

        self.update_listbox()

    def insert_element(self):
        element = self.entry.get()
        if element:
            self.stack.insertion(element)
            self.entry.delete(0, ctk.END)
            self.update_listbox()

    def delete_element(self):
        element = self.stack.deletion()
        if element:
            messagebox.showinfo("Deleted", f"Deleted element: {element}")
            self.update_listbox()

    def peek_element(self):
        if self.stack.top != -1:
            element = self.stack.peek()
            messagebox.showinfo("Peek", f"Top element: {element}")

    def traverse_elements(self):
        elements = self.stack.traverse()
        messagebox.showinfo("Traverse", f"Stack elements:\n{elements}")
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in reversed(self.stack.get_stack()):
            self.listbox.insert(tk.END, item) 

if __name__ == "__main__":
    stack = Stack_Operations(5)
    root = ctk.CTk()
    app = StackApp(root, stack)
    root.mainloop()
