class Robot:
    FORWARD = 1
    BACKWARD = 2
    RIGHT = 3
    LEFT = 4

    MAX_SPEED = 25

    _last_serial_number = 0

    def __init__(self, model, current_speed=0):
        print('__init__:', model, current_speed)
        self.model = model
        self.serial_number = f'{self.model} - SN: {Robot._last_serial_number}'
        self.current_speed = 0
        self.driver = ...
        Robot._last_serial_number += 1

    def _move(self, speed, direction):
        self.driver

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Robot moving forward')
        self._move(speed, self.FORWARD)

    def move_backward(self, speed):
        print(self.model, self.serial_number, 'Robot moving backward')
        self._move(speed, self.BACKWARD)

    def turn_right(self):
        print(self.model, self.serial_number, 'Robot turning right')
        self._move(self.RIGHT)

    def turn_left(self):
        print(self.model, self.serial_number, 'Robot turning left')
        self._move(self.LEFT)


class SpotMini(Robot):
    def __init__(self, model, current_speed, legs_response=4):
        super().__init__(model, current_speed)
        self.legs_response = legs_response

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Robot SpotMini moving forward')
        if self.legs_response < 4:
            self.current_speed = 0
            print('Warning! The legs are broken! All 4 legs mast be operable!')
        self._move(speed, self.FORWARD)


class Atlas(Robot):
    def __init__(self, model, current_speed, battery_level=100):
        super().__init__(model, current_speed)
        self.battery_level = battery_level

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Robot Atlas moving forward')
        if self.battery_level < 25:
            print('Warning! Low battery! Please recharge!')
        self._move(speed, self.FORWARD)


class Handle(Robot):
    def __init__(self, model, current_speed, distance_to_base=0):
        super().__init__(model, current_speed)
        self.distance_to_base = distance_to_base

    def move_forward(self, speed):
        print(self.model, self.serial_number, 'Robot Handle moving forward')
        if self.distance_to_base >= 100:
            print('Warning! You are too far from the base!')
        self._move(speed, self.FORWARD)


robot1 = SpotMini('SpotMini_Prototype_001', 15, 4)
robot1.move_forward(15)

robot2 = Atlas('Atlas_Prototype_001', 10, 75)
robot2.move_forward(10)

robot3 = Handle('Handle_Prototype_001', 20, 50)
robot3.move_forward(20)
