from datetime import timedelta, datetime


class Truck:
    def __init__(self):
        self.packages = []
        self.miles_driven = 0
        self.miles_per_hour = 18
        self.current_address = None
        # timer is the truck's "clock".
        self.timer = datetime(2021, 12, 31, 7, 59, 00)

    def set_current_address(self, address_id):
        self.current_address = address_id

    def set_timer(self, time):
        self.timer = time

    def add_miles(self, miles):
        self.miles_driven += miles

    def get_miles_driven(self):
        return self.miles_driven

    def load(self, package_id):
        if (len(self.packages) < 16):
            self.packages.append(package_id)
            return True
        else:
            return False

    def get_packages(self):
        return self.packages

    def get_package(self, index):
        return self.packages[index]

    def get_current_address(self):
        return self.current_address

    def get_miles_per_hour(self):
        return self.miles_per_hour

    def get_timer(self):
        return self.timer

    def remove_package(self, index):
        self.packages.pop(index)

    def add_seconds(self, added_seconds):
        self.timer = self.timer + timedelta(seconds=added_seconds)
        return self.timer
