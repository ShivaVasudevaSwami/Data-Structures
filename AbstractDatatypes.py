# # Aim: Write a program to implement Abstract Data Types (ADT)
# class Stack:
#     def __init__(self, size):
#         self.array = [None] * size  # Initialize array with None values
#         self.top = -1  # Stack is empty
#         self.size = size  # Define the size of the stack

#     def push(self, element):
#         # Check Overflow or Stack is Full
#         if self.top >= self.size - 1:
#             print("Stack Full.")
#         else:
#             self.top += 1
#             self.array[self.top] = element

#     def pop(self):
#         # Check Underflow OR Stack Empty
#         if self.top == -1:
#             return None  # "Stack Empty."
#         else:
#             element = self.array[self.top]
#             print(element)
#             self.top -= 1
#             del self.array[self.top +1] # Clear the popped element
            
#     def peek(self):
#         if self.top == -1:
#             return None
#         else:
#             print(self.array[self.top])

#     def display(self):
#         for i in range(self.top, -1, -1):
#             print(self.array[i])

# # Example usage
# stack = Stack(5)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6) # This should prints "Stack Full."
# stack.display()
# stack.pop()# This will print the top item and the it will delete the top item
# stack.peek()


#Aim: Write a program to implement Abstract Data Types (ADT) with GUI
import customtkinter as ctk
from tkinter import messagebox

class Stack:
    def __init__(self, size):
        self.array = [None] * size  # Initialize array with None values
        self.top = -1  # Stack is empty
        self.size = size  # Define the size of the stack

    def push(self, element):
        # Check Overflow or Stack is Full
        if self.top >= self.size - 1:
            messagebox.showerror("Error", "Stack Full.")
        else:
            self.top += 1
            self.array[self.top] = element

    def pop(self):
        # Check Underflow OR Stack Empty
        if self.top == -1:
            messagebox.showerror("Error", "Stack Empty.")
            return None
        else:
            element = self.array[self.top]
            self.array[self.top] = None  # Clear the popped element
            self.top -= 1
            return element

    def peek(self):
        if self.top == -1:
            messagebox.showinfo("Peek", "Stack is empty.")
            return None
        else:
            return self.array[self.top]

    def display(self):
        if self.top == -1:
            messagebox.showinfo("Display", "Stack is empty.")
        else:
            stack_elements = [str(self.array[i]) for i in range(self.top, -1, -1)]
            messagebox.showinfo("Stack Elements", "\n".join(stack_elements))

class StackGUI:
    def __init__(self, stack):
        self.stack = stack
        self.root = ctk.CTk()
        self.root.title("Abstract Datatype(Stack)")

        self.element_label = ctk.CTkLabel(self.root, text="Element:")
        self.element_label.pack()
        self.element_entry = ctk.CTkEntry(self.root)
        self.element_entry.pack()

        self.push_button = ctk.CTkButton(self.root, text="Push",text_color="black", fg_color="#16FF00", command=self.push)
        self.push_button.pack()
        self.pop_button = ctk.CTkButton(self.root, text="Pop", text_color="black" ,fg_color="#FFED00", command=self.pop)
        self.pop_button.pack()
        self.peek_button = ctk.CTkButton(self.root, text="Peek", text_color="black", fg_color="#ECA3F5", command=self.peek)
        self.peek_button.pack()
        self.display_button = ctk.CTkButton(self.root, text="Display", text_color = "black", fg_color = "lightgreen", command=self.display)
        self.display_button.pack()

    def push(self):
        element = self.element_entry.get()
        if element:
            self.stack.push(element)
            self.element_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Please enter an element.")

    def pop(self):
        element = self.stack.pop()
        if element:
            messagebox.showinfo("Pop", f"Popped element: {element}")

    def peek(self):
        element = self.stack.peek()
        if element:
            messagebox.showinfo("Peek", f"Top element: {element}")

    def display(self):
        self.stack.display()

    def run(self):
        self.root.mainloop()

# Example usage
stack = Stack(5)
gui = StackGUI(stack)
gui.run()
