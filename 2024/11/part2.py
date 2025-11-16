class Stone:
    number: int | None
    sub_stones: list["Stone"] | None = None

    def __init__(self, number: int):
        self.number = number

    def replace_zero_stone(self):
        self.number = 1

    def split_stone(self):
        str_number = str(self.number)
        half_size = int(len(str_number) / 2)

        first_stone = Stone(int(str_number[:half_size]))
        second_stone = Stone(int(str_number[half_size:]))

        self.sub_stones = [first_stone, second_stone]
        self.number = None

    def multiply(self):
        self.number = self.number * 2024

    def apply_rules(self):
        if self.sub_stones:
            for stone in self.sub_stones:
                stone.apply_rules()
            return

        if self.number == 0:
            self.replace_zero_stone()
        elif len(str(self.number)) % 2 == 0:
            self.split_stone()
        else:
            self.multiply()

    def how_many_stones(self):
        if not self.sub_stones:
            return 1
        stones = 0

        for stone in self.sub_stones:
            stones += stone.how_many_stones()

        return stones

def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            file.append(line)

    return file

if __name__ == "__main__":
    file = read_file_input()
    line = file[0]

    stones = list()
    for number in line.split(" "):
        stones.append(Stone(int(number)))

    max_blinks = 75

    for i in range(max_blinks):
        print("blink: ", i)
        for stone in stones:
            stone.apply_rules()

    stone_count = 0
    for stone in stones:
        stone_count += stone.how_many_stones()
    print(stone_count)