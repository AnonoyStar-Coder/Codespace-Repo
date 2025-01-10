import sqlite3
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

# Connect to (or create) the SQLite database
conn = sqlite3.connect('inventory.db')

# Create a cursor to interact with the database
c = conn.cursor()

# Create the products table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

# Commit and close the database connection
conn.commit()

# Button to Add Product
def add_product():
    product_name = product_name_entry.get()
    product_quantity = product_quantity_entry.get()

    # Add product to database
    try:
        c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, product_quantity))
        conn.commit()
        messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding product: {str(e)}")

add_product_button = tk.Button(root, text="Add Product", command=add_product)
add_product_button.pack(pady=10)

root.mainloop()
