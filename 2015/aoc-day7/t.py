import operator

import numpy as np


class Solver(object):
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

    def solve(self, instructions):
        self.make_inputs(instructions)
        self.make_outputs()

    def make_inputs(self, instructions):
        for instruction in instructions.splitlines():
            self.parse(instruction)

    def parse(self, instruction):
        (ops, wire) = instruction.split(" -> ")
        self.inputs[wire] = ops.split()

    def make_outputs(self):
        keys = set(self.inputs.keys())
        while keys:
            for key in keys.copy():
                try:
                    self.outputs[key] = self.do_instruction(self.inputs[key])
                    keys.remove(key)
                except KeyError:
                    continue

    def do_instruction(self, instruction):
        if len(instruction) == 1:
            return self.get_value(instruction[0])
        elif len(instruction) == 2:
            return ~self.get_value(instruction[1])
        elif len(instruction) == 3:
            operations = {
                "AND": operator.and_,
                "OR": operator.or_,
                "LSHIFT": operator.lshift,
                "RSHIFT": operator.rshift,
            }

            in_1 = self.get_value(instruction[0])
            op = instruction[1]
            in_2 = self.get_value(instruction[2])
            return operations[op](in_1, in_2)

    def get_value(self, item):
        if item in self.inputs:
            return np.uint16(self.outputs[item])
        else:
            return np.uint16(item)


def part_one():
    solver = Solver()
    with open("7.txt") as input_file:
        solver.solve(input_file.read())
    print("Wire a: {}".format(solver.outputs["a"]))


def part_two():
    with open("7.txt") as input_file:
        input_text = input_file.read()

    solver = Solver()
    solver.make_inputs(input_text)
    in1 = solver.inputs
    solver.make_outputs()
    a_value = solver.outputs["a"]

    modified_solver = Solver()
    modified_solver.make_inputs(input_text)
    in2 = modified_solver.inputs
    in2["b"] = [str(a_value)]
    print(in1 == in2)
    modified_solver.inputs["b"] = [str(a_value)]
    modified_solver.make_outputs()
    new_a_value = modified_solver.outputs["a"]
    print("New wire a: {}".format(new_a_value))


if __name__ == "__main__":
    part_one()
    part_two()
