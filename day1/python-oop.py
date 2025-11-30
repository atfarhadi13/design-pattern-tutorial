class User:
    def __init__(self, email, full_name):
        self.email = email
        self.full_name = full_name

user = User("amin@example.com", "Amin Nasiri")

class Settings:
    APP_NAME = "Muzzomo"   # class attribute (shared by all)

    def __init__(self, user_id):
        self.user_id = user_id  # instance attribute

# self example in method
class Cart:
    def add_item(self, item):
        print(f"Adding {item} to the cart.")


# class method example
class User:
    user = []

    @classmethod
    def count(cls):
        return len(cls.user)
    
# static method example
class MathTools:

    @staticmethod
    def is_evern(number):
        return number % 2 == 0
    

# encapsulation private and public members
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    

# inheritance is-A relationship
class Vehicle:
    pass

class Car(Vehicle):
    pass


# composition has-A relationship
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()



# practical muzzomo example
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city


class Professional:
    def __init__(self, name, service_category, address: Address):
        self.name = name
        self.service_category = service_category
        self.address = address  # Composition


class Job:
    def __init__(self, title, customer, professional: Professional):
        self.title = title
        self.customer = customer
        self.professional = professional