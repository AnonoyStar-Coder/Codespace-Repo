import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create the products table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x600")

# Product Name
product_name_label = tk.Label(root, text="Product Name:")
product_name_label.pack(pady=5)
product_name_entry = tk.Entry(root)
product_name_entry.pack(pady=5)

# Product Quantity
product_quantity_label = tk.Label(root, text="Quantity:")
product_quantity_label.pack(pady=5)
product_quantity_entry = tk.Entry(root)
product_quantity_entry.pack(pady=5)

# Add Product Function
def add_product():
    product_name = product_name_entry.get()
    product_quantity = product_quantity_entry.get()

    try:
        c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, product_quantity))
        conn.commit()
        messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding product: {str(e)}")

# Add Product Button
add_product_button = tk.Button(root, text="Add Product", command=add_product)
add_product_button.pack(pady=10)

# Inventory Display
inventory_listbox = tk.Listbox(root)
inventory_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

def show_inventory():
    inventory_listbox.delete(0, tk.END)
    c.execute("SELECT name, quantity FROM products")
    rows = c.fetchall()
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Refresh Inventory Button
refresh_button = tk.Button(root, text="Refresh Inventory", command=show_inventory)
refresh_button.pack(pady=10)

# Search Functionality

# Search Label and Entry
search_label = tk.Label(root, text="Search by Product Name:")
search_label.pack(pady=5)
search_entry = tk.Entry(root)
search_entry.pack(pady=5)

# Search Function
def search_product():
    search_term = search_entry.get()
    
    if search_term:
        inventory_listbox.delete(0, tk.END)  # Clear current listbox content
        
        # Search for products that match the search term (using SQL LIKE for partial match)
        c.execute("SELECT name, quantity FROM products WHERE name LIKE ?", ('%' + search_term + '%',))
        rows = c.fetchall()
        
        if rows:
            for row in rows:
                inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")
        else:
            inventory_listbox.insert(tk.END, "No products found")
    else:
        messagebox.showwarning("Input Error", "Please enter a product name to search.")

# Search Button
search_button = tk.Button(root, text="Search", command=search_product)
search_button.pack(pady=10)

root.mainloop()
