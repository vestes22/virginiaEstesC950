class Address:
    def __init__(self, address_ID, street, city, state, zipcode):
        self.address_ID = address_ID
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def set_address_ID(self, address_ID):
        self.address_ID = address_ID

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def get_address_ID(self):
        return self.address_ID

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode


class MapGraph:
    def __init__(self):
        self.adjacent_address_list = {}
        self.address_distances = {}

    def add_address(self, address):
        self.adjacent_address_list[address] = []

    def add_unidirectional_distance(self, start_address, end_address, weight):
        self.address_distances[(start_address, end_address)] = weight
        self.adjacent_address_list[start_address].append(end_address)

    def add_bidirectional_distance(self, start_address, end_address, weight):
        self.add_unidirectional_distance(start_address, end_address, weight)
        self.add_unidirectional_distance(end_address, start_address, weight)

