class animal:

    def __init__(self, name: str, color: str, country: str,  age=10, height=35, length=35):
        self.name = name
        self.color = color
        self.country = country
        self.age = age
        self.height = height
        self.length = length

    def voice(self):
        print(self.sound)

    def calculate_sound(self) -> str:
        if self.height > 100:
            return "igo"
        if self.height <= 100:
            return "gaf"

print("animal class:1.dog, 2.cat, 3.horse")

class dog_keri(animal):
    def __init__(self, name: str, color: str, country: str,  age=10, height=35):
        super().__init__(name, color, country, age, height)
dog_keri = dog_keri("keri", "brown", "Japan", age=5, height=35)
print("character dog:")
print("name:", dog_keri.name, "color:", dog_keri.color, "counry:", dog_keri.country, "age:", dog_keri.age, "height:", dog_keri.height, "sound:", dog_keri.calculate_sound())



class main_coon_cat(animal):
    def __init__(self, name: str, color: str, country: str, length=120):
        super().__init__(name, color, country, length=120)
main_coon_cat = main_coon_cat("coon", "grey", "America", length=120)
print("character cat:")
print("name:", main_coon_cat.name, "color:", main_coon_cat.color, "country:", main_coon_cat.country, "length:", main_coon_cat.length)

class high_horse(animal):
    def __init__(self, name: str, color: str, country: str, age=12 , height=170):
        super().__init__(name, color, country, age, height)
high_horse = high_horse("ben", "white", "Mexico", age=12, height=170)
print("character horse:")
print("name:", high_horse.name, "color:", high_horse.color, "country:", high_horse.country, "age:", high_horse.age, "height:", high_horse.height, "sound:", high_horse.calculate_sound())


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} сек.")
        return result
    return wrapper

@timer
def some_function():
    time.sleep(2)
print(some_function)