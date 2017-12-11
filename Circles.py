def circle(number_of_friends, rhyme, direction = 1, debug=False):
    if direction == 1:
        start = 1
        end = number_of_friends + 1
    elif direction == -1:
        start = number_of_friends
        end = 1

    friends = [i for i in range(start, end, direction)]

    if direction == -1:
        friends.insert(0, 1)

    pointer = 0



    while len(friends) > 1:
        pointer += rhyme - 1
        pointer %= len(friends)

        if debug:
            print('removing friend {}'.format(friends[pointer]))
        del friends[pointer]

    if debug:
        print('friend {} is the last one left'.format(friends[0]))
    return friends[0]


def run_tests(dictionary, func):
    for input, expected in dictionary.items():
        result = func(*input)
        if result == expected:
            passed = "Passed!"
        else:
            passed = "Failed!"
        print('Testing input: {} Expected: {} Got: {} \t\t{}'.format(input, expected, result, passed))


if __name__ == "__main__":

    d = {
        (7, 3): 4,
        (6, 4): 5,
        (40, 1): 40,
        (20, 8): 1,
        (37, 19): 27,
        (200, 200): 149,
        (230, 173): 230,
        (555, 444): 31,
        (999, 82): 9,
        (82, 999): 49
    }
    print('Question 1a:')
    print()

    run_tests(d, circle)
    print()

    print('Question 1b:')
    print()
    circle(12, 5, debug=True)
    print()

    print('Question 1c:')
    for i in range(1, 100):
        if circle(100, i, -1) == circle(100, i, 1):
            print(i)
            break