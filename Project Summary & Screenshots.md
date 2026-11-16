# 📄 Project Summary: Mini E-Commerce System

## 📌 Overview
The **Mini E-Commerce System** is a console-based Python application designed to manage store inventory and handle customer purchases seamlessly. It separates user access into two distinct roles—**Admin** and **Customer**—ensuring secure inventory management while providing a smooth shopping experience.

---

## ⚙️ How the Code Works (Architecture)

1. **Data Management (`load_products` & `save_products`):**
   * Product records are stored in `products.txt` using a pipe-delimited format (`ID|Name|Price|Stock`).
   * At runtime, data is loaded into a global list of dictionaries for fast searching and manipulation.

2. **Search & Display (`find_products` & `show_products`):**
   * Case-insensitive product ID lookup ensures smooth user interaction.
   * Clean tabular formatting displays inventory details clearly in the terminal.

3. **Admin Operations (`admin_menu`):**
   * Provides full CRUD (Create, Read, Update, Delete) functionality with strict input validation (`try-except` blocks) to prevent invalid prices, negative stock, or formatting errors.

4. **Shopping & Billing (`customer_menu`):**
   * Uses a Python dictionary (`cart`) to map `product_id` to `quantity`.
   * During checkout, it verifies stock levels, updates the main product list, saves changes back to `products.txt`, and generates the final bill.

---

## 📸 Project Screenshots

*(Note: Replace the placeholders below with actual screenshots of your code execution and output before submitting on GitHub)*

### 1. Main Menu & Admin Panel
> ![Admin Menu Screenshot](screenshots/admin_menu.png)
> *Description: Adding and viewing products in the inventory.*

### 2. Customer Shopping & Cart
> ![Customer Cart Screenshot](screenshots/customer_cart.png)
> *Description: Browsing products and adding items to the shopping cart.*

### 3. Checkout & Bill Generation
> ![Checkout Screenshot](screenshots/checkout.png)
> *Description: Completing the purchase and updating stock in `products.txt`.*

---

## ✅ Conclusion
This project demonstrates practical implementation of file handling, data structures, and error handling in Python to build a real-world inventory and billing workflow.