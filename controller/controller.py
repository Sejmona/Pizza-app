from static.model.pizza import Pizza
from static.model.topping import Topping
from static.model.order import Order
from static.model.sales import Sales
from view.ui import UI
from view.payment import PaymentUI
from view.admin import AdminUI

class Controller:
    def __init__(self):
        self.ui = UI()
        self.payment_ui = PaymentUI()
        self.admin_ui = AdminUI()
        self.sales = Sales()
        self.current_order = None

    def run(self):
        while True:
            self.ui.display_main_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_order()
            elif choice == '2':
                self.pay_order()
            elif choice == '3':
                self.admin_menu()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_order(self):
        self.current_order = Order()
        self.ui.display_order_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            pizza = Pizza("Margherita", 8.00)
            self.current_order.add_pizza(pizza)
        elif choice == '2':
            pizza = Pizza("Custom", 5.00)
            topping = Topping("Extra Cheese", 1.50)
            pizza.add_topping(topping)
            self.current_order.add_pizza(pizza)
        else:
            print("Invalid choice. Please try again.")
        print(f"Order Created:\n{self.current_order}")

    def pay_order(self):
        if self.current_order:
            print(f"Order Summary:\n{self.current_order}")
            print(f"Total: ${self.current_order.get_total():.2f}")
            self.payment_ui.display_payment_options()
            payment_choice = input("Choose payment method: ")

            if payment_choice in ['1', '2']:
                self.sales.record_sale(self.current_order)
                print("Order has been paid.")
                self.current_order = None
            else:
                print("Invalid payment option.")
        else:
            print("No order to pay.")

    def admin_menu(self):
        password = self.admin_ui.display_login()
        if password == "admin123":
            summary = self.sales.get_sales_summary()
            self.admin_ui.display_sales_summary(summary)
        else:
            print("Incorrect password.")
