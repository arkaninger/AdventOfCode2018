# SOLUTION CREDITS TO nedbat
# https://github.com/nedbat/adventofcode2018/blob/master/day06.py

import itertools


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


def map_total_distances(points):
    whole_grid = {}   # key is point, value is sum of distances.
    for grid_point in grid_points(*bounds(points)):
        whole_grid[grid_point] = sum(distance(grid_point, point) for point in points)
    return whole_grid

if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"
    INPUT_TEST_FILEPATH = "input_test.txt"  # answer = 16

    # problem constraint
    TOTAL_DISTANCE_FOR_SAFE_REGION_TEST = 32
    TOTAL_DISTANCE_FOR_SAFE_REGION = 10000
    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        lista = [eval(line) for line in input_file if line.strip()]
        grid = map_total_distances(lista)
        result = sum(1 for dist in grid.values() if dist < TOTAL_DISTANCE_FOR_SAFE_REGION)
        print("The size of the region containing all locations which have a total distance to all given"
              " coordinates of less than {0} is {1}.".format(TOTAL_DISTANCE_FOR_SAFE_REGION, result))

