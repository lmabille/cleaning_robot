import unittest
from unittest.mock import patch
from CleaningRobot import CleaningRobot
from CleaningRobotError import CleaningRobotError
from mock import GPIO


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

    @patch.object(GPIO, 'input')
    def test_manage_battery_1(self, mock_input):
        mock_input.return_value = 3
        self.rb.manage_battery()
        self.assertTrue(self.rb.battery_led_on)
        self.assertFalse(self.rb.cleaning_system_on)

    @patch.object(GPIO, 'input')
    def test_manage_battery_2(self, mock_input):
        mock_input.return_value = 12
        self.rb.manage_battery()
        self.assertTrue(self.rb.cleaning_system_on)
        self.assertFalse(self.rb.battery_led_on)



