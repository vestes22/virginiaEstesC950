class Truck:
    def __init__(self):
        self.packages = [None] * 16
        self.miles_driven = 0

    def add_miles(self, miles):
        self.miles_driven += miles

    def load_truck(self, package):
        self.packages.append(package)
