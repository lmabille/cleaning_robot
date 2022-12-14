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
        self.assertEqual(coordinates, '(0,0,N)')

    @patch.object(GPIO, 'input')
    def test_manage_battery_1(self, mock_input):
        mock_input.return_value = 3
        self.rb.initialize_robot()
        self.rb.manage_battery()
        self.assertTrue(self.rb.battery_led_on)
        self.assertFalse(self.rb.cleaning_system_on)

    @patch.object(GPIO, 'input')
    def test_manage_battery_2(self, mock_input):
        mock_input.return_value = 12
        self.rb.manage_battery()
        self.assertTrue(self.rb.cleaning_system_on)
        self.assertFalse(self.rb.battery_led_on)

    @patch.object(GPIO, 'input')
    def test_execute_command_no_obstacle_1(self, mock_input):
        mock_input.side_effect = [12, 0] #[input1, input2] -> input1 for battery, input2 for infrared sensor
        self.rb.initialize_robot()
        self.rb.execute_command('l')
        status = self.rb.robot_status()
        self.assertEqual('(0,0,W)', status )

    @patch.object(GPIO, 'input')
    def test_execute_command_no_obstacle_2(self, mock_input):
        mock_input.side_effect = [12, 0]
        self.rb.initialize_robot()
        self.rb.execute_command('r')
        status = self.rb.robot_status()
        self.assertEqual('(0,0,E)', status )

    @patch.object(GPIO, 'input')
    def test_execute_command_no_obstacle_3(self, mock_input):
        mock_input.side_effect = [12, 0]
        self.rb.pos_x = '1'
        self.rb.pos_y = '1'
        self.rb.facing = 'E'
        self.rb.execute_command('r')
        status = self.rb.robot_status()
        self.assertEqual('(1,1,S)', status )

    @patch.object(GPIO, 'input')
    def test_execute_command_no_obstacle_4(self, mock_input):
        mock_input.side_effect = [12, 0]
        self.rb.pos_x = '1'
        self.rb.pos_y = '1'
        self.rb.facing = 'E'
        self.rb.update_status()
        self.rb.execute_command('r')
        status = self.rb.robot_status()
        self.assertEqual('(1,1,S)', status )

    @patch.object(GPIO, 'input')
    def test_execute_command_with_obstacle_1(self, mock_input):
        mock_input.side_effect = [12, 3]
        self.rb.pos_x = '1'
        self.rb.pos_y = '1'
        self.rb.facing = 'E'
        self.rb.update_status()
        self.rb.execute_command('f')
        status = self.rb.robot_status()
        self.assertEqual('(1,1,E)(2,1)', status)

    @patch.object(GPIO, 'input')
    def test_execute_command_no_obstacle_no_battery(self, mock_input):
        mock_input.side_effect = [0, 0]
        self.rb.pos_x = '1'
        self.rb.pos_y = '1'
        self.rb.facing = 'E'
        self.rb.execute_command('r')
        status = self.rb.robot_status()
        self.assertEqual('(1,1,E)', status)






