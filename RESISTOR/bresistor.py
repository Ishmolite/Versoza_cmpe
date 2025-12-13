import math


def get_resistance_material(resistivity, length, area):
    resistance = (resistivity * length) / area
    print(f"Resistance is {resistance} ohms")
    print("=================================================")
    return resistance

def get_resistance_by_iv(voltage, current):
    resistance = voltage / current
    print(f"Resistance is {resistance} ohms")
    print("=================================================")
    return resistance


''' Runs the command from the value given in mainRunner.py root file'''
if __name__ == "__main__":  #Acts as debug
    get_resistance_material(0.005, 10, 8)
    get_resistance_by_iv(3.0, 3.0)
