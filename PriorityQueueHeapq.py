# #  Heapq CLI
# import heapq

# class PriorityQueue:
#     """
#     A class to represent a priority queue using a heap-based approach.
#     Elements are dequeued based on their priority, with the element of the lowest
#     value (highest priority) being dequeued first.
#     """

#     def __init__(self):
#         """Initialize an empty priority queue."""
#         self.queue = []  # The heap/priority queue
#         self.entry_finder = {}  # Map to store active entries for quick lookup
#         self.REMOVED = '<removed-item>'  # Placeholder for a removed item
#         self.counter = 0  # Unique sequence count

#     def is_empty(self) -> bool:
#         """
#         Check if the priority queue is empty.

#         Returns:
#             bool: True if the queue is empty, False otherwise.
#         """
#         return not self.queue

#     def enqueue(self, item: str, priority: int) -> None:
#         """
#         Add an item to the priority queue with a given priority.

#         Args:
#             item (str): The item to add to the queue.
#             priority (int): The priority of the item.
#         """
#         if item in self.entry_finder:
#             self.remove_item(item)  # Remove the existing item if it's already in the queue

#         count = self.counter
#         entry = [priority, count, item]  # Create a new entry
#         self.entry_finder[item] = entry  # Map the item to its entry
#         heapq.heappush(self.queue, entry)  # Add the entry to the heap
#         self.counter += 1  # Increment the counter to ensure unique sorting for same-priority items
#         print(f"Enqueued: {item} with priority {priority}")

#     def remove_item(self, item: str) -> None:
#         """
#         Mark an existing item as removed from the priority queue.
#         Does not raise an error if the item is not found.

#         Args:
#             item (str): The item to be marked as removed.
#         """
#         entry = self.entry_finder.pop(item, None)  # Remove the item from the entry finder
#         if entry is not None:
#             entry[-1] = self.REMOVED  # Mark the item as removed

#     def dequeue(self) -> str:
#         """
#         Remove and return the item with the highest priority (lowest priority value) from the queue.

#         Returns:
#             str: The item with the highest priority.

#         Raises:
#             Exception: If the priority queue is empty.
#         """
#         while self.queue:
#             priority, count, item = heapq.heappop(self.queue)  # Pop the entry with the highest priority
#             if item is not self.REMOVED:
#                 del self.entry_finder[item]  # Remove the item from the entry finder
#                 print(f"Dequeued: {item}")
#                 return item
#         raise Exception("Priority Queue is empty. Cannot dequeue.")

#     def traverse(self) -> None:
#         """
#         Print all items in the priority queue with their priorities.
#         """
#         active_entries = [(priority, item) for priority, _, item in self.queue if item is not self.REMOVED]
#         if not active_entries:
#             print("Priority Queue is empty.")
#         else:
#             print("Priority Queue contains:")
#             for priority, item in sorted(active_entries):
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





# Heapq GUI
import heapq
import tkinter as tk
from tkinter import messagebox

class PriorityQueue:
    """
    A class to represent a priority queue using a heap-based approach.
    Elements are dequeued based on their priority, with the element of the lowest
    value (highest priority) being dequeued first.
    """

    def __init__(self):
        """Initialize an empty priority queue."""
        self.queue = []  # The heap/priority queue
        self.entry_finder = {}  # Map to store active entries for quick lookup
        self.REMOVED = '<removed-item>'  # Placeholder for a removed item
        self.counter = 0  # Unique sequence count

    def is_empty(self) -> bool:
        """
        Check if the priority queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self.queue

    def enqueue(self, item: str, priority: int) -> None:
        """
        Add an item to the priority queue with a given priority.

        Args:
            item (str): The item to add to the queue.
            priority (int): The priority of the item.
        """
        if item in self.entry_finder:
            self.remove_item(item)  # Remove the existing item if it's already in the queue

        count = self.counter
        entry = [priority, count, item]  # Create a new entry
        self.entry_finder[item] = entry  # Map the item to its entry
        heapq.heappush(self.queue, entry)  # Add the entry to the heap
        self.counter += 1  # Increment the counter to ensure unique sorting for same-priority items

    def remove_item(self, item: str) -> None:
        """
        Mark an existing item as removed from the priority queue.
        Does not raise an error if the item is not found.

        Args:
            item (str): The item to be marked as removed.
        """
        entry = self.entry_finder.pop(item, None)  # Remove the item from the entry finder
        if entry is not None:
            entry[-1] = self.REMOVED  # Mark the item as removed

    def dequeue(self) -> str:
        """
        Remove and return the item with the highest priority (lowest priority value) from the queue.

        Returns:
            str: The item with the highest priority.

        Raises:
            Exception: If the priority queue is empty.
        """
        while self.queue:
            priority, count, item = heapq.heappop(self.queue)  # Pop the entry with the highest priority
            if item is not self.REMOVED:
                del self.entry_finder[item]  # Remove the item from the entry finder
                return item
        raise Exception("Priority Queue is empty. Cannot dequeue.")

    def traverse(self) -> str:
        """
        Return a string representation of all items in the priority queue with their priorities.
        """
        active_entries = [(priority, item) for priority, _, item in self.queue if item is not self.REMOVED]
        if not active_entries:
            return "Priority Queue is empty."
        else:
            entries = [f"Item: {item}, Priority: {priority}" for priority, item in sorted(active_entries)]
            return "\n".join(entries)

class PriorityQueueGUI:
    def __init__(self, root):
        self.pq = PriorityQueue()
        self.root = root
        self.root.title("Priority Queue")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame for inputs and buttons
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Entry for item
        tk.Label(frame, text="Item:").grid(row=0, column=0, padx=5, pady=5)
        self.item_entry = tk.Entry(frame)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for priority
        tk.Label(frame, text="Priority:").grid(row=1, column=0, padx=5, pady=5)
        self.priority_entry = tk.Entry(frame)
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(frame, text="Enqueue", command=self.enqueue_item).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(frame, text="Dequeue", command=self.dequeue_item).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(frame, text="Display Queue", command=self.display_queue).grid(row=2, column=2, padx=5, pady=5)

        # Text area for displaying queue
        self.queue_text = tk.Text(self.root, height=10, width=50)
        self.queue_text.pack(padx=10, pady=10)

    def enqueue_item(self):
        item = self.item_entry.get().strip()
        priority = self.priority_entry.get().strip()

        if not item:
            messagebox.showerror("Input Error", "Item cannot be empty.")
            return
        
        try:
            priority = int(priority)
            self.pq.enqueue(item, priority)
            messagebox.showinfo("Success", f"Enqueued: {item} with priority {priority}")
            # Clear the entry boxes
            self.item_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Priority must be an integer.")

    def dequeue_item(self):
        try:
            item = self.pq.dequeue()
            messagebox.showinfo("Success", f"Dequeued: {item}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_queue(self):
        queue_contents = self.pq.traverse()
        self.queue_text.delete(1.0, tk.END)
        self.queue_text.insert(tk.END, queue_contents)

if __name__ == "__main__":
    root = tk.Tk()
    app = PriorityQueueGUI(root)
    root.mainloop()