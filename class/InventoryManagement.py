from Product import Product
import csv

class InventoryManagementData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, inventoryManagements):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['products'])
            for inventoryManagement in inventoryManagements:
                writer.writerow([inventoryManagements.product])

    def load(self):
        inventoryManagements = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventoryManagements.append(InventoryManagement(row['product']))
        return inventoryManagements


class InventoryManagement:
  def _init_(self,products):
    self.products=products
    
  def is_available(self, product_id):
    for product in self.products:
      if product.id == product_id and product.quantity > 0:
        return True
    return False

  def decrement(self, product_id):
    for product in self.products:
      if product.id == product_id and product.quantity > 0:
        product.quantity -= 1
        return
    raise ValueError("Product not found or quantity is already 0")
  
class TestInventoryManagement:
    def test_is_available(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        assert inventory.is_available(1) == True
        assert inventory.is_available(2) == False
        assert inventory.is_available(3) == False

    def test_decrement(self):
        product1 = Product(1, 'Tomato', 10)
        product2 = Product(2, 'Milk', 0)
        inventory = InventoryManagement([product1, product2])

        inventory.decrement(1)
        assert product1.quantity == 9

        try:
            inventory.decrement(2)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"

        try:
            inventory.decrement(3)
        except ValueError as e:
            assert str(e) == "Product not found or quantity is already 0"
        else:
            assert False, "Expected ValueError but no exception was raised"

