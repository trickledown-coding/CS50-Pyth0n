import emoji

class Jar:
    def __init__(self, size, capacity=12):
        self.capacity = capacity
        self.size = size
        ...

    def __str__(self):
        return f"{emoji.emojize(':cookie:')}"*self.size
        ...

    def deposit(self, n):
        if self.capacity < 12 and self.capacity + n <= 12:
            self.size += n
            return self.size
        else:
            raise ValueError

    def withdraw(self, n):
        if self.capacity > 0 and self.capacity - n >= 0:
            self.size -= n
            return self.size
        elif self.capacity - n <= 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value > 12:
            raise ValueError("No more than 12 cookies fit in the cookie jar")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if  0 > value > 12:
            raise ValueError("No more than 12 cookies can be in the cookie jar")
        self._size = value
