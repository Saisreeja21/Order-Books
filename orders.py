class OrderBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, operation, price, volume, order_id):
        new_order = {"price": price, "volume": volume, "orderId": order_id}
        if operation == "BUY":
            self.buy_orders.append(new_order)
        elif operation == "SELL":
            self.sell_orders.append(new_order)
        print("Order added:", new_order)

    def delete_order(self, order_id):
        self.buy_orders = [order for order in self.buy_orders if order["orderId"] != order_id]
        self.sell_orders = [order for order in self.sell_orders if order["orderId"] != order_id]
        print("Order deleted with ID:", order_id)

    def process_orders(self):
        print(f"Buy Orders for {self.book_name}:")
        for order in self.buy_orders:
            print(f"{order['volume']} @ {order['price']}")

        print(f"Sell Orders for {self.book_name}:")
        for order in self.sell_orders:
            print(f"{order['volume']} @ {order['price']}")


if __name__ == "__main__":
    order_books = []

    while True:
        print("\nOptions:")
        print("1. Add Order")
        print("2. Delete Order")
        print("3. Process Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter book name: ")
            order_book = next((b for b in order_books if b.book_name == book_name), None)
            if not order_book:
                order_book = OrderBook(book_name)
                order_books.append(order_book)
            order_book.add_order(
                input("Enter operation (BUY or SELL): ").upper(),
                float(input("Enter price: ")),
                int(input("Enter volume: ")),
                input("Enter order ID: ")
            )
        elif choice == "2":
            book_name = input("Enter book name: ")
            order_book = next((b for b in order_books if b.book_name == book_name), None)
            if order_book:
                order_book.delete_order(input("Enter order ID: "))
            else:
                print("Book not found:", book_name)
        elif choice == "3":
            book_name = input("Enter book name: ")
            order_book = next((b for b in order_books if b.book_name == book_name), None)
            if order_book:
                order_book.process_orders()
            else:
                print("Book not found. Please enter a valid book name.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
