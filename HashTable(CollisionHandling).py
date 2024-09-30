# # # CLI
# class Node:
#     def __init__(self, key, value):
#         """Node for the linked list used in overflow chaining."""
#         self.key = key
#         self.value = value
#         self.next = None


# class HashTable:
#     def __init__(self, size=10):
#         """Initialize the hash table with a given size."""
#         self.size = size
#         self.table = [None] * size
#         self.count = 0  # Keep track of the number of elements

#     def hash_function(self, key):
#         """Hash function to determine the index for a given key."""
#         return key % self.size

#     def resize(self):
#         """Resize the hash table when load factor exceeds 0.7."""
#         old_table = self.table
#         self.size *= 2  # Double the size
#         self.table = [None] * self.size
#         self.count = 0  # Reset count and reinsert elements

#         for node in old_table:
#             current = node
#             while current:
#                 self.insert(current.key, current.value)
#                 current = current.next

#     def load_factor(self):
#         """Calculate the current load factor of the hash table."""
#         return self.count / self.size

#     def insert(self, key, value):
#         """Insert a key-value pair into the hash table."""
#         index = self.hash_function(key)
#         new_node = Node(key, value)

#         if self.table[index] is None:
#             self.table[index] = new_node
#         else:
#             current = self.table[index]
#             while current.next:
#                 # Update the value if the key already exists
#                 if current.key == key:
#                     current.value = value
#                     return
#                 current = current.next
#             current.next = new_node

#         self.count += 1  # Increment the count of elements
#         if self.load_factor() > 0.7:  # Check if resize is needed
#             self.resize()

#     def delete(self, key):
#         """Delete the value associated with the given key."""
#         index = self.hash_function(key)
#         current = self.table[index]
#         prev = None

#         while current:
#             if current.key == key:
#                 if prev:
#                     prev.next = current.next
#                 else:
#                     self.table[index] = current.next
#                 self.count -= 1  # Decrement count when an item is deleted
#                 return
#             prev = current
#             current = current.next

#     def search(self, key):
#         """Search for the value associated with the given key."""
#         index = self.hash_function(key)
#         current = self.table[index]

#         while current:
#             if current.key == key:
#                 return current.value
#             current = current.next

#         return None

#     def traverse(self):
#         """Traverse and print all key-value pairs in the hash table."""
#         for index, node in enumerate(self.table):
#             current = node
#             if current is not None:
#                 while current:
#                     print(f"Index {index}: Key {current.key}, Value {current.value}")
#                     current = current.next
#             else:
#                 print(f"Index {index}: None")


# # Example Usage
# if __name__ == "__main__":
#     # Create a hash table with a fixed size of 10
#     hash_table = HashTable(size=10)

#     # Insert some values
#     hash_table.insert(1, "Value for key 1")
#     hash_table.insert(2, "Value for key 2")
#     hash_table.insert(12, "Value for key 12")  # This will go to the same index as key 2

#     # Traverse and print the hash table
#     print("Hash Table after insertions:")
#     hash_table.traverse()

#     # Search for values
#     print("\nSearching for key 2:")
#     print(hash_table.search(2))  # Should print: Value for key 2

#     print("Searching for key 1:")
#     print(hash_table.search(1))  # Should print: Value for key 1

#     print("Searching for key 12:")
#     print(hash_table.search(12))  # Should print: Value for key 12

#     # Delete a value
#     hash_table.delete(2)

#     # Traverse and print the hash table after deletion
#     print("\nHash Table after deletion:")
#     hash_table.traverse()

#     # Search for deleted key
#     print("\nSearching for deleted key 2:")
#     print(hash_table.search(2))  # Should print: None




# GUI
import tkinter as tk
from tkinter import messagebox

class Node:
    """Node for the linked list used in separate chaining."""
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None for _ in range(size)]

    def _ascii_hash_function(self, key):
        """Compute hash code using ASCII values."""
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.size

    def insert(self, key):
        """Insert key into the hash table."""
        index = self._ascii_hash_function(key)
        new_node = Node(key)

        # Insert into the linked list at the index
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:  # Update existing key
                    return
                current = current.next
            current.next = new_node

    def remove(self, key):
        """Remove key from the hash table."""
        index = self._ascii_hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def contains(self, key):
        """Check if key exists in the hash table."""
        index = self._ascii_hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def display(self):
        """Return the contents of the hash table as a list."""
        result = []
        for i in range(self.size):
            bucket = []
            current = self.table[i]
            while current:
                bucket.append(current.key)
                current = current.next
            result.append(bucket)
        return result

    def hash_code(self, key):
        """Return ASCII sum and hash code for a given key."""
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum, ascii_sum % self.size

class HashTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Table with Separate Chaining")
        self.hash_table = HashTable()
        self.root.geometry("600x500")

        self.label = tk.Label(root, text="Hash Table with Collisions Handling", font=("Arial", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=20)

        self.display_area = tk.Text(root, height=12, width=50, font=("Arial", 14))
        self.display_area.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

        self.hash_code_label = tk.Label(root, text="Hash Code (ASCII Sum)", font=("Arial", 16, "bold"))
        self.hash_code_label.grid(row=2, column=0, pady=20)

        self.hash_code_value = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.hash_code_value.grid(row=2, column=1, pady=20)

        self.entry = tk.Entry(root, width=30, font=("Arial", 16))
        self.entry.grid(row=3, column=0, columnspan=2, pady=20)

        self.add_btn = tk.Button(root, text="Add", command=self.add, width=10, font=("Arial", 14))
        self.add_btn.grid(row=4, column=0, padx=10, pady=10)

        self.remove_btn = tk.Button(root, text="Remove", command=self.remove, width=10, font=("Arial", 14))
        self.remove_btn.grid(row=4, column=1, padx=10, pady=10)

        self.contains_btn = tk.Button(root, text="Contains", command=self.contains, width=10, font=("Arial", 14))
        self.contains_btn.grid(row=5, column=0, padx=10, pady=10)

        self.size_btn = tk.Button(root, text="Size", command=self.size, width=10, font=("Arial", 14))
        self.size_btn.grid(row=5, column=1, padx=10, pady=10)

        self.update_display()

    def update_display(self):
        """Update the display area with the contents of the hash table."""
        self.display_area.delete('1.0', tk.END)
        hash_table = self.hash_table.display()
        for i, bucket in enumerate(hash_table):
            if bucket:
                items = ' -> '.join(bucket)
                self.display_area.insert(tk.END, f"{i}: {items}\n")
            else:
                self.display_area.insert(tk.END, f"{i}: (empty)\n")

    def update_hash_code(self, key):
        """Update the hash code display based on the current key."""
        ascii_sum, hash_code = self.hash_table.hash_code(key)
        self.hash_code_value.config(text=f"Sum of ASCII: {ascii_sum}, Hash Code: {ascii_sum} % {self.hash_table.size} = {hash_code}")

    def add(self):
        """Add a key to the hash table."""
        key = self.entry.get().strip()
        if key:
            self.hash_table.insert(key)
            self.update_hash_code(key)
            self.update_display()

    def remove(self):
        """Remove a key from the hash table."""
        key = self.entry.get().strip()
        if key:
            self.hash_table.remove(key)
            self.update_hash_code(key)
            self.update_display()

    def contains(self):
        """Check if a key exists in the hash table."""
        key = self.entry.get().strip()
        if key:
            found = self.hash_table.contains(key)
            if found:
                messagebox.showinfo("Result", f"'{key}' is in the hash table.")
            else:
                messagebox.showinfo("Result", f"'{key}' is not in the hash table.")
            self.update_hash_code(key)

    def size(self):
        """Show the total number of keys in the hash table."""
        total_size = sum(len(bucket) for bucket in self.hash_table.display())
        messagebox.showinfo("Size", f"Hash table contains {total_size} elements.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
