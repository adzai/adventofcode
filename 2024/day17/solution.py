def handle_combo_operand(operand, registers):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case 7:
            raise Exception("Invalid operand 7")
        case _:
            raise Exception(f"Unhandled operand {operand}")


def handle_instruction(registers, instruction_ptr, instruction_vals):
    opcode = instruction_vals[instruction_ptr]
    operand = instruction_vals[instruction_ptr + 1]
    has_jumped = False
    ret = None
    match opcode:
        case 0:
            registers["A"] = registers["A"] // 2 ** handle_combo_operand(operand, registers)
        case 1:
            registers["B"] ^= operand
        case 2:
            registers["B"] = handle_combo_operand(operand, registers) % 8
        case 3:
            if registers["A"] != 0:
                instruction_ptr = operand
                has_jumped = True
        case 4:
            registers["B"] ^= registers["C"]
        case 5:
            ret = handle_combo_operand(operand, registers) % 8
        case 6:
            registers["B"] = registers["A"] // 2 ** handle_combo_operand(operand, registers)
        case 7:
            registers["C"] = registers["A"] // 2 ** handle_combo_operand(operand, registers)

    if not has_jumped:
        instruction_ptr += 2

    return ret, instruction_ptr


def get_output_from_instructions(instructions, registers):
    outputs = []
    instruction_ptr = 0
    while instruction_ptr + 1 < len(instructions):
        ret, instruction_ptr = handle_instruction(registers, instruction_ptr, instructions)

        if ret is not None:
            outputs.append(ret)

    return outputs


def get_a_value_that_produces_target(target, target_slice_start_idx, current_a_value):
    if target_slice_start_idx < 0:
        return current_a_value

    for offset in range(8):
        a_value_to_consider = current_a_value * 8 + offset
        if (
            get_output_from_instructions(target, {"A": a_value_to_consider, "B": 0, "C": 0})
            == target[target_slice_start_idx:]
        ):
            new_a_value = get_a_value_that_produces_target(target, target_slice_start_idx - 1, a_value_to_consider)

            if new_a_value is not None:
                return new_a_value

    return None


if __name__ == "__main__":
    registers = {}
    with open("input.txt") as f:
        input_data = f.read().split("\n\n")
        for register in input_data[0].split("\n"):
            reg_name, reg_value = register.replace("Register ", "").split(": ")
            registers[reg_name] = int(reg_value)

        instructions = list(map(lambda x: int(x), input_data[-1].replace("Program: ", "").replace("\n", "").split(",")))

    print("Part 1:", ",".join(list(map(lambda x: str(x), get_output_from_instructions(instructions, registers)))))

    print("Part 2:", get_a_value_that_produces_target(instructions, len(instructions) - 1, 0))
