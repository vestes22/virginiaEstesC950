class PackageHashTable:

    def __init__(self):
        self.table = []
        self.capacity = 40
        for i in range(self.capacity):
            self.table.append(None)

    # A hash function to use in conjunction with the hash table.
    def simple_hash(self, key):
        index = (key % 41) - 1
        return index

    # A function to insert new packages into the table.
    # O(1) time complexity.
    def insert_package(self, package):
        index = self.simple_hash(package.get_package_id())
        self.table[index] = package
        return True

    # A look-up function to return package data based on the package ID.
    # O(1) time complexity.
    def search(self, key):
        index = self.simple_hash(key)
        if self.table[index] is None:
            return False
        return self.table[index]

