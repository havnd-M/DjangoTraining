class test:

    pay_rent = 0.9

    def __init__(self, mony: float, price: float):
        assert mony >= 0, f"bla bla bla {mony} is not bigger than ziro"

        self.mony = mony
        self.price = price

    def pay_rent_discount(self):

        self.price = self.mony * test.pay_rent


t = test(10, 3)
t.pay_rent_discount()

print(t.price)
