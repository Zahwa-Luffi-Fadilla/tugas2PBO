class Product:

    def __init__(self, id, name, price, stock):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getter
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Setter
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price > 0:
            self.__price = price

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock

    # Behavior
    def tambah_stok(self, jumlah):
        self.__stock += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stock:
            self.__stock -= jumlah

    def hitung_diskon(self, persen):
        return self.__price - (self.__price * persen / 100)