class Battery:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.level = capacity

    def discharge(self, amount):
        self.level = max(0, self.level - amount)
        return self.level

    def charge(self, amount):
        self.level = min(self.capacity, self.level + amount)
        return self.level

    def status(self):
        return {"capacity": self.capacity, "level": self.level}
