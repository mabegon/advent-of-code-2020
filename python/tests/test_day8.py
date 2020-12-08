from unittest import TestCase

from python.Day8 import Handheld, parse_input, found_fixed_code


class TestDay8(TestCase):
    def test_handheld_accululator_must_be_0_when_obj_is_created(self):
        handheld = Handheld()
        self.assertEqual(0, handheld.accumulator)

    def test_handheld_stack_head_must_be_None_when_obj_is_created(self):
        handheld = Handheld()
        self.assertEqual(None, handheld.head)

    def test_handheld_stack_head_must_be_0_when_code_is_loaded(self):
        handheld = Handheld()
        code = [{'operation': handheld.OP_NOP, 'arg1': '+0'}]
        handheld.load(code)
        self.assertEqual(0, handheld.head)

    def test_handheld_accumulator_must_be_0_when_code_is_loaded(self):
        handheld = Handheld()
        code = [{'operation': handheld.OP_NOP, 'arg1': '+0'}]
        handheld.accumulator = 1
        handheld.load(code)
        self.assertEqual(0, handheld.accumulator)


    def test_handheld_stack_head_must_be_None_if_code_loaded_is_empty(self):
        handheld = Handheld()
        code = []
        handheld.load(code)
        self.assertEqual(None, handheld.head)

    def test_compute_nop_operation_do_nothing_but_update_head(self):
        handheld = Handheld()
        handheld.accumulator = 0
        handheld.head = 0
        operation = {'opcode': handheld.OP_NOP, 'arg1': '+0'}
        handheld.compute(operation)  # add state to compute params in order to evict side effects
        self.assertEqual(0, handheld.accumulator)
        self.assertEqual(1, handheld.head)

    def test_compute_acc_add_value_to_accululator(self):
        handheld = Handheld()
        handheld.accumulator = 0
        handheld.head = 0
        operation = {'opcode': handheld.OP_ACC, 'arg1': '+1'}
        handheld.compute(operation)  # add state to compute params in order to evict side effects
        self.assertEqual(1, handheld.accumulator)
        self.assertEqual(1, handheld.head)

    def test_compute_acc_substract_value_to_accululator_when_value_is_neg(self):
        handheld = Handheld()
        handheld.accumulator = 0
        handheld.head = 0
        operation = {'opcode': handheld.OP_ACC, 'arg1': '-1'}
        handheld.compute(operation)  # add state to compute params in order to evict side effects
        self.assertEqual(-1, handheld.accumulator)
        self.assertEqual(1, handheld.head)

    def test_compute_jmp_add_value_to_head(self):
        handheld = Handheld()
        handheld.accumulator = 0
        handheld.head = 0
        operation = {'opcode': handheld.OP_JMP, 'arg1': '+5'}
        handheld.compute(operation)  # add state to compute params in order to evict side effects
        self.assertEqual(0, handheld.accumulator)
        self.assertEqual(5, handheld.head)

    def test_compute_jmp_substract_value_to_head_when_value_is_neg(self):
        handheld = Handheld()
        handheld.accumulator = 0
        handheld.head = 7
        operation = {'opcode': handheld.OP_JMP, 'arg1': '-4'}
        handheld.compute(operation)  # add state to compute params in order to evict side effects
        self.assertEqual(0, handheld.accumulator)
        self.assertEqual(3, handheld.head)

    def test_parse_input(self):
        code_expected = [{'opcode': Handheld.OP_NOP, 'arg1': '+0'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                         {'opcode': Handheld.OP_JMP, 'arg1': '+4'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+3'},
                         {'opcode': Handheld.OP_JMP, 'arg1': '-3'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '-99'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                         {'opcode': Handheld.OP_JMP, 'arg1': '-4'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+6'},
                         ]
        with open('./input_test_day8.txt') as fp:
            code = parse_input(fp)
            self.assertEqual(code_expected, code)

    def test_run_before_loop(self):
        handheld = Handheld()
        code = [{'opcode': Handheld.OP_NOP, 'arg1': '+0'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_JMP, 'arg1': '+4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+3'},
                {'opcode': Handheld.OP_JMP, 'arg1': '-3'},
                {'opcode': Handheld.OP_ACC, 'arg1': '-99'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_JMP, 'arg1': '-4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+6'},
                ]
        handheld.load(code)
        handheld.run_before_loop()
        self.assertEqual(5, handheld.accumulator)
        self.assertEqual(1, handheld.head)

    def test_run_must_finish(self):
        handheld = Handheld()
        code = [{'opcode': Handheld.OP_NOP, 'arg1': '+0'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_JMP, 'arg1': '+4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+3'},
                {'opcode': Handheld.OP_JMP, 'arg1': '-3'},
                {'opcode': Handheld.OP_ACC, 'arg1': '-99'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_NOP, 'arg1': '-4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+6'},
                ]
        handheld.load(code)
        finish = handheld.run_protected()
        self.assertTrue(finish)
        self.assertEqual(8, handheld.accumulator)

    def test_found_fixed_code(self):
        code = [{'opcode': Handheld.OP_NOP, 'arg1': '+0'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_JMP, 'arg1': '+4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+3'},
                {'opcode': Handheld.OP_JMP, 'arg1': '-3'},
                {'opcode': Handheld.OP_ACC, 'arg1': '-99'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                {'opcode': Handheld.OP_JMP, 'arg1': '-4'},
                {'opcode': Handheld.OP_ACC, 'arg1': '+6'},
                ]
        code_expected = [{'opcode': Handheld.OP_NOP, 'arg1': '+0'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                         {'opcode': Handheld.OP_JMP, 'arg1': '+4'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+3'},
                         {'opcode': Handheld.OP_JMP, 'arg1': '-3'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '-99'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+1'},
                         {'opcode': Handheld.OP_NOP, 'arg1': '-4'},
                         {'opcode': Handheld.OP_ACC, 'arg1': '+6'},
                         ]

        self.assertEqual(code_expected, found_fixed_code(code))
