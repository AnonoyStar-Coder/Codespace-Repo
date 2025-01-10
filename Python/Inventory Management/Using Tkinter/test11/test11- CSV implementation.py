import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Create the products table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.state('zoomed')  # Open maximized
root.configure(bg="#f0f0f0")  # Light background color

# Create a frame for input fields
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.grid(row=0, column=0, padx=60, pady=60, sticky="nsew")

# Create a frame for output (Listbox)
output_frame = tk.Frame(root, bg="#f0f0f0")
output_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Configure grid weights for better resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# Configure row weight for better resizing
root.grid_rowconfigure(0, weight=1)

# Product Name
product_name_label = tk.Label(input_frame, text="Product Name:", bg="#f0f0f0")
product_name_label.grid(row=0, column=0, pady=5, sticky="w")
product_name_entry = tk.Entry(input_frame, width=30)
product_name_entry.grid(row=1, column=0, pady=5)

# Product Quantity
product_quantity_label = tk.Label(input_frame, text="Quantity:", bg="#f0f0f0")
product_quantity_label.grid(row=2, column=0, pady=5, sticky="w")
product_quantity_entry = tk.Entry(input_frame, width=30)
product_quantity_entry.grid(row=3, column=0, pady=5)

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
add_product_button = tk.Button(input_frame, text="Add Product", command=add_product, bg="#4CAF50", fg="white")
add_product_button.grid(row=4, column=0, pady=10)

# Inventory Display
inventory_listbox = tk.Listbox(output_frame, width=150, height=30)
inventory_listbox.pack(pady=10, padx=10)

# Function to show full inventory
def show_inventory():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products")  # Select all products from DB
    rows = c.fetchall()  # Fetch all rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Refresh Inventory Button
refresh_button = tk.Button(output_frame, text="Refresh Inventory", command=show_inventory, bg="#2196F3", fg="white")
refresh_button.pack(pady=10)

# Search Functionality

# Search Label and Entry
search_label = tk.Label(input_frame, text="Search by Product Name:", bg="#f0f0f0")
search_label.grid(row=5, column=0, pady=5, sticky="w")
search_entry = tk.Entry(input_frame, width=30)
search_entry.grid(row=6, column=0, pady=5)

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
search_button = tk.Button(input_frame, text="Search", command=search_product, bg="#FF9800", fg="white")
search_button.grid(row=7, column=0, pady=10)

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
delete_button = tk.Button(input_frame, text="Delete Product", command=delete_product, bg="#F44336", fg="white")
delete_button.grid(row=8, column=0, pady=10)

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
update_button = tk.Button(input_frame, text="Update Product", command=update_product, bg="#FFC107", fg="white")
update_button.grid(row=9, column=0, pady=10)

# Sort by Name Functionality

# Function to sort the inventory by product name
def sort_inventory():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products ORDER BY name")  # Select and sort products by name
    rows = c.fetchall()  # Fetch all sorted rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Sort by Name Button
sort_name_button = tk.Button(input_frame, text="Sort by Name", command=sort_inventory, bg="#9C27B0", fg="white")
sort_name_button.grid(row=10, column=0, pady=10)

# Sort by Quantity Functionality

# Function to sort the inventory by product quantity in ascending order
def sort_inventory_by_quantity():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products ORDER BY quantity")  # Select and sort products by quantity
    rows = c.fetchall()  # Fetch all sorted rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Sort by Quantity Button
sort_quantity_button = tk.Button(input_frame, text="Sort by Quantity (Ascending)", command=sort_inventory_by_quantity, bg="#9C27B0", fg="white")
sort_quantity_button.grid(row=11, column=0, pady=10)

# Function to sort the inventory by product quantity in decending order
def sort_inventory_by_quantity():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products ORDER BY quantity DESC")  # Select and sort products by quantity
    rows = c.fetchall()  # Fetch all sorted rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Sort by Quantity Button
sort_quantity_button = tk.Button(input_frame, text="Sort by Quantity (Decending)", command=sort_inventory_by_quantity, bg="#9C27B0", fg="white")
sort_quantity_button.grid(row=12, column=0, pady=10)

# Save Report Functionality
def save_report():
    # Ask for the file path
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                               filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Product Name", "Quantity"])  # Write header
                for item in inventory_listbox.get(0, tk.END):
                    name, quantity = item.split(" - ")
                    writer.writerow([name, quantity.split(" ")[0]])  # Write product name and quantity
            messagebox.showinfo("Report Saved", f"Report saved as: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving report: {str(e)}")

# Save Report Button
save_report_button = tk.Button(output_frame, text="Save Report", command=save_report, bg="#FF9800", fg="white")
save_report_button.pack(pady=10)

# Show Inventory on Start
show_inventory()

# Main loop
root.mainloop()

# Close the database connection when done
conn.close()
