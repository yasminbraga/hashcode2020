class DataReader:
    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self.data = file.readlines()

    def strip_and_split(self, row: str) -> list:
        return list(map(int, row.strip().split(' ')))

    def parse(self) -> list:
        return list(map(self.strip_and_split, self.data))


class Order:
    def __init__(self, data: DataReader):
        self.data = data

    @property
    def max_slices(self) -> int:
        return self.data[0][0]

    @property
    def types_length(self) -> int:
        return self.data[0][1]

    @property
    def types(self) -> list:
        return self.data[1]
