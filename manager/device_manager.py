from classes.motor import Motor
from classes.sensor import Sensor
from classes.controller import Controller
from classes.device_type import DeviceType
from classes.sensor_type import SensorType


class DeviceManager:
    def __init__(self, devices=[]):
        self.__devices = devices

    def __del__(self):
        pass

    def add_device(self, device):
        self.__devices.append(device)

    def find_device_by_type(self, device_type: DeviceType):
        found_devices = []
        for device in self.__devices:
            if device.device_type == device_type:
                found_devices.append(device)
        return found_devices

    def sort_by_manufacturer(self, reverse=False):
        sorted_devices = sorted(self.__devices, key=lambda device: device.manufacturer, reverse=reverse)

        return sorted_devices

    def sort_by_consumtion(self, reverse=False):
        sorted_devices = sorted(self.__devices, key=lambda device: device.current_consumption_in_watts, reverse=reverse)

        return sorted_devices
