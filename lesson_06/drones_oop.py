class Drone:
    FORWARD = 1
    BACKWARD = 2
    UP = 3
    DOWN = 4

    MAX_SPEED = 100
    MAX_ALTITUDE = 1000
    MAX_PAYLOAD = 10

    _last_serial_number = 0

    def __init__(self, model, current_payload, current_altitude=0):
        print('__init__:', model, current_payload, current_altitude)
        self.model = model
        self.current_payload = current_payload
        self.serial_number = f'{self.model} - SN: {Drone._last_serial_number}'
        self.current_altitude = current_altitude
        self.current_speed = 0
        self.driver = ...
        Drone._last_serial_number += 1

    def _move(self, speed, direction):
        # send low-evel commadn to self.driver
        self.driver

    def move_backward(self, speed):
        print(self.model)
        self._move(speed, self.BACKWARD)

    def move_down(self, speed):
        print(self.model, self.serial_number, 'moving down...')
        if self.current_altitude == 0:
            print('ERROR: Can\'t move down')
        self._move(speed, self.DOWN)


dr1 = Drone('XS-100', 10, current_altitude=100)  # __init__
dr2 = Drone('XS-200', 20)

dr1.move_down(10)
dr2.move_down(10)
