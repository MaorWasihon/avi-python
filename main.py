import sys

sys.path.append('./class/')

from Menu import *
from Product import *
from Resturant import Restaurant

def show_options():
        print("\nMenu Manager Options:")
        print("1. View Menu")
        print("2. Add Product to Menu")
        print("3. Edit Product from Menu")
        print("4. Delete Product from Menu")
        print("5. View Product List")
        print("6. Add New Product")
        print("7. Remove Product")
        print("8. Edit Product Details")
        print("9. Save Menu")
        print("10. Exit")



def main():
    """
    1. load menu data
    2. load product data
    3. print menu options
    :return:
    """

    # 1. load menu data
    menuData = MenuData('data/Menudata.csv')
    menu = Menu(menuData.load())

    # connect csv file to Product data
    products = ProductData('data/ProductData.csv')
    # print all products
    # products.print_products()
    # menu.view_menu()

    show_options()
    choice = input("Enter your choice: ")

    while True:
        print(menu.products)
        if choice == '1':
            menu.view_menu()
            show_options()
            choice = input("Enter your choice: ")

        elif choice == '2':
            name = input('Enter product name: ')
            price = input('Enter product price: ')
            is_veg = input('Enter product vegi [True\False]: ')
            prd = Product(name = name, price = price, is_vegetarian = bool(is_veg))
            print(prd)
            menu.add_product(prd)
            choice = input("Enter your choice: ")

        elif choice == '3':
            name = input('Enter product name: ')
            price = input('Enter product new price: ')
            menu.edit_product(name, price)
            choice = input("Enter your choice: ")

        elif choice == '4':
            name = input('Enter product name: ')
            menu.delete_product(name)
            choice = input("Enter your choice: ")

        elif choice == '5':
            products.print_products()
            show_options()
            choice = input("Enter your choice: [1-10] ")

        elif choice == '9':
            menuData.save(menu.view_menu())
            show_options()
            choice = input("Enter your choice: [1-10] ")
        elif choice == '10':
            break
        else:
            show_options()
            choice = input("Enter your choice: [1-10] ")


if __name__ == "__main__":
    main()
