from Product import Product 
from Table import Table 
import csv

class OrderData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, orders):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id','table_id', 'products','total_amount','customer'])
            for order in orders:
                writer.writerow([order.id, order.table_id, order.products, order.total_amount, order.customer])

    def load(self):
        orders = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                orders.append(Order(int(row['order_id']), int(row['table_id']), row['products'], int(row['total_amount']), row['customer']))
        return orders


class Order:
  def __init__ (self,order_id,table_id, products,total_amount,customer):
    self.order_id = order_id
    self.table_id = table_id
    self.products = products
    self.total_amount = total_amount 
    self.customer=customer
 
  def place_order(self):
    self.customer.place_order(self.table_id, self.products)
    
  def add_product(self, product):
    self.products.append(product)

  def remove_product(self, product):
    if product in self.products:
      self.products.remove(product)

  def update_product_quantity(self, product, quantity):
    for p in self.products:
      if p == product:
        p.quantity = quantity

  def get_total_amount(self):
    total = 0
    for product in self.products:
      total += product.price * product.quantity
    return total

  def place_order(self, customer, table):
    print(f"Order placed by {customer.name} at table {table.table_id}")

import unittest
from unittest.mock import Mock



class TestOrder():

    def setUp(self):
        self.customer = Customer('Alin Pahima', '053-4648833')
        self.table = Table(1, 5, 'available')
        self.product1 = Product('Pasta', 65, False)
        self.product2 = Product('Sushi', 72, True)

    def test_add_product(self):
        order = Order(1, self.table.table_id, [], 0, self.customer)
        order.add_product(self.product1)
        self.assertEqual(order.products, [self.product1])

    def test_remove_product(self):
        order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer)
        order.remove_product(self.product1)
        self.assertEqual(order.products, [self.product2])

    def test_update_product_quantity(self):
        order = Order(1, self.table.table_id, [self.product1], 0, self.customer)
        order.update_product_quantity(self.product1, 2)
        self.assertEqual(order.products[0].quantity, 2)

    def test_get_total_amount(self):
        order = Order(1, self.table.table_id, [self.product1, self.product2], 0, self.customer)
        total = order.get_total_amount()
        self.assertEqual(total, self.product1.price + self.product2.price)

    def test_place_order(self):
        order = Order(1, self.table.table_id, [self.product1], 0, self.customer)
        self.customer.place_order = Mock()
        order.place_order()
        self.customer.place_order.assert_called_once_with(self.table.table_id, [self.product1])

