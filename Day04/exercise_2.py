import re


def update_dict(guards_sleeping_dict, guards_minutes_sleeping_dict, guard_id, actions_block):
    for action in actions_block:
        if "falls" in action:
            match_minute_obj = re.search(r':(\d\d)', action)
            if match_minute_obj:
                starting_minute = int(match_minute_obj.group(1))
        if "wakes" in action:
            match_minute_obj = re.search(r':(\d\d)', action)
            if match_minute_obj:
                ending_minute = int(match_minute_obj.group(1))
            for minute in range(starting_minute, ending_minute):
                guard_id_minute = (guard_id, minute)
                if not guards_minutes_sleeping_dict.get(guard_id_minute):
                    guards_minutes_sleeping_dict[guard_id_minute] = 1
                else:
                    guards_minutes_sleeping_dict[guard_id_minute] = guards_minutes_sleeping_dict.get(guard_id_minute) + 1
            minutes_sleeping = ending_minute - starting_minute
            if not guards_sleeping_dict.get(guard_id):
                guards_sleeping_dict[guard_id] = minutes_sleeping
            else:
                guards_sleeping_dict[guard_id] = guards_sleeping_dict.get(guard_id) + minutes_sleeping
    return None


if __name__ == '__main__':
    # input path
    INPUT_FILEPATH = "input.txt"

    # exercise constraints
    # IMPORTANT NOTE: I've checked that every single time a guard falls asleep, he wakes up before ending his shift
    # current_frequency = 0

    # sample input
    # [1518 - 03 - 23 23: 59] Guard  # 1301 begins shift

    # [1518 - 03 - 24 23: 58] Guard  # 1279 begins shift
    # [1518 - 03 - 25 00: 33] falls asleep
    # [1518 - 03 - 25 00: 53] wakes up

    # [1518 - 03 - 25 23: 50] Guard  # 1877 begins shift
    # [1518 - 03 - 26 00: 00] falls asleep
    # [1518 - 03 - 26 00: 22] wakes up
    # [1518 - 03 - 26 00: 57] falls asleep
    # [1518 - 03 - 26 00: 58] wakesup

    with open(INPUT_FILEPATH, encoding='utf-8') as input_file:
        lines = sorted(input_file.read().splitlines())
        guards_minutes_sleeping_dict = {}
        guards_sleeping_dict = {}
        # the dict will have the following structure:
        # key: (guardId, minute)
        # value: times that guard was asleep that minute

        guard_id = 0
        actions_block = []
        for line in lines:
            if "Guard" in line:
                if actions_block.__len__() > 0:
                    update_dict(guards_sleeping_dict, guards_minutes_sleeping_dict, guard_id, actions_block)
                match_id_obj = re.search(r'#(\d+) ', line)
                if match_id_obj:
                    guard_id = int(match_id_obj.group(1))
                actions_block = []
            elif "falls" or "wakes" in line:
                line = line.replace("]", "] Guard #{0}".format(guard_id))
                actions_block.append(line)

    desired_guard_frequent_minute = max(guards_minutes_sleeping_dict.keys(), key=(lambda k: guards_minutes_sleeping_dict[k]))
    print("The guard who is most frequently asleep on the same minute is guard {0} at minute {1}".format(desired_guard_frequent_minute[0], desired_guard_frequent_minute[1]))
    print("Then, the result is {0}*{1}={2}".format(desired_guard_frequent_minute[0], desired_guard_frequent_minute[1], desired_guard_frequent_minute[0] * desired_guard_frequent_minute[1]))
