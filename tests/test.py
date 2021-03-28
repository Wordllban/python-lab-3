import unittest
from classes.motor import Motor
from classes.sensor import Sensor
from classes.controller import Controller
from classes.sensor_type import SensorType
from classes.device import Device
from manager.device_manager import DeviceManager
from classes.device_type import DeviceType


class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.test_device_list = [
                Sensor(430, 2.66, 1.13, "Humidity Sensor", "China", SensorType.HUMIDITY),
                Sensor(430, 2.66, 1.13, "Sound Sensor", "USA", SensorType.SOUND),
                Sensor(430, 2.66, 1.13, "Touch Sensor", "Ukraine", SensorType.TOUCH),
                Controller(230, 2.55, 0.76, "Arduino Mega", "USA", 28, 16, 10, True),
                Controller(220, 2.55, 0.76, "Arduino Nano", "China", 28, 16, 10, True),
                Controller(210, 2.55, 0.76, "Arduino NoName", "Vietnam", 28, 16, 10, True),
                Motor(325.5, 3.2, 0.7, "Top Motor", "China", 3228),
                Motor(333.5, 3.6, 0.9, "Nice Motor", "Ukraine", 3228)
                                ]

        self.d_manager = DeviceManager(self.test_device_list)

    def test_find_device_by_type(self):
        actual = self.d_manager.find_device_by_type(DeviceType.SENSOR)
        expected = list(filter(lambda device: device.device_type == DeviceType.SENSOR, self.test_device_list))
        self.assertEqual(actual, expected)

    def test_sort_by_manufacturer(self):
        actual = self.d_manager.sort_by_manufacturer(reverse=False)
        expected = sorted(self.test_device_list, key=lambda device: device.manufacturer, reverse=False)
        self.assertEqual(actual, expected)

    def test_sort_by_consumtion(self):
        actual = self.d_manager.sort_by_consumption(reverse=False)
        expected = sorted(self.test_device_list, key=lambda device: device.current_consumption_in_watts, reverse=False)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
