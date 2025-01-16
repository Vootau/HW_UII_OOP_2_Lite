# 3. Класс для управления корзиной покупок
class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    _all_carts = []

    def __init__(self, customer):
        self.items = []
        self.customer = customer
        ShoppingCart._all_carts.append(self)

    @classmethod
    def carts_info(cls):
        cart_info = [ShoppingCart._all_carts, len(ShoppingCart._all_carts)]
        return cart_info

    @classmethod
    def get_total_cost(cls):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = 0
        for _ in range(len(ShoppingCart.carts_info()[0])):
            for item in ShoppingCart.carts_info()[0][_].items:
                total += item["Продукт"].price * item["количество"]
        return total

    @classmethod
    def get_carts_details(cls):
        summary = f"Сводная информация о покупках:\n"
        for _ in range(len(ShoppingCart.carts_info()[0])):
            for item in ShoppingCart.carts_info()[0][_].items:
                summary += f"Покупатель: {item['Покупатель'].username}\n\t"
                summary += f"{item['Продукт'].get_details()}, "
                summary += f"Количество: {item['количество']}\n"
        summary += f"Общая стоимость покупок: {ShoppingCart.get_total_cost()}"
        return summary

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity, "Покупатель": self.customer})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_details(self, customer):
        """
        Возвращает информацию о корзине покупок конкретного покупателя
        """
        customer_cart_details = f"Корзина покупок {customer.username}\n"
        cart_cost = sum(
            item["Продукт"].price * item["количество"] for item in self.items if item['Покупатель'].username == customer.username
        )
        for item in self.items:
            if item['Покупатель'].username == customer.username:
                customer_cart_details += f"{item['Продукт'].get_details()},Количество: {item['количество']}\n"
        customer_cart_details += f"Общее: {cart_cost} руб"
        return customer_cart_details


