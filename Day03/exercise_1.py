import re


class Claim:
    # A claim like #123 @ 3,2: 5x4 means that
    # claim ID 123 specifies a rectangle
    # 3 inches from the left edge,
    # 2 inches from the top edge,
    # 5 inches wide, and
    # 4 inches tall.
    def __init__(self, claim):
        self.line = claim
        match_id_obj = re.search(r'#(\d+) @', claim)
        if match_id_obj:
            self.id = int(match_id_obj.group(1))
        match_margin_obj = re.search(r'(\d+),(\d+)', claim)
        if match_margin_obj:
            self.margin_left = int(match_margin_obj.group(1))
            self.margin_top = int(match_margin_obj.group(2))
        match_size_obj = re.search(r'(\d+)x(\d+)', claim)
        if match_size_obj:
            self.width = int(match_size_obj.group(1))
            self.height = int(match_size_obj.group(2))


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # result
    claimed_more_than_once = 0

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        lines = input_file.read().splitlines()
        fabric = {}
        for line in lines:
            claim = Claim(line)

            # print(claim.line)
            # print(claim.id)
            # print(claim.margin_left)
            # print(claim.margin_top)
            # print(claim.width)
            # print(claim.height)

            for x in range(claim.margin_left, claim.margin_left+claim.width):
                for y in range(claim.margin_top, claim.margin_top+claim.height):
                    coordinates = (x, y)
                    if not fabric.get(coordinates):
                        fabric[coordinates] = 1
                    else:
                        if fabric.get(coordinates) == 1:
                            claimed_more_than_once += 1
                        fabric[coordinates] = fabric.get(coordinates) + 1
        print("Square inches already claimed by others: ", claimed_more_than_once)
