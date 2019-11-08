# Python Tutorial: Iterators and Iterables, by Corey Schafer
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

if __name__ == "__main__":
    nums = MyRange(1, 10)
    print(dir(nums))

    for num in nums:
        print(num)
