if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    appears_twice = 0
    appears_three = 0

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        box_ids = input_file.read().splitlines()
        for box_id in box_ids:
            letter_occurences_dict = {letter:box_id.count(letter) for letter in box_id}
            #print(letter_occurences_dict)
            appears_twice_here = [key for key, val in letter_occurences_dict.items() if val == 2]
            appears_three_here = [key for key, val in letter_occurences_dict.items() if val == 3]
            if appears_twice_here.__len__() > 0:
                #print("There are {0} letters that appear two times here ({1}).".format(appears_twice_here.__len__(), appears_twice_here))
                appears_twice += 1
            if appears_three_here.__len__() > 0:
                #print("There are {0} letters that appear three times here ({1}).".format(appears_three_here.__len__(), appears_three_here))
                appears_three += 1
            #print()
        print("There are {0} IDs that contain two times the same letter, and {1} that contain three times the same letteer.".format(appears_twice, appears_three))
        print("Therefore, the checksum is {0}*{1} = {2}".format(appears_twice, appears_three, appears_twice*appears_three))
