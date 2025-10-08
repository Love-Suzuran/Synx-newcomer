import random
class BatchDataLoader:
    def __init__(self, data, batch_size: int, shuffle: bool):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.it = 0
        self.len = len(self.data)
        if self.shuffle:
            random.shuffle(self.data) 
    def __iter__(self):
        self.it = 0
        if self.shuffle:
            random.shuffle(self.data)
        return self
    def __next__(self):
        if self.it >= self.len:
            raise StopIteration
        ending = min(self.it + self.batch_size, self.len)
        batch = self.data[self.it:ending]
        self.it = ending
        return batch
data = list(range(1, 21))
loader = BatchDataLoader(data, batch_size=6, shuffle=False)
for i, batch in enumerate(loader, 1):
    print(f"第{i}组数据: {batch}")