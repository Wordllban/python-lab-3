from classes.device_type import DeviceType

class Device:
    def __init__(self, price: float, operating_voltage_in_watts: float, current_consumption_in_watts: float,
                 device_type: DeviceType, model_name: str, manufacturer: str):
        self.__price = price
        self.__operating_voltage_in_watts = operating_voltage_in_watts
        self.__current_consumption_in_watts = current_consumption_in_watts
        self.__device_type = device_type
        self.__model_name = model_name
        self.__manufacturer = manufacturer
        self.__is_powered = False

    def __del__(self):
        pass

    def switch_power(self):
        self.__is_powered = not self.__is_powered

    def __str__(self):
        return f'Price: {self.price}\n' \
        f'Voltage: {self.operating_voltage_in_watts}\n' \
        f'Consumption: {self.current_consumption_in_watts}\n' \
        f'Model name: {self.model_name}\n' \
        f'Manufacturer: {self.manufacturer}\n'


    @property
    def device_type(self):
        return self.__device_type
    @property
    def price(self):
        return self.__price
    @property
    def operating_voltage_in_watts(self):
        return self.__operating_voltage_in_watts
    @property
    def current_consumption_in_watts(self):
        return self.__current_consumption_in_watts
    @property
    def model_name(self):
        return self.__model_name
    @property
    def manufacturer(self):
        return self.__manufacturer
    @property
    def is_powered(self):
        return self.__is_powered


