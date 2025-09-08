print("I will find the circumference of any circle!")
def circumference(diameter):
    return diameter * 3.14
diameter = float(input("Diameter: "))
circ = circumference(diameter)
print(circ)