class Engine:
    def __init__(self, name, engine_type):
        self.name = name
        self.engine_type = engine_type

class Car:
    def __init__(self, engine, driver):
        self.engine = engine
        self.driver = driver

    def display(self):
        print("Car Info:")
        print(f"  Engine: {self.engine.name} ({self.engine.engine_type})")
        print(f"  Driver: {self.driver}")