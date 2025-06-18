
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __mull__(self, other):
        if self.currency == other.currency:
            return Money(self.amount * other.amount, self.currency)
        else:
            raise ValueError("Currency mismatch")

    

    def __str__(self):
        return f"{self.amount} {self.currency}"

m1 = Money(1000, "$")
m2 = Money(3000, "$")
m3 = Money(m1 m2)




