from unittest import TestCase
import python.Day12
from python.Day12 import NORTH_SOUTH, EAST_WEST, ORIENTED, NORTH, SOUTH, EAST, WEST, WAYPOINT_NORTH_SOUTH, WAYPOINT_EAST_WEST


class TestDay12(TestCase):

    def test_forward_10_action(self):
        state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 0}
        action = 'F10'
        expected_state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 10}

        self.assertEqual(expected_state, python.Day12.compute_state(state, action))

    def test_west_10_action(self):
        state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 5}
        expected_state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: -5}

        self.assertEqual(expected_state, python.Day12.west_action(state, 10))

    def test_rotate_90_left_action(self):
        state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: -5}
        expected_state = {ORIENTED: NORTH, NORTH_SOUTH: 0, EAST_WEST: -5}

        self.assertEqual(expected_state, python.Day12.rotate_left_action(state, 90))

    def test_rotate_180_left_action(self):
        state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: -5}
        expected_state = {ORIENTED: WEST, NORTH_SOUTH: 0, EAST_WEST: -5}

        self.assertEqual(expected_state, python.Day12.rotate_left_action(state, 180))

    def test_rotate_360_left_action(self):
        state = {ORIENTED: SOUTH, NORTH_SOUTH: 0, EAST_WEST: 0}
        expected_state = {ORIENTED: SOUTH, NORTH_SOUTH: 0, EAST_WEST: 0}

        self.assertEqual(expected_state, python.Day12.rotate_left_action(state, 360))

    def test_rotate_270_left_action(self):
        state = {ORIENTED: SOUTH, NORTH_SOUTH: 0, EAST_WEST: 0}
        expected_state = {ORIENTED: WEST, NORTH_SOUTH: 0, EAST_WEST: 0}

        self.assertEqual(expected_state, python.Day12.rotate_left_action(state, 270))

    def test_rotate_270_RIGHT_action(self):
        state = {ORIENTED: SOUTH, NORTH_SOUTH: 0, EAST_WEST: 0}
        expected_state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 0}

        self.assertEqual(expected_state, python.Day12.rotate_right_action(state, 270))


    def test_compute_result1_result_must_be_25(self):
        commands_input = ['F10', 'N3', 'F7', 'R90', 'F11']
        state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 0}
        self.assertEqual(25, python.Day12.compute_result1(state, commands_input))

    def test_forward_10_v2_action(self):
        state = {WAYPOINT_NORTH_SOUTH:1, WAYPOINT_EAST_WEST: 10, NORTH_SOUTH: 0, EAST_WEST: 0}
        expected_state = {WAYPOINT_NORTH_SOUTH:1, WAYPOINT_EAST_WEST: 10, NORTH_SOUTH: 10, EAST_WEST: 100}
        self.assertEqual(expected_state, python.Day12.forward_action_v2(state, 10))

    def test_rotate_right_90_v2_action(self):

        state = {WAYPOINT_NORTH_SOUTH:4, WAYPOINT_EAST_WEST: 10, NORTH_SOUTH: 38, EAST_WEST: 170}
        expected_state = {WAYPOINT_NORTH_SOUTH:-10, WAYPOINT_EAST_WEST: 4, NORTH_SOUTH: 38, EAST_WEST: 170}
        self.assertEqual(expected_state, python.Day12.rotate_right_action_v2(state, 90))

    def test_compute_result2_result_must_be_286(self):
        commands_input = ['F10', 'N3', 'F7', 'R90', 'F11']
        state = {WAYPOINT_NORTH_SOUTH:1, WAYPOINT_EAST_WEST: 10, NORTH_SOUTH: 0, EAST_WEST: 0}
        self.assertEqual(286, python.Day12.compute_result2(state, commands_input))