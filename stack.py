class stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def is_empty(self):
        if self.item ==[]:
            return True
        else:
            return False
if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)

    while not s.is_empty():
        item = s.pop()
        print(item)