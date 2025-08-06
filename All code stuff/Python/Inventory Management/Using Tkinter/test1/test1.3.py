import tkinter as tk
from tkinter import ttk, messagebox, filedialog
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
root.configure(bg="#EAEDED")  # Light grey background color

# Create a frame for input fields
input_frame = tk.Frame(root, bg="#F9E79F", bd=5, relief="ridge")  # Soft yellow for input frame
input_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")

# Create a frame for output (Listbox)
output_frame = tk.Frame(root, bg="#D5DBDB", bd=5, relief="ridge")  # Soft grey for output frame
output_frame.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

# Configure grid weights for better resizing
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_rowconfigure(0, weight=1)

# Custom Button Style using ttk
style = ttk.Style()
style.configure("Rounded.TButton",
                padding=6,
                relief="flat",
                background="#2980B9",  # Blue color
                foreground="black",  # Black font color
                font=("Helvetica", 10, "bold"))

# Product Name
product_name_label = tk.Label(input_frame, text="Product Name:", bg="#F9E79F", font=("Helvetica", 12, "bold"))
product_name_label.grid(row=0, column=0, pady=5, sticky="w")
product_name_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 11))
product_name_entry.grid(row=1, column=0, pady=5)

# Product Quantity
product_quantity_label = tk.Label(input_frame, text="Quantity:", bg="#F9E79F", font=("Helvetica", 12, "bold"))
product_quantity_label.grid(row=2, column=0, pady=5, sticky="w")
product_quantity_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 11))
product_quantity_entry.grid(row=3, column=0, pady=5)

# Modify Add Product Function
def add_product():
    product_name = product_name_entry.get()
    product_quantity = product_quantity_entry.get()

    if not product_name or not product_quantity.isdigit():
        messagebox.showwarning("Input Error", "Please enter valid product name and quantity.")
        return

    c.execute("SELECT * FROM products WHERE name = ?", (product_name,))
    if c.fetchone():
        messagebox.showwarning("Input Error", "Product already exists. Please use a different name.")
        return

    # Continue with the insert
    try:
        c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, int(product_quantity)))
        conn.commit()
        messagebox.showinfo("Product Added", f"{product_name} - {product_quantity} units added.")
        show_inventory()  # Refresh inventory display
    except Exception as e:
        messagebox.showerror("Error", f"Error adding product: {str(e)}")

# Handle closing
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Inventory Display
inventory_listbox = tk.Listbox(output_frame, width=100, height=30, font=("Helvetica", 11))
inventory_listbox.pack(pady=10, padx=10)

# Function to show full inventory
def show_inventory():
    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute("SELECT name, quantity FROM products")  # Select all products from DB
    rows = c.fetchall()  # Fetch all rows
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Refresh Functionality
def refresh_inventory():
    show_inventory()  # Refresh inventory display

# Create buttons in a grid layout
button_frame = tk.Frame(input_frame, bg="#F9E79F")
button_frame.grid(row=4, column=0, pady=10)

# Center the Add Product Button
add_product_button = ttk.Button(button_frame, text="Add Product", command=add_product, style="Rounded.TButton")
add_product_button.grid(row=0, column=0, padx=5)

# Space after Add Product Button
tk.Label(button_frame, bg="#F9E79F").grid(row=1, column=0, pady=10)  # Adding an empty label for spacing

# Search Functionality
search_label = tk.Label(input_frame, text="Search by Product Name:", bg="#F9E79F", font=("Helvetica", 12, "bold"))
search_label.grid(row=5, column=0, pady=5, sticky="w")
search_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 11))
search_entry.grid(row=6, column=0, pady=5)

# Add quantity range fields for advanced search
min_quantity_label = tk.Label(input_frame, text="Min Quantity:", bg="#F9E79F", font=("Helvetica", 12, "bold"))
min_quantity_label.grid(row=7, column=0, pady=5, sticky="w")
min_quantity_entry = tk.Entry(input_frame, width=10, font=("Helvetica", 11))
min_quantity_entry.grid(row=8, column=0, pady=5, sticky="w")

max_quantity_label = tk.Label(input_frame, text="Max Quantity:", bg="#F9E79F", font=("Helvetica", 12, "bold"))
max_quantity_label.grid(row=9, column=0, pady=5, sticky="w")
max_quantity_entry = tk.Entry(input_frame, width=10, font=("Helvetica", 11))
max_quantity_entry.grid(row=10, column=0, pady=5, sticky="w")

# Search Function
def search_product():
    search_term = search_entry.get()
    min_quantity = min_quantity_entry.get()
    max_quantity = max_quantity_entry.get()

    query = "SELECT name, quantity FROM products WHERE 1=1"
    params = []

    if search_term:
        query += " AND name LIKE ?"
        params.append('%' + search_term + '%')

    if min_quantity.isdigit():
        query += " AND quantity >= ?"
        params.append(int(min_quantity))

    if max_quantity.isdigit():
        query += " AND quantity <= ?"
        params.append(int(max_quantity))

    inventory_listbox.delete(0, tk.END)  # Clear current listbox content
    c.execute(query, params)
    rows = c.fetchall()

    if rows:
        for row in rows:
            inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")
    else:
        inventory_listbox.insert(tk.END, "No products found")

# Search Button
search_button = ttk.Button(input_frame, text="Search", command=search_product, style="Rounded.TButton")
search_button.grid(row=11, column=0, pady=10)

# Delete Functionality
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

# Update Functionality
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

        c.execute("UPDATE products SET name = ?, quantity = ? WHERE name = ?", (new_name, new_quantity, product_name))
        conn.commit()
        messagebox.showinfo("Product Updated", f"{new_name} updated to {new_quantity} units.")
        show_inventory()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a product to update.")
    except Exception as e:
        messagebox.showerror("Error", f"Error updating product: {str(e)}")

# Add More Buttons (Update, Delete, Refresh)
update_button = ttk.Button(button_frame, text="Update Product", command=update_product, style="Rounded.TButton")
update_button.grid(row=0, column=1, padx=5)

delete_button = ttk.Button(button_frame, text="Delete Product", command=delete_product, style="Rounded.TButton")
delete_button.grid(row=0, column=2, padx=5)

refresh_button = ttk.Button(button_frame, text="Refresh Inventory", command=refresh_inventory, style="Rounded.TButton")
refresh_button.grid(row=0, column=3, padx=5)

# Create sorting buttons and save button
sorting_frame = tk.Frame(output_frame, bg="#D5DBDB")
sorting_frame.pack(pady=10)

# Add sort by name button
sort_name_button = ttk.Button(sorting_frame, text="Sort by Name", command=lambda: sort_inventory("name"), style="Rounded.TButton")
sort_name_button.pack(side=tk.LEFT, padx=5)

# Existing sorting buttons
sort_asc_button = ttk.Button(sorting_frame, text="Sort Ascending", command=lambda: sort_inventory("asc"), style="Rounded.TButton")
sort_asc_button.pack(side=tk.LEFT, padx=5)

sort_desc_button = ttk.Button(sorting_frame, text="Sort Descending", command=lambda: sort_inventory("desc"), style="Rounded.TButton")
sort_desc_button.pack(side=tk.LEFT, padx=5)

# Save to CSV Functionality
def save_to_csv():
    filename = filedialog.asksaveasfilename(defaultextension=".csv",
                                              filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if filename:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Quantity"])
            c.execute("SELECT name, quantity FROM products")
            rows = c.fetchall()
            writer.writerows(rows)
            messagebox.showinfo("Success", "Inventory saved to CSV successfully!")

# Save Button
save_button = ttk.Button(sorting_frame, text="Save to CSV", command=save_to_csv, style="Rounded.TButton")
save_button.pack(side=tk.LEFT, padx=5)

# Function to sort the inventory
def sort_inventory(order):
    inventory_listbox.delete(0, tk.END)

    if order == "asc":
        c.execute("SELECT name, quantity FROM products ORDER BY name ASC")
    elif order == "desc":
        c.execute("SELECT name, quantity FROM products ORDER BY name DESC")
    else:
        c.execute("SELECT name, quantity FROM products ORDER BY name")

    rows = c.fetchall()
    for row in rows:
        inventory_listbox.insert(tk.END, f"{row[0]} - {row[1]} units")

# Start with showing inventory
show_inventory()

# Run the application
root.mainloop()
