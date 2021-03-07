from classes.device import Device
from classes.device_type import DeviceType

class Motor(Device):
    def __init__(self, price: float, operating_voltage_in_watts: float, current_consumption_in_watts: float,
                 model_name: str, manufacturer: str, revolutions_per_sec: float = None):

        super().__init__(price, operating_voltage_in_watts, current_consumption_in_watts,
                         DeviceType.MOTOR, model_name, manufacturer)
        self.__revolutions_per_sec = revolutions_per_sec

    def __del__(self):
        pass

    def __str__(self):
        return super(Motor, self).__str__() + f'Revolutions per sec: {self.revolutions_per_sec}\n'

    @property
    def revolutions_per_sec(self):
        return self.__revolutions_per_sec

    def change_revolutions_speed(self):
        self.__revolutions_speed = int(input("Set revolution speed: "))

        if self.__revolutions_speed <= 25:
            print("Revolution speed is low")
        elif 26 >= self.__revolutions_speed <= 50:
            print("Revolution speed is medium")
        elif 51 >= self.__revolutions_speed <= 100:
            print("Revolution speed is high")
        else:
            print("Astanavites")

