DRONE_MOVE_FORWARD = 1
DRONE_MOVE_BACKWARD = 2
DRONE_MOVE_UP = 3
DRONE_MOVE_DOWN = 4
DRONE_MAX_ALTITUDE = 1000

_dron_last_serial_number = 1

drone = {
    'model': '',
    'serial_number': '',
    'current_payload': 0,
    'current_speed': 0,
    'current_altitude': 0
}


def drone_init(drone, model, payload, current_altitude=0):
    global _dron_last_serial_number
    drone['model'] = model
    drone['current_payload'] = payload
    drone['serial_number'] = f'{drone["model"]} - SN: {_dron_last_serial_number}'
    drone['current_altitude'] = current_altitude
    drone['driver'] = ...
    _dron_last_serial_number += 1


def drone_move(drone, speed, direction):
    # send low-leer commadn to drone['driver']
    drone['driver']


def drone_info(drone):
    print('Drone info: ', drone['model'], drone['serial_number'], drone['current_altitude'])


def drone_move_up(drone, speed):
    drone_info(drone)
    if drone['current_altitude'] == DRONE_MAX_ALTITUDE:
        print('ERROR: Can\'t move up')
    drone_move(drone, speed, DRONE_MOVE_UP)


def drone_move_down(drone, speed):
    drone_info(drone)
    if drone['current_altitude'] == 0:
        print('ERROR: Can\'t move down')
    drone_move(drone, speed, DRONE_MOVE_DOWN)


#####
dr1 = drone.copy()
drone_init(dr1, 'XS-100', 10)

dr2 = drone.copy()
drone_init(dr2, 'XS-200', 20, current_altitude=0)

drone_move_up(dr1, 10)
drone_move_down(dr2, 5)
