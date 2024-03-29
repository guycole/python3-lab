#
# Title:battery.py
# Description: cruise battery level report
#

import json

def get_cars():
    cars = '{"Beetle": "ce1K9WtMd5wXmAdb1", "BoltyMcBoltface": "Az6xYDIYdUA3I2EXq", "Penguin": "Kefkjfe39KJKf3234djkl"}'
    return json.loads(cars)

def get_battery_level(vin):
    battery_levels = '{"ce1K9WtMd5wXmAdb1": {"battery_level": 3}, "Az6xYDIYdUA3I2EXq": {"battery_level": 4}, "Kefkjfe39KJKf3234djkl": {"battery_level": 4}}'
    datum = json.loads(battery_levels)

    if vin in datum:
        return datum[vin].get('battery_level', -1)
    else:
        return -1

def battery_level_filter(candidates, level):
    filtered = dict((k, v) for k, v in candidates.items() if v == level)
    return list(filtered)

if __name__ == '__main__':
    print("main")

    car_batteries = {}

    cars = get_cars()
    for car in cars:
        car_batteries[car] = get_battery_level(cars[car])

    for battery_level in reversed(range(5)):
        print(f"Level {battery_level}")
        for candidate in battery_level_filter(car_batteries, battery_level):
            print(candidate)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
