class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, special_notes, status):
        self.package_id = package_id
        self.address_id = None
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status

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

    def set_status(self, status):
        self.status = status

    def get_package_id(self):
        return self.package_id

    def get_address_id(self):
        return self.address_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self, state):
        return self.state

    def get_zip(self):
        return self.zipcode

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_special_notes(self, special_notes):
        return self.special_notes

    def get_status(self):
        return self.status
