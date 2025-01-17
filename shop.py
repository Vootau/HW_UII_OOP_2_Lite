from classes.products import *
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
shower_gel = HouseholdChemicals("Clear", 200, 'shower')

# Создаем пользователей
customer1 = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(admin)
cart2 = ShoppingCart(customer1)
cart2.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(shower_gel, 3)

# Выводим детали корзины
print(customer1.get_details())
print(cart.get_details(admin))
print(cart2.get_details(customer1))

print(ShoppingCart.get_carts_details())
