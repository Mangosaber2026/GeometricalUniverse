import re


def get_pattern():
    pattern = re.compile(r"[LR][0-9]\d*")
    return pattern

def get_matches(text: str):
    return get_pattern().findall(text)

def parse_matches(match_list: list[str]):

    match_listed = []

    for match in match_list:

        match_listed.append((match[0], int(match[1:])))

    return match_listed

def calculate(value: int, parsed_matches: list[tuple[str, int]]):

    position_left_0 = 0

    for item in parsed_matches:

        if item[0] == "R":

            for _ in range(item[1]):
                value += 1

                if value == 100:
                    value = 0
                    position_left_0 += 1

        else:

            for _ in range(item[1]):
                value -= 1

                if value == -1:
                    value = 99
                    position_left_0 += 1

        if value == 0:
            position_left_0 += 1

    return value, position_left_0

def orchestrator(value: int, text: str):
    print(f"Value: {value}")

    matches = get_matches(text)

    print(f"Number of commands: {len(matches)}")

    matches_dict = parse_matches(matches)

    result, position_left_0 = calculate(value, matches_dict)

    return result, position_left_0

def execute_file():

    with open("./first_problem_commands.txt", "r") as command_text:
        value = 50
        result, positions = orchestrator(value, command_text.read())
        print(f"Number: {result}, Position (true answer): {positions}")


def example(value: int, command_text: str):

    result, positions = orchestrator(value, command_text)

    print(f"""
Given value: {result}

Position: {positions}
""")

execute_file()