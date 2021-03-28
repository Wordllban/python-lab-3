from classes.device import Device
from classes.device_type import DeviceType

class Controller(Device):
    def __init__(self, price: float, operating_voltage_in_watts: float, current_consumption_in_watts: float,
                 model_name: str, manufacturer: str, total_numbers_of_pins: int, analog_pins: int, digital_pins: int,
                 I2C_pin: bool):
        super().__init__(price, operating_voltage_in_watts, current_consumption_in_watts,
                         DeviceType.CONTROLLER, model_name, manufacturer)
        self.__total_numbers_of_pins = total_numbers_of_pins
        self.__analog_pins = analog_pins
        self.__digital_pins = digital_pins
        self.__I2C_pin = I2C_pin

    def __del__(self):
        pass

    def __str__(self):
        return super(Controller, self).__str__() + f'Total numbers of pins: {self.total_numbers_of_pins}\n' \
                                                   f'Analog pins: {self.analog_pins}\n' \
                                                   f'Digital pins: {self.digital_pins}\n' \
                                                   f'I2C pin: {self.I2C_pin}\n'
    @property
    def total_numbers_of_pins(self):
        return self.__total_numbers_of_pins

    @property
    def analog_pins(self):
        return self.__analog_pins

    @property
    def digital_pins(self):
        return self.__digital_pins

    @property
    def I2C_pin(self):
        return self.__I2C_pin

    def reset(self):
        analog_pins = None
        digital_pins = None
        I2C_pin = None
