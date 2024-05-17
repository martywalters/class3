class Restaurant:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Restaurant, cls).__new__(cls)
            cls.instance._orders = 0
            cls.instance._total_sales = 0.0
            #return cls._instance
        else:
            #print('exist')
            pass
        return cls.instance
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
        print("init food")
        pass
    def price(self):
        return 0
    def prepare(self):
        pass
    @staticmethod
    def order_food(food_type): # Notice no 'self'
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
            
class Cheeseburger(Food):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.price():.2f}"

    def price(self):
        return 5.99
    def prepare(self):
        print( f"{__class__.__name__}: grill all-beef patty")

class Pasta(Food):
    def __str__(self):
        return f"{self.__class__.__name__}: {self.price():.2f}"
    def price(self):
        return 8.99
    def prepare(self):
        print("Pasta: boil water for noodles")
    

def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)
    food = r.order_food("pasta")
    if food:
        print(food)
    food = r.order_food("mac and cheese") # doesn't exist, prints failure message
    if food:
         print(food)

if __name__ == "__main__":
    main()

# Use this test to prove we have a single instance of Restaurant:
r2 = Restaurant()
print(r2)
##restaurant = Restaurant()
##print(restaurant)
##restaurant2 = Restaurant()
##print(restaurant2)

    
    
        
