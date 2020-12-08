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

def parse_input(file):
    code = []
    for line in file:
        code.append(parse_line(line))
    return code

def parse_line(line):
    m = re.match('^(?P<opcode>\w{3})\s(?P<arg1>(\+|-)\d+)', line.strip())
    line_parsed = m.groupdict()
    return {'opcode': line_parsed['opcode'], 'arg1': line_parsed['arg1'] }


def main():
    with open('../input_day8_1.txt') as fp:
        code = parse_input(fp)
        handheld = Handheld()
        handheld.load(code)
        handheld.run_before_loop()
        print(f'Result 1 is {handheld.accumulator}')

if __name__ == '__main__':
    main()
