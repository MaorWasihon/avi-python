import unittest
import io
from contextlib import redirect_stdout
import csv

class IncomeReportData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, income_reports):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['restaurant_name', 'year', 'month', 'total_income', 'expenses'])
            for report in income_reports:
                writer.writerow([report.restaurant_name, report.year, report.month, report.total_income, report.expenses])

    def load(self):
        income_reports = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                restaurant_name = row['restaurant_name']
                year = int(row['year'])
                month = int(row['month'])
                total_income = float(row['total_income'])
                expenses = ast.literal_eval(row['expenses'])
                income_report = IncomeReport(restaurant_name, year, month, total_income, expenses)
                income_reports.append(income_report)
        return income_reports


class IncomeReport:
    def __init__(self, restaurant_name, year, month, total_income, expenses):
        self.restaurant_name = restaurant_name
        self.year = year
        self.month = month
        self.total_income = total_income
        self.expenses = expenses
        
    def generate_report(self):
        net_income = self.total_income - sum(self.expenses.values())
        
        print(f"Income Report for {self.restaurant_name} - {self.month}/{self.year}")
        print("=" * 50)
        print(f"Total Income: ${self.total_income}")
        print(f"Total Expenses: ${sum(self.expenses.values())}")
        print(f"Net Income: ${net_income}")
        print()
        
        print("Expenses Breakdown:")
        print("-" * 50)
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
        print()


import unittest

class TestIncomeReport(unittest.TestCase):

    def test_generate_report(self):
        expenses = {'Rent': 1000, 'Salaries': 5000, 'Supplies': 500}
        income_report = IncomeReport('My Restaurant', 2022, 'May', 10000, expenses)
        expected_output = "Income Report for My Restaurant - May/2022\n==================================================\nTotal Income: $10000\nTotal Expenses: $6500\nNet Income: $3500\n\nExpenses Breakdown:\n--------------------------------------------------\nRent: $1000\nSalaries: $5000\nSupplies: $500\n\n"
        with io.StringIO() as buffer, redirect_stdout(buffer):
            income_report.generate_report()
            output = buffer.getvalue()
            self.assertEqual(output, expected_output)

