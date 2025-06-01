class RandomizedSet:

    def __init__(self):
        self.data = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if self.hash.get(val) is not None:
            return False
        self.data.append(val)
        self.hash[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if self.hash.get(val) is None:
            return False
        
        index = self.hash[val]
        self.data[index],self.data[-1] = self.data[-1],self.data[index]
        self.hash[self.data[index]] = index
        self.data.pop()
        del self.hash[val] 
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()