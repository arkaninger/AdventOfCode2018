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
        self.overlaps = False

    def __str__(self):
        return self.line + "; "+str(self.overlaps)


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        lines = input_file.read().splitlines()
        fabric = {}

        claims_dict = {}
        for line in lines:
            # Create claim instance
            claim = Claim(line)
            # Add instance to claims_dict dictionary, with claim.id as key and the instance itself as value
            claims_dict[claim.id] = claim

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
                        fabric[coordinates] = [claim.id]
                    else:
                        fabric.get(coordinates).append(claim.id)
                        for claim_id in fabric.get(coordinates):
                            claims_dict[claim_id].overlaps = True

        print("Claims which don't overlap: ")
        for claim_id in claims_dict.keys():
            if not claims_dict.get(claim_id).overlaps:
                print(claims_dict.get(claim_id))
