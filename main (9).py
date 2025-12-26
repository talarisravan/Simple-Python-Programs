class Car:
    def __init__(self, name, price, color):
        self.name=name
        self.price=price
        self.color=color
    def accelerate(self):
        print("I am accelerating")
        print(self.color)
C1=Car("Swift",214674,"blue")
C2=Car("Toyato",6384764,"black")
C1.accelerate()
C2.accelerate()