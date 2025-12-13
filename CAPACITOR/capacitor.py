import math

def get_capacitance_by_cv(charge, voltage):
    capacitance = charge / voltage
    print(f"Capacitance is {capacitance} farad")
    print("=================================================")
    return capacitance

def get_capacitance_material(permittivity, relativep, area, distance):
    capacitance = (permittivity * relativep * area) / distance
    print(f"Capacitance is {capacitance} farad")
    print("=================================================")
    return capacitance

def get_capacitive_reactance(frequency, capacitance):
    reactance = 1 / ( 2 * math.pi * frequency * capacitance)
    print(f"Capacitive reactance is {reactance} ohms")
    return reactance

if __name__ == '__main__':
    get_capacitance_by_cv(10, 10)