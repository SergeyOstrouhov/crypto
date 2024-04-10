class BitArray:
    def __init__(self, size):
        self.size = size
        self.data = [0]* size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return self.size

    def get_bit(self, index):
        return self.data[index]

    def set_bit(self, index, value):
        self.data[index] = value

    def shift_left(self, n):
        self.data = self.data[n:] + self.data[:n]

    def shift_right(self, n):
        self.data = self.data[-n:] + self.data[:-n]

    def rotate_left(self, n):
        n %= self.size
        self.data = self.data[n:] + self.data[:n]

    def rotate_right(self, n):
        n %= self.size
        self.data = self.data[-n:] + self.data[:n]
