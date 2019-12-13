def main():
    file = open("input.txt", 'r', encoding="utf-8")
    input_line = [line.rstrip() for line in file][0].split(',')
    run_intcode_computer(input_line)


def run_intcode_computer(input_line):
    print('run_intcode_computer START')
    instruction_start_index = 0
    while input_line[instruction_start_index] != "99":
        operation = input_line[instruction_start_index]
        padded_operation = pad_operation(operation)
        op_type = get_op_type(padded_operation)
        instruction_length = get_instruction_length(op_type)
        instruction_params = input_line[instruction_start_index + 1: instruction_start_index + instruction_length]
        params_with_modes = get_params_with_modes(padded_operation, instruction_params)

        execute_instruction(op_type, params_with_modes, input_line)

        instruction_start_index = instruction_start_index + instruction_length


def pad_operation(operation):
    instr_copy = str(operation)[:]
    while len(instr_copy) < 5:
        instr_copy = '0' + instr_copy

    return instr_copy


def get_op_type(padded_operation):
    return padded_operation[3:5]


def get_instruction_length(op_type):
    if op_type in ["01", "02"]:
        return 4
    elif op_type == "99":
        return 0
    else:
        return 2


def get_params_with_modes(padded_operation, instruction_params):
    params_with_modes = []
    op_params = padded_operation[-3::-1]
    for i in range(len(instruction_params)):
        params_with_modes.append({
            "param": instruction_params[i],
            "mode": op_params[i]
        })

    return params_with_modes


def execute_instruction(op_type, params_with_modes, input_line):
    if op_type == "01":
        operand_1 = get_param_value(params_with_modes[0], input_line)
        operand_2 = get_param_value(params_with_modes[1], input_line)
        destination = params_with_modes[2]["param"]

        input_line[int(destination)] = operand_1 + operand_2
    elif op_type == "02":
        operand_1 = get_param_value(params_with_modes[0], input_line)
        operand_2 = get_param_value(params_with_modes[1], input_line)
        destination = params_with_modes[2]["param"]

        input_line[int(destination)] = operand_1 * operand_2
    elif op_type == "03":
        input_value = input("Please enter an integer: ")
        destination = params_with_modes[0]["param"]

        input_line[int(destination)] = input_value
    elif op_type == "04":
        output_value = get_param_value(params_with_modes[0], input_line)
        print(output_value)


def get_param_value(param_with_mode, input_line):
    mode = param_with_mode["mode"]
    param = param_with_mode["param"]
    if mode == "0":
        return int(input_line[int(param)])
    else:
        return int(param)


def get_num_of_params(op_type):
    return get_instruction_length(op_type) - 1


if __name__ == "__main__":
    main()