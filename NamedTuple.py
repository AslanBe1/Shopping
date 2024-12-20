from collections import namedtuple

class Product (namedtuple("Product", "name, price,quantity")):
    def total(self):
        return self.price * self.quantity


class User(namedtuple("User", "name, age,address")):
    def is_adults(self):
        if self.age >= 18:
            return f'Adult {self.age}'
        else:
            raise ValueError('You are not adults')

product=Product('Laptop',15000,3)
user=User('John',18,'john@gmail.com')

print(f'Name: {product.name} \nProduct Price: {product.price} \nQuantity: {product.quantity}\nTotal Price: {product.total()}\n')
print(f'User: {user.name} \nAge: {user.is_adults()} \nAddress: {user.address}')