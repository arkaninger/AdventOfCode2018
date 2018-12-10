if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    current_frequency = 0

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        frequency_changes = input_file.read().splitlines()
        for frequency_change in frequency_changes:
            int_frequency_change = int(frequency_change)
            # print("Current frequency {0}".format(current_frequency))
            # print("Change of {0}".format(frequency_change))
            current_frequency += int(frequency_change)
            # print("Resulting frequency {0}".format(current_frequency))
            # print("")
        print("Final resulting frequency is {0}".format(current_frequency))
