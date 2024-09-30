# # CLI
# class HashTableWithChaining:
#     def __init__(self, size):
#         self.size = size
#         # Each index will have a list (bucket) to handle collisions
#         self.table = [[] for _ in range(size)]
        
#     def hash_function(self, key):
#         return key % self.size
    
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         # Check if the key already exists and update it if found
#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index][i] = (key, value)
#                 print(f'Updated: ({key}, {value}) at index {index} in bucket {i}')
#                 return
#         # If the key doesn't exist, append it
#         self.table[index].append((key, value))
#         print(f'Inserted: ({key}, {value}) at index {index}')
    
#     def delete(self, key):
#         index = self.hash_function(key)
#         # Search for the key in the chain (list)
#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 del self.table[index][i]
#                 print(f'Deleted: ({key}, {v}) from index {index}')
#                 return
#         print(f'Key {key} not found for deletion.')
    
#     def traverse(self):
#         print("Hash Table Contents with Chaining:")
#         for index, bucket in enumerate(self.table):
#             if bucket:
#                 print(f'Index {index}: {bucket}')
#             else:
#                 print(f'Index {index}: Empty')

# # Example usage
# if __name__ == "__main__":
#     hash_table = HashTableWithChaining(size=10)
#     # Inserting key-value pairs
#     hash_table.insert(1, 'A')
#     hash_table.insert(2, 'B')
#     hash_table.insert(3, 'C')
#     # Insert a collision to show chaining
#     hash_table.insert(11, 'X')  # 11 % 10 = 1, should go to the same index as key 1
#     # Traversing the hash table
#     hash_table.traverse()
#     # Deleting a key
#     hash_table.delete(2)
#     # Traversing the hash table again
#     hash_table.traverse()



# GUI
import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Separate chaining
        self.original_size = 0  # Tracks the original number of elements
    
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size  # Hashing based on string key
    
    def current_size(self):
        return sum(len(bucket) for bucket in self.table)
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value  # Update existing value
                return f'Updated: ({key}, {value}) at index {index}'
        self.table[index].append([key, value])
        return f'Inserted: ({key}, {value}) at index {index}'
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                deleted_value = kv[1]
                del self.table[index][i]
                return f'Deleted: ({key}, {deleted_value}) from index {index}'
        return f'Key {key} not found for deletion.'
    
    def traverse(self):
        return self.table

class HashTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Table GUI with Difference Display")
        self.hash_table = HashTable(size=10)
        self.previous_size = self.hash_table.current_size()

        # Input Frame for key-value pair insertion
        input_frame = tk.Frame(root, bg="lightgrey")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        self.key_label = tk.Label(input_frame, text="Key:", bg="lightgrey")
        self.key_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.key_entry = tk.Entry(input_frame)
        self.key_entry.grid(row=0, column=1, padx=5)

        self.value_label = tk.Label(input_frame, text="Value:", bg="lightgrey")
        self.value_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.value_entry = tk.Entry(input_frame)
        self.value_entry.grid(row=1, column=1, padx=5)

        # Buttons for operations
        self.insert_button = tk.Button(input_frame, text="Insert/Update", command=self.insert)
        self.insert_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(input_frame, text="Delete", command=self.delete)
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.traverse_button = tk.Button(input_frame, text="Show Hash Table", command=self.show_array)
        self.traverse_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Horizontal line separator
        separator = tk.Frame(root, height=2, bd=1, relief="sunken")
        separator.grid(row=0, column=1, padx=20, pady=10, sticky="ns")

        # Display section for the hash table
        display_frame = tk.Frame(root)
        display_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")

        # Result Frame for showing hash table content
        self.result_frame = tk.Frame(display_frame)
        self.result_frame.pack()

        self.array_labels = []
        for i in range(10):
            label = tk.Label(self.result_frame, text=f'Index {i}: None', borderwidth=1, relief='solid', width=30)
            label.grid(row=i, column=0, padx=5, pady=2)
            self.array_labels.append(label)

        # Display size difference
        self.size_frame = tk.Frame(root)
        self.size_frame.grid(row=1, column=0, columnspan=3, pady=10)

        self.size_label = tk.Label(self.size_frame, text="Size difference: 0 (Original: 0, Current: 0)")
        self.size_label.pack()

    def update_size_label(self):
        current_size = self.hash_table.current_size()
        size_diff = current_size - self.previous_size
        original_size = self.previous_size
        self.size_label.config(text=f"Size difference: {size_diff} (Original: {original_size}, Current: {current_size})")
        self.previous_size = current_size

    def insert(self):
        key = self.key_entry.get().strip()
        value = self.value_entry.get().strip()
        if key == "" or value == "":
            messagebox.showerror("Error", "Key and Value cannot be empty.")
            return
        result = self.hash_table.insert(key, value)
        messagebox.showinfo("Result", result)
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.show_array()
        self.update_size_label()

    def delete(self):
        key = self.key_entry.get().strip()
        if key == "":
            messagebox.showerror("Error", "Key cannot be empty.")
            return
        result = self.hash_table.delete(key)
        messagebox.showinfo("Result", result)
        self.key_entry.delete(0, tk.END)
        self.show_array()
        self.update_size_label()

    def show_array(self):
        contents = self.hash_table.traverse()
        for i, bucket in enumerate(contents):
            if not bucket:
                self.array_labels[i].config(text=f'Index {i}: None', bg="lightgrey")
            else:
                items = ', '.join([f'{key}:{value}' for key, value in bucket])
                self.array_labels[i].config(text=f'Index {i}: [{items}]', bg="lightblue")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
