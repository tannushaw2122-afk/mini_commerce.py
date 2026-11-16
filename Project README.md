# 🛒 Mini E-Commerce System (Python)

A command-line interface (CLI) based **Mini E-Commerce System** built using Python. This project simulates a basic retail inventory and shopping cart system with persistent data storage using a local text file (`products.txt`).

---

## 🚀 Features

### 1. Persistent Data Storage
* Uses Python's `pathlib` module to automatically create and manage a `products.txt` file.
* Reads existing inventory on startup and saves every addition, update, deletion, or purchase immediately.

### 2. Admin Panel
* **Add Product:** Add new products with a unique ID, name, price, and stock quantity (includes validation against negative values and duplicate IDs).
* **View Products:** Displays all available products in a formatted table (`ID`, `Name`, `Price`, `Stock`).
* **Update Product:** Modify the name, price, or stock of an existing product by its ID (press Enter to retain existing values).
* **Delete Product:** Remove discontinued or unwanted products from the inventory.

### 3. Customer Panel
* **View Products:** Browse the catalog of available items and check current stock.
* **Add to Cart:** Select products by ID and specify desired quantities (validates stock availability).
* **View Cart:** Review items added to the cart, individual item totals, and the overall grand total.
* **Checkout:** Validates final stock, calculates the total bill, automatically deducts purchased quantities from inventory, updates `products.txt`, and clears the cart.

---

## 🛠️ Technologies & Concepts Used
* **Language:** Python 3
* **Modules:** `pathlib` (File handling)
* **Core Concepts:** File I/O (`read`/`write`), Exception Handling (`try-except` for `ValueError`), Functions & Modular Programming, Loops & Conditional Statements, Lists & Dictionaries.

---

## 💻 How to Run the Project

1. Make sure you have **Python 3** installed on your system.
2. Clone this repository or download the `python project.py` file.
3. Open your terminal/command prompt in the project folder and run:
   ```bash
   python "python project.py"
   ```
4. A `products.txt` file will be generated automatically in the same directory to store your inventory data.