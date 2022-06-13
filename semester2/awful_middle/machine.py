"""middle task. Vending machine"""


class VendingMachine:
    """Parent class for different kinds of Vending Machine."""

class TextMachine(VendingMachine):
    """Class to represent Text Machine.
    Attributes:
    ------------
        price1: int
        price2: int
        text1: int
        text2: int
    """

    def __init__(self, type1, type2):
        self.price1 = type1[1]
        self.price2 = type2[1]
        self.text1 = type1[0]
        self.text2 = type2[0]

    def __str__(self):
        if self.text1 != 0 and self.text2 != 0:
            price1 = self.price_to_str(self.price1)
            price2 = self.price_to_str(self.price2)
            return f"Text Machine:<{self.text1} texts; {price1} each>; " +\
                f"<{self.text2} texts; {price2} each>"

    def price_to_str(self, price):
        """Converts price to string."""
        price = str(price)
        price = "₴" + price[:-2] + "." + price[-2:]
        return price

    def is_empty(self):
        """Checks if machine is not empty."""
        if self.text1 != 0 and self.text2 != 0:
            return False
        return True

    def texts_count(self):
        """Counts texts."""
        return (self.text1, self.text2)

    def still_owe(self):
        """Counts owing amount."""
        return (self.price1, self.price2)

    def insert_money(self, m_text):
        """Inserts money for some type of text.
        Checks if owing amount is 0 or not."""
        if m_text[1] == 'short':
            temp = max(self.text1,self.text2)
        elif m_text[1] == 'long':
            temp = min(self.text1,self.text2)

    @classmethod
    def railway_station_machine(cls):
        """Puts machine in different place."""
        pass

    def stock_machine(self, filling):
        """Fills the machine."""
        if self.text1 == 0:
            self.text1 = filling[0]
            self.price1 = filling[1]
        if self.text2 == 0:
            self.text2 = filling[0]
            self.price2 = filling[1]
