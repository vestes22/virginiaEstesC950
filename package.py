from datetime import timedelta, datetime


class Package:
    def __init__(self, package_id, address_id, address, city, state, zipcode, deadline, weight, special_notes):
        self.package_id = package_id
        self.address_id = address_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = []

    def set_package_id(self, package_id):
        self.package_id = package_id

    def set_address_id(self, address_id):
        self.address_id = address_id

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip(self, zipcode):
        self.zipcode = zipcode

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_weight(self, weight):
        self.weight = weight

    def set_special_notes(self, special_notes):
        self.special_notes = special_notes

    # Each time the package status is updated, it is appended to the status array.
    # Each new update consists of an array of 2 indexes. Index 0 is the timestamp of the update,
    # and index 1 is the status.
    def update_status(self, time, status):
        new_status = [time, status]
        self.status.append(new_status)

    def get_package_id(self):
        return self.package_id

    def get_address_id(self):
        return self.address_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zipcode

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_special_notes(self):
        return self.special_notes

    def get_status(self, key):
        index = 0
        for package in self.status:
            if self.status[index][0] == key:
                return self.status[index]
            index += 1

    def get_all_statuses(self):
        return self.status
