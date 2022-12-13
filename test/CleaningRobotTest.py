import unittest
from unittest.mock import patch
from CleaningRobot import CleaningRobot
from CleaningRobotError import CleaningRobotError


class CleaningRobotTest(unittest.TestCase):
    """
    Your tests go here
    """

    def setUp(self) -> None:
        self.rb = CleaningRobot(2, 2)

    def test_initialize_robot(self):
        self.rb.initialize_robot()
        coordinates = self.rb.pos_y + self.rb.pos_x + self.rb.facing
        self.assertEqual(coordinates, '00N')

    def test_robot_status(self):
        self.rb.initialize_robot()
        coordinates = self.rb.robot_status()
        self.assertEqual(coordinates, '00N')

