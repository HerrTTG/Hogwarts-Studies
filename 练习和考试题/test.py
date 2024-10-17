from typing import NamedTuple


class Product(NamedTuple):
    p_name: str
    price: float
    number: int | float

    def total(self) -> float:
        return self.price * self.number

    def __str__(self):
        return f'<Product>({self.p_name, self.price, self.number})'


class Cart(NamedTuple):
    customer: str
    products: list[Product]

    @property
    def total(self):
        total = 0.00
        for p in self.products:
            total += p.total()
        return total

    def __str__(self):
        str1 = f'<Cart>{self.customer}\n'
        for p in self.products:
            str1 += str(p) + '\n'
        str2 = f'Total:{self.total}'
        return str1 + str2


print(Cart('张三', [Product('苹果', 0.5, 2), Product('香蕉', 1, 10)]))
