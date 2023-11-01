order_books = []

def add_order():
    book = input("Enter book name: ")
    operation = input("Enter operation (BUY or SELL): ").upper()
    price = float(input("Enter price: "))
    volume = int(input("Enter volume: "))
    order_id = input("Enter order ID: ")

    if all([book, operation, price, volume, order_id]):
        new_order = {"price": price, "volume": volume, "orderId": order_id}

        book_exists = next((b for b in order_books if b["book"] == book), None)
        if not book_exists:
            book_exists = {"book": book, "buy": [], "sell": []}
            order_books.append(book_exists)

        if operation == "BUY":
            book_exists["buy"].append(new_order)
        elif operation == "SELL":
            book_exists["sell"].append(new_order)

        print("Order added:", new_order)
    else:
        print("Please fill in all the fields.")

def delete_order():
    book = input("Enter book name: ")
    order_id = input("Enter order ID: ")

    if all([book, order_id]):
        selected_book = next((b for b in order_books if b["book"] == book), None)
        if selected_book:
            selected_book["buy"] = [order for order in selected_book["buy"] if order["orderId"] != order_id]
            selected_book["sell"] = [order for order in selected_book["sell"] if order["orderId"] != order_id]
            print("Order deleted with ID:", order_id)
        else:
            print("Book not found:", book)
    else:
        print("Please enter book name and order ID.")

def process_orders():
    book_name = input("Enter book name: ")
    selected_book = next((b for b in order_books if b["book"] == book_name), None)

    if selected_book:
        print(f"Buy Orders for {book_name}:")
        for order in selected_book["buy"]:
            print(f"{order['volume']} @ {order['price']}")

        print(f"Sell Orders for {book_name}:")
        for order in selected_book["sell"]:
            print(f"{order['volume']} @ {order['price']}")
    else:
        print("Book not found. Please enter a valid book name.")

# Example usage
while True:
    print("\nOptions:")
    print("1. Add Order")
    print("2. Delete Order")
    print("3. Process Orders")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        delete_order()
    elif choice == "3":
        process_orders()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
