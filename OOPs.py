
# ============================
# 12. OBJECT-ORIENTED PROGRAMMING
# ============================

# ---- Person Class ----

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


p1 = Person("Aaditya", 24)
p2 = Person("Charan")

p1.greet()
p2.greet()


# ---- Book Class ----

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"{self.title} by {self.author}")

    def describe_with_awards(self, awards):
        print(f"{self.title} by {self.author} and got {awards}")


b1 = Book("1984", "George Orwell")
b1.describe()
b1.describe_with_awards("Pulitzer Prize")


# ---- Counter Class ----

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get_value(self):
        return self.count


counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
print("Counter value:", counter.get_value())


# ---- BankAccount Class ----

class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.holder_name}'s balance: {self.balance}")


account = BankAccount("Aaditya", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()


# ---- Car Class (Encapsulation) ----

class Car:
    def __init__(self):
        self._speed = 0

    def accelerate(self, amount):
        self._speed += amount

    def brake(self, amount):
        self._speed = max(0, self._speed - amount)

    def get_speed(self):
        return self._speed

    def __str__(self):
        return f"Car speed: {self._speed}"


car = Car()
car.accelerate(60)
car.brake(20)
print(car)