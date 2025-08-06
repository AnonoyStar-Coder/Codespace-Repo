import sys
import sqlite3
import csv
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QFileDialog)


class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Connect to the database
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()

        # Create the products table if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS products
                         (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')

        self.setWindowTitle("Inventory Management System")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Input Layout
        self.input_layout = QHBoxLayout()
        self.product_name_label = QLabel("Product Name:")
        self.product_name_entry = QLineEdit()
        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)
        
        self.product_quantity_label = QLabel("Quantity:")
        self.product_quantity_entry = QLineEdit()
        self.update_product_button = QPushButton("Update Product")
        self.update_product_button.clicked.connect(self.update_product)

        self.input_layout.addWidget(self.product_name_label)
        self.input_layout.addWidget(self.product_name_entry)
        self.input_layout.addWidget(self.add_product_button)
        self.input_layout.addWidget(self.product_quantity_label)
        self.input_layout.addWidget(self.product_quantity_entry)
        self.input_layout.addWidget(self.update_product_button)

        # Search Layout
        self.search_layout = QHBoxLayout()
        self.search_label = QLabel("Search by Product Name:")
        self.search_entry = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_product)

        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_entry)
        self.search_layout.addWidget(self.search_button)

        # Inventory Display
        self.inventory_listbox = QListWidget()

        # Adding all layouts to the main layout
        self.layout.addLayout(self.input_layout)
        self.layout.addLayout(self.search_layout)
        self.layout.addWidget(self.inventory_listbox)

        # Sorting Layout (moved to the bottom)
        self.sorting_layout = QHBoxLayout()
        self.sort_name_button = QPushButton("Sort by Name")
        self.sort_name_button.clicked.connect(lambda: self.sort_inventory("name"))
        
        self.sort_asc_button = QPushButton("Sort Ascending")
        self.sort_asc_button.clicked.connect(lambda: self.sort_inventory("asc"))

        self.sort_desc_button = QPushButton("Sort Descending")
        self.sort_desc_button.clicked.connect(lambda: self.sort_inventory("desc"))

        self.sorting_layout.addWidget(self.sort_name_button)
        self.sorting_layout.addWidget(self.sort_asc_button)
        self.sorting_layout.addWidget(self.sort_desc_button)

        # Button Layout (Delete and Save options)
        self.button_layout = QHBoxLayout()
        self.delete_product_button = QPushButton("Delete Product")
        self.delete_product_button.clicked.connect(self.delete_product)

        self.save_button = QPushButton("Save to CSV")
        self.save_button.clicked.connect(self.save_to_csv)

        self.button_layout.addWidget(self.delete_product_button)
        self.button_layout.addWidget(self.save_button)

        # Adding sorting and button layouts to the main layout
        self.layout.addLayout(self.sorting_layout)
        self.layout.addLayout(self.button_layout)

        # Show inventory on startup
        self.show_inventory()

    def add_product(self):
        product_name = self.product_name_entry.text()
        product_quantity = self.product_quantity_entry.text()

        if not product_name or not product_quantity.isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter valid product name and quantity.")
            return

        self.c.execute("SELECT * FROM products WHERE name = ?", (product_name,))
        if self.c.fetchone():
            QMessageBox.warning(self, "Input Error", "Product already exists. Please use a different name.")
            return

        try:
            self.c.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", 
                           (product_name, int(product_quantity)))
            self.conn.commit()
            QMessageBox.information(self, "Product Added", f"{product_name} - {product_quantity} units added.")
            self.show_inventory()  # Refresh inventory display
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error adding product: {str(e)}")

    def show_inventory(self):
        self.inventory_listbox.clear()  # Clear current listbox content
        self.c.execute("SELECT name, quantity FROM products")  # Select all products from DB
        rows = self.c.fetchall()  # Fetch all rows
        for row in rows:
            self.inventory_listbox.addItem(f"{row[0]} - {row[1]} units")

    def refresh_inventory(self):
        self.show_inventory()  # Refresh inventory display

    def delete_product(self):
        selected_item = self.inventory_listbox.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Selection Error", "Please select a product to delete.")
            return

        product_name = selected_item.text().split(" - ")[0]  # Get the product name
        confirm = QMessageBox.question(self, "Confirm Deletion", 
                                        f"Are you sure you want to delete {product_name}?",
                                        QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.c.execute("DELETE FROM products WHERE name = ?", (product_name,))
            self.conn.commit()
            self.inventory_listbox.takeItem(self.inventory_listbox.row(selected_item))
            QMessageBox.information(self, "Product Deleted", f"{product_name} has been deleted.")

    def update_product(self):
        selected_item = self.inventory_listbox.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Selection Error", "Please select a product to update.")
            return

        product_name = selected_item.text().split(" - ")[0]
        current_quantity = selected_item.text().split(" - ")[1].split(" ")[0]  # Get the current quantity

        new_name = self.product_name_entry.text() or product_name  # If empty, keep current
        new_quantity = self.product_quantity_entry.text() or current_quantity  # If empty, keep current

        if not new_quantity.isdigit():
            QMessageBox.warning(self, "Input Error", "Please enter a valid quantity.")
            return

        self.c.execute("UPDATE products SET name = ?, quantity = ? WHERE name = ?", 
                       (new_name, new_quantity, product_name))
        self.conn.commit()
        QMessageBox.information(self, "Product Updated", f"{new_name} updated to {new_quantity} units.")
        self.show_inventory()

    def search_product(self):
        search_term = self.search_entry.text()
        query = "SELECT name, quantity FROM products WHERE name LIKE ?"
        params = ['%' + search_term + '%']

        self.inventory_listbox.clear()  # Clear current listbox content
        self.c.execute(query, params)
        rows = self.c.fetchall()

        if rows:
            for row in rows:
                self.inventory_listbox.addItem(f"{row[0]} - {row[1]} units")
        else:
            self.inventory_listbox.addItem("No products found")

    def save_to_csv(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Inventory as CSV", "", 
                                                   "CSV files (*.csv);;All files (*)")
        if filename:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Product Name", "Quantity"])
                self.c.execute("SELECT name, quantity FROM products")
                rows = self.c.fetchall()
                writer.writerows(rows)
                QMessageBox.information(self, "Success", "Inventory saved to CSV successfully!")

    def sort_inventory(self, order):
        self.inventory_listbox.clear()  # Clear current listbox content

        if order == "name":
            self.c.execute("SELECT name, quantity FROM products ORDER BY name ASC")
        elif order == "asc":
            self.c.execute("SELECT name, quantity FROM products ORDER BY quantity ASC")
        elif order == "desc":
            self.c.execute("SELECT name, quantity FROM products ORDER BY quantity DESC")

        rows = self.c.fetchall()
        for row in rows:
            self.inventory_listbox.addItem(f"{row[0]} - {row[1]} units")

    def closeEvent(self, event):
        self.conn.close()  # Close database connection
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
