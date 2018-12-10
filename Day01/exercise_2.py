if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    current_frequency = 0

    resulting_frequencies = []
    repeated_frequency_not_found = True
    while repeated_frequency_not_found:
        with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
            frequency_changes = input_file.read().splitlines()
            for frequency_change in frequency_changes:
                int_frequency_change = int(frequency_change)
                current_frequency += int(frequency_change)
                if current_frequency in resulting_frequencies:
                    # found!
                    repeated_frequency_not_found = False
                    print("The input frequency changes list first reaches {0} twice.".format(current_frequency))
                    break
                else:
                    resulting_frequencies.append(current_frequency)
