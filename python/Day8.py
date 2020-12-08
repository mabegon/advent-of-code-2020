import re


class Handheld():
    OP_NOP = 'nop'
    OP_ACC = 'acc'
    OP_JMP = 'jmp'
    accumulator = 0
    head = None
    stack = None
    stack_visited = {}

    def load(self, code):
        if code is not None and len(code) > 0:
            self.stack = code
            self.head = 0
            self.accumulator = 0
            self.stack_visited = {}

    def compute(self, operation):
        if operation['opcode'] == self.OP_NOP:
            self.head += 1
        elif operation['opcode'] == self.OP_ACC:
            self.head += 1
            self.accumulator += int(operation['arg1'])
        elif operation['opcode'] == self.OP_JMP:
            self.head += int(operation['arg1'])

    def run_before_loop(self):
        while self.head not in self.stack_visited.keys():
            self.stack_visited[self.head] = True
            self.compute(self.stack[self.head])

    def run_protected(self):
        while self.head not in self.stack_visited.keys() and self.head < len(self.stack):
            self.stack_visited[self.head] = True
            self.compute(self.stack[self.head])
        if self.head == len(self.stack):
            return True
        else:
            return False


def found_fixed_code(code):
    positions = range(0, len(code) - 1)
    h = Handheld()
    for position in positions:
        fixed_code = code[:]
        if fixed_code[position]['opcode'] in [Handheld.OP_NOP, Handheld.OP_JMP]:
            original = fixed_code[position]
            if original['opcode'] == Handheld.OP_NOP:
                fixed_position = {'opcode': Handheld.OP_JMP, 'arg1': original['arg1']}
            elif original['opcode'] == Handheld.OP_JMP:
                fixed_position = {'opcode': Handheld.OP_NOP, 'arg1': original['arg1']}
            fixed_code[position] = fixed_position
            h.load(fixed_code)
            if h.run_protected():
                return fixed_code
            else:
                fixed_code[position] = original
    return None


def parse_input(file):
    code = []
    for line in file:
        code.append(parse_line(line))
    return code


def parse_line(line):
    m = re.match('^(?P<opcode>\w{3})\s(?P<arg1>(\+|-)\d+)', line.strip())
    line_parsed = m.groupdict()
    return {'opcode': line_parsed['opcode'], 'arg1': line_parsed['arg1']}


def main():
    with open('../input_day8_1.txt') as fp:
        code = parse_input(fp)
        handheld = Handheld()
        handheld.load(code)
        handheld.run_before_loop()
        print(f'Result 1 is {handheld.accumulator}')

        fixed_code = found_fixed_code(code)
        handheld.load(fixed_code)
        handheld.run_protected()
        print(f'Result 2 is {handheld.accumulator}')


if __name__ == '__main__':
    main()
