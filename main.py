from manager.device_manager import DeviceManager
from classes.motor import Motor
from classes.sensor import Sensor
from classes.controller import Controller
from classes.device_type import DeviceType
from classes.sensor_type import SensorType

if __name__ == '__main__':
    devices = [
    Motor(325.5, 3.2, 0.7, "Top Motor", "China", 3228),
    Motor(333.5, 3.6, 0.9, "Nice Motor", "Ukraine", 3228),

    Controller(230, 2.55, 0.76, "Arduino Mega", "USA", 28, 16, 10, True),
    Controller(220, 2.55, 0.76, "Arduino Nano", "China", 28, 16, 10, True),
    Controller(210, 2.55, 0.76, "Arduino NoName", "Vietnam", 28, 16, 10, True),

    Sensor(430, 2.66, 1.13, "Humidity Sensor", "China", SensorType.HUMIDITY),
    Sensor(430, 2.66, 1.13, "Sound Sensor", "USA", SensorType.SOUND),
    Sensor(430, 2.66, 1.13, "Touch Sensor", "Ukraine", SensorType.TOUCH)]

    manager = DeviceManager(devices)

    motor = Motor(350.5, 2.3, 0.8, "Bad Motor", "Vietnam", 3228)
    manager.add_device(motor)

    devices_sorted_by_manufacturer = manager.sort_by_manufacturer()
    for device in devices_sorted_by_manufacturer:
        print(device)

    print("_______________")

    devices_sorted_by_consumption = manager.sort_by_consumtion(reverse=True)
    for device in devices_sorted_by_consumption:
        print(device)

    print("_______________")

    found_sensors = manager.find_device_by_type(DeviceType.SENSOR)
    for sensor in found_sensors:
        print(sensor)