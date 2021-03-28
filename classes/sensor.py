from classes.device import Device
from classes.sensor_type import SensorType
from classes.device_type import DeviceType

class Sensor(Device):
    def __init__(self, price: float, operating_voltage_in_watts: float, current_consumption_in_watts: float,
                 model_name: str, manufacturer: str, sensor_type: SensorType):

        super().__init__(price, operating_voltage_in_watts, current_consumption_in_watts,
                         DeviceType.SENSOR, model_name, manufacturer)
        self.__sensor_type = sensor_type
        self.__value = None

    def __del__(self):
        pass
    def __str__(self):
        return super(Sensor, self).__str__() + f'It is {self.sensor_type.value} sensor\n'

    @property
    def sensor_type(self):
        return self.__sensor_type

    def check_value(self):
        return __value

