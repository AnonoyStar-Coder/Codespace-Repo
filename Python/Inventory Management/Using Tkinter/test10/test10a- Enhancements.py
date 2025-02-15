import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create the products table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("400x600")
root.configure(bg="#f0f0f0")  # Light background color

# Product Name
product_name_label = tk.Label(root, text="Product Name:", bg="#f0f0f0")
product_name_label.pack(pady=5)
product_name_entry = tk.Entry(root, width=30)
product_name_entry.pack(pady=5)

# Product Quantity
product_quantity_label = tk.Label(root, text="Quantity:", bg="#f0f0f0")
product_quantity_label.pack(pady=5)
product_quantity_entry = tk.Entry(root, width=30)
product_quantity_entry.pack(pady=5)

# Add Product Function
def add_product():
    product_name = product_name_entry.get()
    product_quantity = product_quantity_entry.get()

    if not product_name or not product_quantity.isdigit():
        messagebox.showwarning("Input Error", "Please enter valid product name and quantity.")
        return

    try:
        c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, int(product_quantity)))
        conn.commit()
        messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")
        show_inventory()  # Refresh inventory display
    except Exception as e:
        messagebox.showerror("Error", f"Error adding product: {str(e)}")

# Add Product Button
add_product_button = tk.Button(root, text="Add Product", command=add_product, bg="#4CAF50", fg="white")
add_product_button.pack(pady=10)

# Inventory Display
inventory_listbox = tk.Listbox(root, width=50, height=15)
inventory_listbox.pack(pady=10)

# Function to show full inventory
def show_inventory():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products")  # Select all products from DB
    rows = c.fetchall()  # Fetch all rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Refresh Inventory Button
refresh_button = tk.Button(root, text="Refresh Inventory", command=show_inventory, bg="#2196F3", fg="white")
refresh_button.pack(pady=10)

# Search Functionality

# Search Label and Entry
search_label = tk.Label(root, text="Search by Product Name:", bg="#f0f0f0")
search_label.pack(pady=5)
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

# Search Function
def search_product():
    search_term = search_entry.get()
    
    if search_term:
        inventory_listbox.delete(0, tk.END)  # Clear current listbox content
        
        # Search for products that match the search term
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
search_button = tk.Button(root, text="Search", command=search_product, bg="#FF9800", fg="white")
search_button.pack(pady=10)

# Delete Functionality

# Function to delete the selected product with confirmation
def delete_product():
    try:
        selected_item_index = inventory_listbox.curselection()[0]
        selected_item = inventory_listbox.get(selected_item_index)
        
        product_name = selected_item.split(" - ")[0]  # Get the product name
        
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {product_name}?")
        if confirm:
            c.execute("DELETE FROM products WHERE name = ?", (product_name,))
            conn.commit()
            inventory_listbox.delete(selected_item_index)
            messagebox.showinfo("Product Deleted", f"{product_name} has been deleted.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a product to delete.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting product: {str(e)}")

# Delete Button
delete_button = tk.Button(root, text="Delete Product", command=delete_product, bg="#F44336", fg="white")
delete_button.pack(pady=10)

# Update Functionality

# Function to update the selected product
def update_product():
    try:
        selected_item_index = inventory_listbox.curselection()[0]
        selected_item = inventory_listbox.get(selected_item_index)

        product_name = selected_item.split(" - ")[0]
        current_quantity = selected_item.split(" - ")[1].split(" ")[0]  # Get the current quantity

        new_name = product_name_entry.get() or product_name  # If empty, keep current
        new_quantity = product_quantity_entry.get() or current_quantity  # If empty, keep current

        if not new_quantity.isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid quantity.")
            return

        c.execute("UPDATE products SET name = ?, quantity = ? WHERE name = ?", (new_name, int(new_quantity), product_name))
        conn.commit()

        inventory_listbox.delete(selected_item_index)
        inventory_listbox.insert(selected_item_index, f"{new_name} - {new_quantity} units")

        messagebox.showinfo("Product Updated", f"{product_name} has been updated.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a product to update.")
    except Exception as e:
        messagebox.showerror("Error", f"Error updating product: {str(e)}")

# Update Button
update_button = tk.Button(root, text="Update Product", command=update_product, bg="#FFC107", fg="white")
update_button.pack(pady=10)

# Sort by Name Functionality

# Function to sort the inventory by product name
def sort_inventory():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products ORDER BY name")  # Select and sort products by name
    rows = c.fetchall()  # Fetch all sorted rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Sort by Name Button
sort_name_button = tk.Button(root, text="Sort by Name", command=sort_inventory, bg="#9C27B0", fg="white")
sort_name_button.pack(pady=10)

# Sort by Quantity Functionality

# Function to sort the inventory by product quantity
def sort_inventory_by_quantity():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products ORDER BY quantity")  # Select and sort products by quantity
    rows = c.fetchall()  # Fetch all sorted rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Sort by Quantity Button
sort_quantity_button = tk.Button(root, text="Sort by Quantity", command=sort_inventory_by_quantity, bg="#9C27B0", fg="white")
sort_quantity_button.pack(pady=10)

# Show Inventory on Start
show_inventory()

# Main loop
root.mainloop()

# Close the database connection
conn.close()
