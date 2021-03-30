# Addresses are stored in our map as objects.
class Address:
    def __init__(self, address_id, street, city, state, zipcode):
        self.address_id = address_id
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def set_address_id(self, address_id):
        self.address_id = address_id

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def get_address_id(self):
        return self.address_id

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

# Our "map" of Salt Lake City is implemented as a bidirectional weighted graph.
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

    def get_distance(self, start_address, end_address):
        return self.address_distances[(start_address, end_address)]
