class PackageHashTable:

    def __init__(self):
        self.table = []
        self.capacity = 40
        for i in range(self.capacity):
            self.table.append(None)

    def simple_hash(self, key):
        index = key - 1
        return index

    def insert_package(self, package):
        index = self.simple_hash(package.get_package_id())
        self.table[index] = package
        return True

    def search(self, key):
        index = self.simple_hash(key)
        if self.table[index] is None:
            return False
        return self.table[index]

