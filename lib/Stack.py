class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for item in items:
            if(not self.full()):
                self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if (not self.full()):
            self.items.append(item)
        else:
            return None

    def pop(self):
        if self.isEmpty():
            return None

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass
