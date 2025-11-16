def find_unique_tuples(nested_list, unique_tuples_set=None):
    """
    Recursively finds all unique tuples in a deeply nested list.
    """
    if unique_tuples_set is None:
        unique_tuples_set = set()

    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, recurse
            find_unique_tuples(item, unique_tuples_set)
        elif isinstance(item, tuple):
            # If the item is a tuple, add it to the set
            unique_tuples_set.add(item)

    return unique_tuples_set

class TopographicPoint:
    MAX_GRADUAL_STEP = 1

    height: int

    map_vector = tuple

    north: "TopographicPoint | None"
    south: "TopographicPoint | None"
    east: "TopographicPoint | None"
    west: "TopographicPoint | None"

    def __init__(self, height: int | None, x: int, y: int):
        self.height = height
        self.map_vector = (x, y)

        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self):
        return str(self.height)

    def set_north(self, north: "TopographicPoint | None"):
        self.north = north

    def set_south(self, south: "TopographicPoint | None"):
        self.south = south

    def set_east(self, east: "TopographicPoint | None"):
        self.east = east

    def set_west(self, west: "TopographicPoint | None"):
        self.west = west

    def is_hike_start(self) -> bool:
        return self.height == 0

    def is_hike_end(self) -> bool:
        return self.height == 9

    def trails_paths(self) -> list:
        if self.is_hike_end():
            return [self.map_vector]

        points = list()

        if self.north and self.height + self.MAX_GRADUAL_STEP == self.north.height:
            northern_paths = self.north.trails_paths()
            if northern_paths:
                points.append(northern_paths)

        if self.south and self.height + self.MAX_GRADUAL_STEP == self.south.height:
            southern_paths = self.south.trails_paths()
            if southern_paths:
                points.append(southern_paths)

        if self.east and self.height + self.MAX_GRADUAL_STEP == self.east.height:
            eastern_paths = self.east.trails_paths()
            if eastern_paths:
                points.append(eastern_paths)

        if self.west and self.height + self.MAX_GRADUAL_STEP == self.west.height:
            western_paths = self.west.trails_paths()
            if western_paths:
                points.append(western_paths)

        return points

    def count_of_hiking_trails_from_this_point(self) -> int:
        if not self.is_hike_start():
            return 0

        paths = self.trails_paths()
        unique_ends = find_unique_tuples(paths)
        hiking_trails = len(unique_ends)

        return hiking_trails


def read_file_input():
    file = list()
    with open("data.txt") as f:
        for line in f:
            tmp_line = list()
            for char in line:
                if char == "\n":
                    continue
                tmp_line.append(char)
            file.append(tmp_line)

    return file

def write_to_file(s: str):
    with open("tmp.txt", "a") as f:
        f.write(s)
        f.write('\n')


def create_topographic_map(file: list[list]) -> list[list[TopographicPoint]]:
    map = list()

    height = len(file)
    width = len(file[0])

    cur_height = 0
    while cur_height < height:
        map.append(list())
        cur_width = 0
        while cur_width < width:
            topographic_point = TopographicPoint(int(file[cur_height][cur_width]), cur_width, cur_height)

            if cur_height - 1 >= 0:
                north = map[cur_height-1][cur_width]
                topographic_point.set_north(north)
                north.set_south(topographic_point)

            if cur_width - 1 >= 0:
                west = map[cur_height][cur_width-1]
                topographic_point.set_west(west)
                west.set_east(topographic_point)
            map[cur_height].append(topographic_point)

            cur_width += 1
        cur_height += 1

    return map

if __name__ == "__main__":
    file = read_file_input()

    map = create_topographic_map(file)

    count = 0
    for row in map:
        for col in row:
            pass
            count += col.count_of_hiking_trails_from_this_point()

    print(count)
