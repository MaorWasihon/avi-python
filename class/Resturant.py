import unittest

class Restaurant:
    
    def __init__(self, name, address, phone, tables=None, reservations=None, products=None, persons=None, payments=None, orders=None, menu=None, inventory_management=None, ingredient_data=None, income_report=None, employees=None, duties=None, customers=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.tables = tables or []
        self.reservations = reservations or []
        self.products = products or []
        self.persons = persons or []
        self.payments = payments or []
        self.orders = orders or []
        self.menu = menu or []
        self.inventory_management = inventory_management or []
        self.ingredient_data = ingredient_data or []
        self.income_report = income_report or []
        self.employees = employees or []
        self.duties = duties or []
        self.customers = customers or []

    def printName(self):
        print(self.name)

class TestRestaurant(unittest.TestCase):
    def test_restaurant(self):
        restaurant = Restaurant("Tokyo", "dizingof 59 tel aviv", "03-972657")
        self.assertEqual(restaurant.name, "Tokyo")
        self.assertEqual(restaurant.address, "dizingof 59 tel aviv")
        self.assertEqual(restaurant.phone, "03-972657")
        self.assertEqual(restaurant.tables, [])
        self.assertEqual(restaurant.reservations, [])
        self.assertEqual(restaurant.products, [])
        self.assertEqual(restaurant.persons, [])
        self.assertEqual(restaurant.payments, [])
        self.assertEqual(restaurant.orders, [])
        self.assertEqual(restaurant.menu, [])
        self.assertEqual(restaurant.inventory_management, [])
        self.assertEqual(restaurant.ingredient_data, [])
        self.assertEqual(restaurant.income_report, [])
        self.assertEqual(restaurant.employees, [])
        self.assertEqual(restaurant.duties, [])
        self.assertEqual(restaurant.customers, [])


# from datetime import datetime
# import unittest

# class Restaurant:
#     def __init__(self, name, address, phone, Table,Reservation,Product,Person,Payment,Order,Menu,InventoryManagement,IngredientData,IncomeReport, Employee,Duty,Customer):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.Table = Table
#         self.Reservation = Reservation
#         self.Product = Product
#         self.Person = Person
#         self.Payment = Payment
#         self.Order = Order
#         self.Menu = Menu
#         self.InventoryManagement = InventoryManagement
#         self.IngredientData = IngredientData
#         self.IncomeReport = IncomeReport
#         self.Employee = Employee
#         self.Duty = Duty
#         self.Customer = Customer


# def test_restaurant(self):
#         restaurant = Restaurant("Tokyo", "dizingof 59 tel aviv", "03-972657", [])
#         assert restaurant.name == "Tokyo"
#         assert restaurant.address == "dizingof 59 tel aviv"
#         assert restaurant.phone == "03-972657"


# class TestRestaurant(unittest.TestCase):
#     def test_restaurant(self):
#         restaurant = Restaurant("Tokyo", "dizingof 59 tel aviv", "03-972657", [])
#         self.assertEqual(restaurant.name, "Tokyo")
#         self.assertEqual(restaurant.address, "dizingof 59 tel aviv")
#         self.assertEqual(restaurant.phone, "03-972657")


