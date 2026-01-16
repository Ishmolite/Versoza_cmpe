#This is a root file

from RESISTOR import bresistor
from CAPACITOR import capacitor
from INDUCTOR import inductor

print("Welcome to Electronics Calculators")

while True:

    selector = input("Please select your calculator: ")

    match selector.upper():
        case "RC_IV":
            voltage = float(input("Please enter voltage: "))
            current = float(input("Please enter current: "))
            bresistor.get_resistance_by_iv(voltage, current)

        case "CC_CV":
            voltage = float(input("Please enter voltage: "))
            charge = float(input("Please enter charge: "))
            capacitor.get_capacitance_by_cv(voltage, charge)

        case "IC_FI":
            frequency = float(input("Please enter frequency: "))
            inductance = float(input("Please enter inductance: "))
            inductor.get_inductive_reactance(frequency, inductance)

        case _:
            print("Invalid Input")

