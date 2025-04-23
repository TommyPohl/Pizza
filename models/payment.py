class Payment:
    def __init__(self, amount, method="cash"):
        self.amount = amount
        self.method = method
        self.paid = False

    def process_payment(self):
        if self.amount <= 0:
            raise ValueError("Částka musí být větší než 0.")

        print(f"Zpracovávám platbu ve výši {self.amount:.2f} Kč pomocí '{self.method}'.")
        self.paid = True
        return True

    def is_paid(self):
        return self.paid

    def __repr__(self):
        status = "ZAPLACENO" if self.paid else "NEZAPLACENO"
        return f"<Platba: {self.amount:.2f} Kč | Metoda: {self.method} | Stav: {status}>"
