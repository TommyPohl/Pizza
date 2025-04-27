from views.paymentMenu import show_payment_menu
from views.orderMenu import show_order_menu
from views.mainMenu import MainMenu

class mainController:
    def __init__(self):
        self.menu = MainMenu()

    def run(self):
        self.menu.display()

class mainController:
    def __init__(self):
        self.main_menu = MainMenu()
        self.order_menu = show_order_menu()

    def run(self):
        while True:
            choice = self.main_menu.display()
            if choice == "1":
                self.order_menu.display()
            elif choice == "3":
                print("Děkujeme za použití systému. Nashledanou!")
                break
            else:
                print("Neplatná volba.")