# # CLI 
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, root, key):
#         if key < root.val:
#             if root.left is None:
#                 root.left = Node(key)
#             else:
#                 self._insert(root.left, key)
#         else:
#             if root.right is None:
#                 root.right = Node(key)
#             else:
#                 self._insert(root.right, key)

#     def delete(self, key):
#         self.root = self._delete(self.root, key)

#     def _delete(self, root, key):
#         if root is None:
#             return root
#         if key < root.val:
#             root.left = self._delete(root.left, key)
#         elif key > root.val:
#             root.right = self._delete(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             min_larger_node = self._get_min(root.right)
#             root.val = min_larger_node.val
#             root.right = self._delete(root.right, min_larger_node.val)
#         return root

#     def _get_min(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current

#     def inorder_traversal(self):
#         return self._inorder_traversal(self.root)

#     def _inorder_traversal(self, root):
#         res = []
#         if root:
#             res = self._inorder_traversal(root.left)
#             res.append(root.val)
#             res = res + self._inorder_traversal(root.right)
#         return res

#     def preorder_traversal(self):
#         return self._preorder_traversal(self.root)

#     def _preorder_traversal(self, root):
#         res = []
#         if root:
#             res.append(root.val)
#             res = res + self._preorder_traversal(root.left)
#             res = res + self._preorder_traversal(root.right)
#         return res

#     def postorder_traversal(self):
#         return self._postorder_traversal(self.root)

#     def _postorder_traversal(self, root):
#         res = []
#         if root:
#             res = self._postorder_traversal(root.left)
#             res = res + self._postorder_traversal(root.right)
#             res.append(root.val)
#         return res


# if __name__ == "__main__":
#     bt = BinaryTree()

#     while True:
#         print("\n1. Insert")
#         print("2. Delete")
#         print("3. Inorder Traversal")
#         print("4. Preorder Traversal")
#         print("5. Postorder Traversal")
#         print("6. Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             key = int(input("Enter the value to insert: "))
#             bt.insert(key)
#         elif choice == 2:
#             key = int(input("Enter the value to delete: "))
#             bt.delete(key)
#         elif choice == 3:
#             print("Inorder traversal: ", bt.inorder_traversal())
#         elif choice == 4:
#             print("Preorder traversal: ", bt.preorder_traversal())
#         elif choice == 5:
#             print("Postorder traversal: ", bt.postorder_traversal())
#         elif choice == 6:
#             break
#         else:
#             print("Invalid choice! Please try again.")



# # GUI
import customtkinter as ctk
from tkinter import messagebox

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        res = []
        if root:
            res = self._inorder_traversal(root.left)
            res.append(root.val)
            res = res + self._inorder_traversal(root.right)
        return res

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self._preorder_traversal(root.left)
            res = res + self._preorder_traversal(root.right)
        return res

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, root):
        res = []
        if root:
            res = self._postorder_traversal(root.left)
            res = res + self._postorder_traversal(root.right)
            res.append(root.val)
        return res


class BinaryTreeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Binary Tree Operations")
        self.geometry("400x300")

        self.tree = BinaryTree()

        self.label = ctk.CTkLabel(self, text="Binary Tree Operations", font=("Arial", 16))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter a value")
        self.entry.pack(pady=5)

        self.insert_button = ctk.CTkButton(self, text="Insert", command=self.insert_value)
        self.insert_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self, text="Delete", command=self.delete_value)
        self.delete_button.pack(pady=5)

        self.inorder_button = ctk.CTkButton(self, text="Inorder Traversal", command=self.show_inorder)
        self.inorder_button.pack(pady=5)

        self.preorder_button = ctk.CTkButton(self, text="Preorder Traversal", command=self.show_preorder)
        self.preorder_button.pack(pady=5)

        self.postorder_button = ctk.CTkButton(self, text="Postorder Traversal", command=self.show_postorder)
        self.postorder_button.pack(pady=5)

        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

    def insert_value(self):
        try:
            key = int(self.entry.get())
            self.tree.insert(key)
            messagebox.showinfo("Success", f"Value {key} inserted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
        self.entry.delete(0, 'end')

    def delete_value(self):
        try:
            key = int(self.entry.get())
            self.tree.delete(key)
            messagebox.showinfo("Success", f"Value {key} deleted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
        self.entry.delete(0, 'end')

    def show_inorder(self):
        traversal = self.tree.inorder_traversal()
        messagebox.showinfo("Inorder Traversal", f"Inorder: {traversal}")

    def show_preorder(self):
        traversal = self.tree.preorder_traversal()
        messagebox.showinfo("Preorder Traversal", f"Preorder: {traversal}")

    def show_postorder(self):
        traversal = self.tree.postorder_traversal()
        messagebox.showinfo("Postorder Traversal", f"Postorder: {traversal}")


if __name__ == "__main__":
    app = BinaryTreeApp()
    app.mainloop()
