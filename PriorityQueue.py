# # # Simple Program CLI
# class PriorityQueue:
#     """
#     A class to represent a priority queue, where each element is associated with a priority.
#     Elements are dequeued based on their priority, with the element of the lowest value
#     (highest priority) being dequeued first.
#     """
#     def __init__(self):
#         """Initialize an empty priority queue."""
#         self.queue = []

#     def is_empty(self) -> bool:   # -> bool: represents the expectation, this funtion will return boolean value.
#         """
#         Check if the priority queue is empty.

#         Returns:
#             bool: True if the queue is empty, False otherwise.
#         """
#         return len(self.queue) == 0
#     def enqueue(self, item: str, priority: int) -> None:  # -> None: represents the expectation, this funtion will not return any item.
#         """
#         Add an item to the priority queue with a given priority.

#         Args:
#             item (str): The item to add to the queue.
#             priority (int): The priority of the item.
#         """
#         self.queue.append((item, priority))
#         self.queue.sort(key=lambda x: x[1])  # Sort by priority (ascending order)
#         print(f"Enqueued: {item} with priority {priority}")
#     def dequeue(self) -> str:  # -> str: represents the item which will return in this function is expected as string.
#         """
#         Remove and return the item with the highest priority (lowest priority value) from the queue.

#         Returns:
#             str: The item with the highest priority.
        
#         Raises:
#             Exception: If the priority queue is empty.
#         """
#         if self.is_empty():
#             raise Exception("Priority Queue is empty. Cannot dequeue.")
        
#         item = self.queue.pop(0)[0]
#         print(f"Dequeued: {item}")
#         return item
#     def traverse(self) -> None:   # -> None: represents the expectation, this funtion will not return any item.
#         """
#         Print all items in the priority queue with their priorities.
#         """
#         if self.is_empty():
#             print("Priority Queue is empty.")
#         else:
#             print("Priority Queue contains:")
#             for item, priority in self.queue:
#                 print(f"Item: {item}, Priority: {priority}")
# def main():
#     """
#     The main function to demonstrate the usage of the PriorityQueue class.
#     """
#     pq = PriorityQueue()
#     while True:
#         print("\nPriority Queue Menu:")
#         print("1. Enqueue an item")
#         print("2. Dequeue an item")
#         print("3. Display the queue")
#         print("4. Exit")
#         try:
#             choice = int(input("Enter your choice (1-4): "))
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 4.")
#             continue

#         if choice == 1:
#             item = input("Enter the item to enqueue: ")
#             try:
#                 priority = int(input("Enter the priority for the item: "))
#                 pq.enqueue(item, priority)
#             except ValueError:
#                 print("Invalid priority. Please enter an integer.")
#         elif choice == 2:
#             try:
#                 pq.dequeue()
#             except Exception as e:
#                 print(e)
#         elif choice == 3:
#             pq.traverse()
#         elif choice == 4:
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")
# if __name__ == "__main__":
#     main()




# Simple Program GUI
import tkinter as tk
from tkinter import messagebox, simpledialog

class PriorityQueue:
    """
    A class to represent a priority queue, where each element is associated with a priority.
    Elements are dequeued based on their priority, with the element of the lowest value
    (highest priority) being dequeued first.
    """
    
    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, item: str, priority: int) -> None:
        if not item:
            raise ValueError("Item cannot be empty. Please enter a valid item.")
        
        if priority is None:
            raise ValueError("Priority cannot be empty. Please enter a valid integer priority.")
        
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])  # Sort by priority (ascending order)
        messagebox.showinfo("Success", f"Enqueued: {item} with priority {priority}")

    def dequeue(self) -> str:
        if self.is_empty():
            raise Exception("Priority Queue is empty. Cannot dequeue.")
        
        item = self.queue.pop(0)[0]
        messagebox.showinfo("Dequeue", f"Dequeued: {item}")
        return item

    def traverse(self) -> str:
        if self.is_empty():
            return "Priority Queue is empty."
        else:
            items = "\n".join([f"Item: {item}, Priority: {priority}" for item, priority in self.queue])
            return f"Priority Queue contains:\n{items}"

class PriorityQueueApp:
    """
    A class to create a GUI application for the PriorityQueue.
    """
    
    def __init__(self, root):
        """
        Initialize the GUI application.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        self.pq = PriorityQueue()
        self.root = root
        self.root.title("Priority Queue Application")

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create and arrange widgets in the GUI application.
        """
        self.queue_display = tk.Text(self.root, height=15, width=50, state='disabled')
        self.queue_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        enqueue_button = tk.Button(self.root, text="Enqueue Item", command=self.enqueue_item)
        enqueue_button.grid(row=1, column=0, padx=10, pady=10)

        dequeue_button = tk.Button(self.root, text="Dequeue Item", command=self.dequeue_item)
        dequeue_button.grid(row=1, column=1, padx=10, pady=10)

        display_button = tk.Button(self.root, text="Display Queue", command=self.display_queue)
        display_button.grid(row=1, column=2, padx=10, pady=10)

    def enqueue_item(self) -> None:
        """
        Enqueue an item by prompting the user for input via dialog boxes.
        """
        item = simpledialog.askstring("Input", "Enter the item to enqueue:")
        if item is None:
            messagebox.showwarning("Warning", "Item entry was canceled.")
            return  # User canceled the input

        try:
            if not item.strip():
                raise ValueError("Item cannot be empty. Please enter a valid item.")

            priority = simpledialog.askinteger("Input", "Enter the priority for the item:")
            if priority is None:
                messagebox.showwarning("Warning", "Priority entry was canceled.")
                return  # User canceled the input
            
            self.pq.enqueue(item, priority)
            self.display_queue()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def dequeue_item(self) -> None:
        """
        Dequeue an item and show the result via a message box.
        """
        try:
            self.pq.dequeue()
            self.display_queue()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_queue(self) -> None:
        """
        Display the current state of the priority queue in the text widget.
        """
        queue_content = self.pq.traverse()
        self.queue_display.config(state='normal')
        self.queue_display.delete(1.0, tk.END)  # Clear the text widget
        self.queue_display.insert(tk.END, queue_content)
        self.queue_display.config(state='disabled')

def main() -> None:
    """
    The main function to run the Priority Queue GUI application.
    """
    root = tk.Tk()
    app = PriorityQueueApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
