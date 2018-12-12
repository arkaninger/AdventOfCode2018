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


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        polymer = input_file.read()
        while True:
            result = check_and_remove_reactive(polymer.strip())
            if result.__len__() < polymer.__len__():
                polymer = result
            else:
                print("Final polymer is {0} by {1} units".format(result, result.__len__()))
                break
