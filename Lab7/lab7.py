from time import sleep
class Restaurant:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Restaurant, cls).__new__(cls)
            cls.instance._orders = 0
            cls.instance._total_sales = 0.0
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
        #print("init food")
        pass
    def price(self):
        return 0
    def __str__(self):
        return f"{type(self).__name__}: {self.price():.2f}"
    def prepare(self):
        pass
    @staticmethod
    def order_food(food_type): # Notice no 'self'

        food_type = food_type.strip().lower()
        if food_type == "cheeseburger":
            food = Cheeseburger()
        elif food_type == "pasta":
            food = Pasta()
        elif food_type == "hotdog":
            food = HotDog()
        else:
            print(f"Sorry, the restaurant does not make '{food_type}'")
            return None
        food.prepare()
        return food
            
class Cheeseburger(Food):
    #def __str__():
    #    pass
    def price(self):
        return 5.99
    def prepare(self):
        print( f"{__class__.__name__}: grill all-beef patty")
        sleep(1)
        print("Cheeseburger: flip patty")
        sleep(2)
        print("Cheeseburger: put cheese on patty")
        sleep(2)
        print("Cheeseburger: put patty on bun and add toppings")
        sleep(1)
        print("Cheeseburger: All done!")

class Pasta(Food):
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
        sleep(1)
        print("Pasta: plate noodles and add sauce on top")
        sleep(1)
        print("Pasta: All done!")
class HotDog(Food):
    def price(self):
        return 3.99
    def prepare(self):
        print("HotDog: boil water for dog")
        sleep(2)
        print("HotDog: put dog in boiling water")
        sleep(2)
        print("HotDog: plate an open bun")
        sleep(1)
        print("HotDog: put dog in bun")
        sleep(1)
        print("HotDog: put ketchup and mustard on dog in bun")
def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)
    food = r.order_food("pasta")
    if food:
        print(food)
    food = r.order_food("hotdog")
    if food:
        print(food)
    food = r.order_food("mac and cheese") # doesn't exist, prints failure message
    if food:
         print(food)
    print(r)
    # Use this test to prove we have a single instance of Restaurant:
    r2 = Restaurant()
    print(r2)
if __name__ == "__main__":
    main()




    
    
        
