class ReverseIter:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.a = len(self.list)
        return self

    def __next__(self):
        if self.a > 0:
            x = self.list[self.a-1]
            self.a -= 1
            return x
        else:
            raise StopIteration
