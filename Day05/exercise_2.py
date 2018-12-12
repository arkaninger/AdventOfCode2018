def is_reactive(first, second):
    if first.lower() == second.lower()\
            and (first.islower() and second.isupper()
                 or first.isupper() and second.islower()):
        return True
    return False


def check_and_remove_reactive(input_polymer):
    for index in range(0, input_polymer.__len__()-1):
        if is_reactive(input_polymer[index], input_polymer[index+1]):
            return input_polymer[:index] + input_polymer[index+2:]
    return input_polymer


def obtain_all_units_from_polymer(input_polymer):
    input_polymer = input_polymer.lower()
    all_unit_types = []
    for index, unit in enumerate(input_polymer):
        if unit not in all_unit_types:
            all_unit_types.append(unit)
    return all_unit_types


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        polymer = input_file.read()
        # polymer = "dabAcCaCBAcCcaDA"
        all_lowercase_units = obtain_all_units_from_polymer(polymer.strip())

        length_by_unit_dict = {}
        for unit in all_lowercase_units:
            short_polymer = polymer.replace(unit, "").replace(unit.upper(), "")
            while True:
                result = check_and_remove_reactive(short_polymer.strip())
                if result.__len__() < short_polymer.__len__():
                    short_polymer = result
                else:
                    print("Final polymer by removing all {0} is {1} units long".format(unit, result.__len__()))
                    length_by_unit_dict[unit] = result.__len__()
                    break

        min_polymer = min(length_by_unit_dict.keys(), key=(lambda k: length_by_unit_dict[k]))
        print("By removing all {0} units, final polymer is {1} units long.".format(min_polymer, length_by_unit_dict[min_polymer]))
