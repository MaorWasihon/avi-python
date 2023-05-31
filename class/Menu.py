import csv
import unittest
from Product import *


class MenuData:
    def __init__(self, filename):
        self.filename = filename
        print(self.filename)

    def save(self, products):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product', 'price'])
            for prod in products:
                writer.writerow([prod['product'], prod['price']])

    def load(self):
        menus = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menus.append(row)
        return menus


class Menu:
    def __init__(self, products):
        self.products = products

    def view_menu(self):
        """
        print the menu
        :return:
        """
        rtn = []
        for product in self.products:
            print(product)
            rtn.append(product)
        return rtn


    def add_product(self, product):
        self.products.append({'product': f'{product.name}', 'price': f'{product.price}'})
        print(f"{product.name} has been added to the menu.")

    def edit_product(self, name, price):
        for i, product in enumerate(self.products):
            print(i, product)
            if product['product'] == name:
                self.products[i]['price'] = price
                print(f"{product['product']} has been updated with a new price of ${product['price']}")
                return
        print(f"Error: {name} not found in the menu.")

    def delete_product(self, product_name):
        for i, product in enumerate(self.products):
            if product['product'] == product_name:
                del self.products[i]
                print(f"{product_name} has been deleted from the menu.")
                return
        print(f"Error: {product_name} not found in the menu.")

