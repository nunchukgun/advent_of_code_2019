def main():
    file = open('input.txt')
    range_start, range_stop = [int(num) for num in file.readline().split('-')]

    potential_passwords = build_potential_passwords(range_start, range_stop)

    print(len(potential_passwords))


    print("day_four")


def build_potential_passwords(range_start, range_stop):
    potential_passwords = []

    for i in range(range_start, range_stop):
        if has_adjacent_digits_outside_a_greater_pattern(str(i)) and digits_do_not_descend(str(i)):
            potential_passwords.append(i)

    return potential_passwords


def has_adjacent_digits_outside_a_greater_pattern(num_str):
    consec_chars_list = build_consec_chars_list(num_str)
    binary_adjacents_list = list(filter(lambda str: (len(str) == 2), consec_chars_list))
    return len(binary_adjacents_list) > 0


def build_consec_chars_list(my_str):
    consec_substrings = []

    previous_char = None
    block_start_idx = 0

    for i in range(0, len(my_str)):
        current_char = my_str[i]
        next_char = my_str[i + 1] if i < len(my_str) - 1 else None
        if current_char != previous_char:
            block_start_idx = i
        if current_char != next_char:
            sub_str = my_str[block_start_idx: i + 1]
            consec_substrings.append(sub_str)
        previous_char = my_str[i]

    return consec_substrings


def digits_do_not_descend(num_str):
    for i in range(len(num_str) - 1):
        next_digit = int(num_str[i + 1])
        current_digit = int(num_str[i])
        if next_digit < current_digit:
            return False
    return True


if __name__ == "__main__":
    main()