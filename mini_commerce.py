from pathlib import Path
DATA_FILE = Path(__file__).with_name("products.txt")
products= []

def load_products():
    """Load products from the text file."""
    global products
    products = []
    if not DATA_FILE.exists():
        DATA_FILE.write_text("",encoding="utf-8")
        return

    with DATA_FILE.open("r",encoding="utf-8")as file:
        for line in file:
            parts=line.strip().split("l")
            if len(parts) !=4:
                continue
            product_id,name,price,stock=parts
            try:
                products.append({
                    "id":product_id,
                    "name":name,
                    "price":float(price),
                    "stock":int(stock)
                })
            except ValueError:
                print(f"Skipping invalid record:{line.strip()}")

def save_products():
  """Save all products to the text file."""
  with DATA_FILE.open("w",encoding="utf-8")as file:
      for product in products:
          file.write(
            f"{product['id']}|{product['name']}|"
            f"{product['price']}|{product['stock']}\n"  
          )

def find_products(product_id):
    for product in products:
        if product["id"].lower()==product_id.lower():
            return product
    return None

def show_products():
    if not products:
        print("\nNo products available.")
        return
    print("\n"+"-*65")
    print("      PRODUCT LIST")
    print("-"* 65)
    print("ID\tName\t\tPrice\t\tStock")
    print("-"* 65)

    for product in products:
        print(
            f"{product["id"]}\t"
            f"{product['name']}\t\t"
            f"{product['price']}\t\t"
            f"{product['stock']}"
        )
    print("-"* 65)

#Add new product
def add_product():
    product_id = input("Enter Product ID: ")
    if find_products(product_id):
        print("Product ID already exists.")
        return
    name = input("Enter Product Name:")

    if not name.strip() or "I" in name:
        print("Invalid product name.")
        return
    try:
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock:"))

        if price <= 0 or stock < 0:
            print("Price must be positive and stock cannot be negative.")
            return
    except ValueError:
        print("Please enter valid price and stock.")
        return

    products.append({
        "id":product_id,
        "name":name,
        "price":price,
        "stock":stock
    })
    save_products()
    print("Product added successfully!")

#Update existing product
def update_product():
    product_id = input("Enter Product ID to update:")
    product = find_products(product_id)

    if product is None:
        print("Product not found")
        return
    print("Press Enter to keep the old value.")

    name = input(f"Enter new name({product['name']}):")
    price = input(f"Enter new price({product['price']}):")
    stock = input(f"Enter new stock({product['stock']}):")
    if name.strip():
        if"I" in name:
            print("Invalid product name.")
            return
        product["name"] = name

    try:
        if price.strip():
            new_price = float(price)
            if new_price <= 0:
                print("Price must be positive.")
                return
            product["price"] = new_price

        if stock.strip():
            new_stock = int(stock)
            if new_stock < 0:
                print("Stock cannot be negative.")
                return
            product["stock"] = new_stock

    except ValueError:
        print("Invalid price or stock.")
        return
    save_products()
    print("Product updated successfully!")

#Delete product
def delete_product():
    product_id = input("Enter Product ID to delete:")
    product = find_products(product_id)

    if product is None:
        print("Product not found.")
        return
    products.remove(product)
    save_products()

    print("Product deleted successfully!")

#Admin menu
def admin_menu():
    while True:
        print("\n==========ADMIN MENU==========")
        print("1.Add Product")
        print("2.View Products")
        print("3.Update Product")
        print("4.Delete Product")
        print("5.Back to Main Menu")

        choice = input("Enter your choice:")

        if choice == "1":
            add_product()
        elif choice == "2":
            show_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

#Customer menu
def customer_menu():
    cart = {}
    while True:
        print("\n==========CUSTOMER MENU==========")
        print("1.View Products")
        print("2.Add to Cart")
        print("3.View Cart")
        print("4.Checkout")
        print("5.Back to Main Menu")

        choice = input("Enter your choice:")
        if choice == "1":
            show_products()
        if choice == "2":
            show_products()
            product_id = input("Enter Product ID:")
            product = find_products(product_id)
            if product is None:
                print("Product not found.")

            else:
                try:
                    quantity=int(input("Enter quantity:"))
                    if quantity <= 0:
                        print("Quantity must be greater than zero.")

                    elif quantity>product["stock"]:
                        print("Not enough stock available.")

                    else:
                        cart[product["id"]] = (
                            cart.get(product["id"],0) + quantity
                        )
                        print("Product added to cart!")
                except ValueError:
                    print("Please enter a valid quantity.")
        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                total=0
                print("\n==========YOUR CART==========")  
                for product_id, quantity in cart.items():
                    product=find_products(product_id)
                    amount = product["price"]*quantity
                    total += amount
                    print(
                        product["name"],
                        "Quantity:",quantity,
                        "Amount:" ,amount

                    )
                print("Total Amount:",total)
        elif choice == "4":
            if not cart:
                print("Your cart is empty.")
                continue

            valid = True
            #Check stock before checkout
            for product_id, quantity in cart.items():
                product = find_products(product_id)

                total+=product["price"]*quantity
                product["stock"]-=quantity

                save_products()
                print("Order placed successfully!")
                print("Total Bill:",total)
                cart.clear()
            else:
              print("Checkout failed.")
        elif choice=="5":
            break
        else:
            print("Invalid choice")




#Main function
def main():
    load_products()
    while True:
        print("\n==========MINI E-COMMERCE SYSTEM==========")
        print("1.Admin")
        print("2.Customer")
        print("3.Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            admin_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Try again.")

#Program execution starts here
if __name__ =="__main__":
    main()



        


    
        
            

            








