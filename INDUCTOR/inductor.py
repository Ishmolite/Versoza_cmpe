import math

def get_inductance_material(permeability, relativep, turns, area, length):
    inductance = (permeability * relativep * turns * turns * area) / length
    print(f"Inductance is {inductance} henry")
    print("=================================================")
    return inductance

def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print(f"Reactance is {reactance} ohms")
    return reactance

if __name__ == "__main__": #Acts as debug
    get_inductive_reactance(100000, 0.0000005)
