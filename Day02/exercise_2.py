def compare_two_box_ids(first_box_id, second_box_id):
    different_characters = 0
    last_different_character_position = 0
    for char_position in range(first_box_id.__len__()):
        if first_box_id[char_position] != second_box_id[char_position]:
            different_characters += 1
            last_different_character_position = char_position
            if different_characters > 1:
                return False
    if different_characters == 1:
        common_characters = first_box_id[:last_different_character_position] + first_box_id[last_different_character_position+1:]
        print("The two box ids that differ in one single character are {0} and {1},\n "
              "and the common characters are {2}.".format(first_box_id, second_box_id, common_characters))
        return True
    else:
        return False


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    correct_box_ids_found = False

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        box_ids = input_file.read().splitlines()
        sorted_box_ids = sorted(box_ids)
        for index, current_box_id in enumerate(sorted_box_ids):
            if current_box_id.__len__() > 0:
                for i in range(index, sorted_box_ids.__len__()):
                    correct_box_ids_found = compare_two_box_ids(current_box_id, sorted_box_ids[i])
                    if correct_box_ids_found:
                        break
                if correct_box_ids_found:
                    break
