# # CLI
# class Queue:
#     def __init__(self):
#         self.queue = []

#     def is_empty(self):
#         return len(self.queue) == 0

#     def enqueue(self, item):
#         self.queue.append(item)
#         print(f"Enqueued: {item}")

#     def dequeue(self):
#         if self.is_empty():
#             print("Queue is empty. Cannot dequeue.")
#             return None
#         return self.queue.pop(0)

#     def traverse(self):
#         if self.is_empty():
#             print("Queue is empty.")
#         else:
#             print("Queue contains:", end=" ")
#             for item in self.queue:
#                 print(item, end=" ")
#             print()

# # Example usage:
# if __name__ == "__main__":
#     q = Queue()

#     # Enqueue elements
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue(3)

#     # Traverse elements
#     q.traverse()

#     # Dequeue elements
#     print(f"Dequeued: {q.dequeue()}")
#     print(f"Dequeued: {q.dequeue()}")

#     # Traverse elements
#     q.traverse()

#     # Dequeue elements
#     print(f"Dequeued: {q.dequeue()}")

#     # Attempt to dequeue from an empty queue
#     print(f"Dequeued: {q.dequeue()}")


#GUI
import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def traverse(self):
        if self.is_empty():
            return "Queue is empty."
        else:
            return "Queue contains: " + " ".join(map(str, self.queue))

class QueueGUI:
    def __init__(self, root):
        self.queue = Queue()
        self.root = root
        self.root.title("Queue GUI")

        self.label = tk.Label(root, text="Queue Operations", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.enqueue_frame = tk.Frame(root)
        self.enqueue_frame.pack(pady=5)

        self.enqueue_label = tk.Label(self.enqueue_frame, text="Enqueue:")
        self.enqueue_label.pack(side=tk.LEFT)

        self.enqueue_entry = tk.Entry(self.enqueue_frame)
        self.enqueue_entry.pack(side=tk.LEFT)

        self.enqueue_button = tk.Button(self.enqueue_frame, text="Enqueue", command=self.enqueue)
        self.enqueue_button.pack(side=tk.LEFT)

        self.dequeue_button = tk.Button(root, text="Dequeue", command=self.dequeue)
        self.dequeue_button.pack(pady=5)

        self.traverse_button = tk.Button(root, text="Traverse", command=self.traverse)
        self.traverse_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def enqueue(self):
        item = self.enqueue_entry.get()
        if item:
            self.queue.enqueue(item)
            self.result_label.config(text=f"Enqueued: {item}")
            self.enqueue_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item to enqueue.")

    def dequeue(self):
        item = self.queue.dequeue()
        if item is not None:
            self.result_label.config(text=f"Dequeued: {item}")
        else:
            messagebox.showwarning("Operation Error", "Queue is empty. Cannot dequeue.")

    def traverse(self):
        result = self.queue.traverse()
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    gui = QueueGUI(root)
    root.mainloop()