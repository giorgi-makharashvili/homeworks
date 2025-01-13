def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left < distance_to_pump / mpg:
        return False
    else:
        return True