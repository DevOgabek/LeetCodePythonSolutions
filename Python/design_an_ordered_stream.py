# Design an Ordered Stream

class OrderedStream(object):
    def __init__(self, n):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey, value):
        self.stream[idKey] = value
        result = []
        
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result

ordered_stream = OrderedStream(5)
print(ordered_stream.insert(3, "c"))
print(ordered_stream.insert(1, "a"))
print(ordered_stream.insert(2, "b"))
print(ordered_stream.insert(5, "e"))
print(ordered_stream.insert(4, "d"))