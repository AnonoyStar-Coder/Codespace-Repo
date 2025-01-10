import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x600")

# Label and Entry for Product Name
product_name_label = tk.Label(root, text="Product Name:")
product_name_label.pack(pady=5)
product_name_entry = tk.Entry(root)
product_name_entry.pack(pady=5)

# Label and Entry for Product Quantity
product_quantity_label = tk.Label(root, text="Quantity:")
product_quantity_label.pack(pady=5)
product_quantity_entry = tk.Entry(root)
product_quantity_entry.pack(pady=5)

# Button to Add Product
def add_product():
    product_name = product_name_entry.get()
    product_quantity = product_quantity_entry.get()
    # Logic for adding product will go here
    messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")

add_product_button = tk.Button(root, text="Add Product", command=add_product)
add_product_button.pack(pady=10)

root.mainloop()
