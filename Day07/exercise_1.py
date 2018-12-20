import re


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"
    INPUT_TEST_FILEPATH = "input_test.txt"  # answer = CABDFE

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        steps_input = input_file.read().splitlines()
    steps_set = set()
    requirements_dict = {}
    for step in steps_input:
        requirement_and_goal = re.findall(r" ([A-Z]) ", step)

        # For completeness sake, on steps_set we should add both:
        # requirements and goals
        steps_set.update(requirement_and_goal)

        requirement_name = requirement_and_goal[0]
        goal_name = requirement_and_goal[1]
        if not requirements_dict.get(goal_name):
            requirements_dict[goal_name] = {requirement_name}
        else:
            requirements_dict[goal_name].update([requirement_name])

    ordered_steps = []
    while steps_set.__len__() > 0:
        print("We start a new round:")
        print("steps_set: {0}".format(steps_set))
        next_available_steps = []
        for element in steps_set:
            if element not in requirements_dict or requirements_dict[element].__len__() == 0:
                next_available_steps.append(element)
        print("next_available_steps: {0}".format(", ".join(next_available_steps)))
        print("We choose as next step: {0}".format(sorted(next_available_steps)[0]))
        chosen_step = sorted(next_available_steps)[0]
        ordered_steps.append(chosen_step)
        print("So ordered_steps remains: {0}".format(", ".join(ordered_steps)))
        steps_set.remove(chosen_step)
        for element in requirements_dict.keys():
            if chosen_step in requirements_dict.get(element):
                requirements_dict.get(element).remove(chosen_step)
        print("")

    print("The order in which the steps should be completed is {0}".format("".join(ordered_steps)))
