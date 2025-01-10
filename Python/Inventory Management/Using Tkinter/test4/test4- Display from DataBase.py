import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("400x300")

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
    # Logic for adding product will go here
    messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")

add_product_button = tk.Button(root, text="Add Product", command=add_product)
add_product_button.pack(pady=10)

# Listbox to display inventory
inventory_listbox = tk.Listbox(root)
inventory_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Function to display the inventory
def show_inventory():
    # Clear current listbox
    inventory_listbox.delete(0, tk.END)
    
    # Fetch products from database
    c.execute("SELECT name, quantity FROM products")
    rows = c.fetchall()
    
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Button to refresh the inventory display
refresh_button = tk.Button(root, text="Refresh Inventory", command=show_inventory)
refresh_button.pack(pady=10)

root.mainloop()
