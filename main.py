#2-masala
class Car:
    def __init__(self, model, speed):
        self.model = model
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def accelerate(self, value):
        self.__speed += value
        print("Tezlik oshdi")

    def brake(self, value):
        if self.__speed >= value:
            self.__speed -= value
            print("Tezlik kamaydi")


c1 = Car("BMW", 120)

print(c1.model)
print(c1.get_speed())

c1.accelerate(30)
print(c1.get_speed())

c1.brake(50)
print(c1.get_speed())
