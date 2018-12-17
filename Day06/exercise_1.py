# SOLUTION CREDITS TO nedbat
# https://github.com/nedbat/adventofcode2018/blob/master/day06.py

import itertools
import collections

class Coordinate:
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x) + "," + str(self.y)+")"


def distance(origin, other):
    return abs(origin[0] - other[0]) + abs(origin[1] - other[1])


def bounds(points):
    """Return minx,maxx,miny,maxy of the grid that encloses all points, plus one extra all around."""
    return (
        min(p[0] for p in points) - 1,
        max(p[0] for p in points) + 1,
        min(p[1] for p in points) - 1,
        max(p[1] for p in points) + 1,
    )

def grid_points(minx, maxx, miny, maxy):
    """Yield all points in the grid."""
    # TODO: still need to understand how this method works
    yx = itertools.product(range(miny, maxy+1), range(minx, maxx+1))
    return ((x,y) for y,x in yx)

def map_the_grid(points):
    # return a dict which represents a grid point (key) and the index of the closest coordinate (value);
    # no dict entry (thus, None) if two or more coordinates are at the same distance
    whole_grid = {}
    # iterate over the whole grid whose bounding box is based on the list of input coordinates
    for grid_point in grid_points(*bounds(points)):
        # assign an array with the distance of every single input coordinate to the specific grid point
        distances = [(distance(grid_point, point), index_point) for index_point, point in enumerate(points)]
        # sort the array so the closest coordinate gets index 0
        distances.sort()
        # if first and second distances are different (thus, no tie), assign the input coordinate to that grid point; else, assign nothing
        if distances[0][0] != distances[1][0]:
            whole_grid[grid_point] = distances[0][1]
    return whole_grid

def largest_finite_area(points, grid):
    # Find the infinite areas. Whatever points the grid edges are nearest,
    # are infinite.
    infinite_points = set()
    minx, maxx, miny, maxy = bounds(points)
    # iterate over the boundaries and add the coordinates (indexes) on them to the infinite_points set (because we don't want infinite areas)
    for x in range(minx, maxx+1):
        for y in [miny, maxy]:
            infinite_points.add(grid.get((x, y)))
    for y in range(miny, maxy+1):
        for x in [minx, maxx]:
            infinite_points.add(grid.get((x, y)))

    # Create a Counter object and iterate over the whole grid at first
    # it works as a dict: key is the coordinate's index, value is the number of occurrences
    # Total up the areas for each point.
    count = collections.Counter()
    count.update(grid.values())

    # then, remove from the counter the coordinates (indexes) that make infinite areas
    for infinite_point in infinite_points:
        del count[infinite_point]

    # print the most repeated coordinate's index and its number of occurrences, as an array of tuples
    # print(count.most_common(1))
    # print the most repeated coordinate's index and its number of occurrences, as a tuple
    # print(count.most_common(1)[0])
    # print only the number of occurrences of the most repeated coordinate
    # print(count.most_common(1)[0][1])
    return count.most_common(1)[0][1]

if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"
    INPUT_TEST_FILEPATH = "input_test.txt"  # answer = 17
    MIN_X = None
    MIN_Y = None
    MAX_X = None
    MAX_Y = None
    # GRID_WIDTH = 0
    # GRID_HEIGHT = 0
    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        lista = [eval(line) for line in input_file if line.strip()]
        grid = map_the_grid(lista)
        print("The size of the largest area that isn't infinite is {0}.".format(largest_finite_area(lista, grid)))

