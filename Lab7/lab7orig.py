class Restaurant:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._orders = 0
            cls._instance._total_sales = 0.0
        return cls._instance

    def __str__(self):
        return f"This restaurant had {self._orders} orders today for a total of ${self._total_sales:.2f} in sales."

    def order_food(self, food_type):
        self._orders += 1
        food = Food.order_food(food_type)
        if food:
            self._total_sales += food.price()
        return food

    

class Food:
    def __init__(self):
        print("Creating food...")  # Placeholder message for debugging

    def price(self):
        return 0  # Placeholder

    def prepare(self):
        pass  # Placeholder

    @staticmethod
    def order_food(food_type):
        food_type = food_type.strip().lower()
        if food_type == "cheeseburger":
            food = Cheeseburger()
        elif food_type == "pasta":
            food = Pasta()
        else:
            print(f"Sorry, the restaurant does not make '{food_type}'")
            return None
        food.prepare()
        return food


from time import sleep

from time import sleep

class Cheeseburger(Food):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.price():.2f}"

    def price(self):
        return 5.99

    def prepare(self):
        print("Cheeseburger: grill all-beef patty")
        sleep(1)
        print("Cheeseburger: flip patty")
        sleep(1)
        print("Cheeseburger: put cheese on patty")
        sleep(1)
        print("Cheeseburger: put patty on bun and add toppings")
        sleep(1)
        print("Cheeseburger: All done!")


class Pasta(Food):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.price():.2f}"

    def price(self):
        return 8.99

    def prepare(self):
        print("Pasta: boil water for noodles")
        sleep(2)
        print("Pasta: saute onions, garlic and tomatoes for sauce")
        sleep(2)
        print("Pasta: put noodles in water")
        sleep(2)
        print("Pasta: season the sauce")
        sleep(2)
        print("Pasta: plate noodles and add sauce on top")
        sleep(2)
        print("Pasta: All done!")


# Extra credit: Add a third food derivative
class Salad(Food):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.price():.2f}"

    def price(self):
        return 7.99

    def prepare(self):
        print("Salad: toss lettuce, tomatoes, and cucumbers")
        sleep(1)
        print("Salad: add dressing")
        sleep(1)
        print("Salad: sprinkle cheese on top")
        sleep(1)
        print("Salad: All done!")

def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)

    food = r.order_food("pasta")
    if food:
        print(food)

    food = r.order_food("mac and cheese")  # doesn't exist, prints failure message
    if food:
        print(food)

    print(r)  # If you did extra credit, it will show number of orders and total sales

    # Use this test to prove we have a single instance of Restaurant:
    r2 = Restaurant()
    print(r2)

if __name__ == "__main__":
    main()


