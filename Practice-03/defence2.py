class Product:
    total_products = 0  

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def get_info(self):
        return f"Product name: {self.name}, Price: {self.price} kzt"

    def get_total_products(self):   
        return f"Total products: {Product.total_products}"


class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_info(self):   
        base_info = super().get_info()
        return f"{base_info}, File size: {self.file_size} MB"
class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def get_info(self):   
        base_info = super().get_info()
        return f"{base_info}, Weight: {self.weight} kg"
p0 = Product("Nonon" , 100)
product1 = DigitalProduct("Something😂😂", 15, 50)
p2 = PhysicalProduct("Laptop", 1000, 2.5)

print(product1.get_info())
print(p2.get_info())
print(product1.get_total_products())  