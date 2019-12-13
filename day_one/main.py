from math import floor


def main():
    input_file = open("input.txt", 'r', encoding="utf-8")

    module_masses = []

    for line in input_file:
        module_masses.append(line.rstrip())

    fuel_required = 0

    for mass in module_masses:
        fuel_required += calc_fuel_required(int(mass))


    print(fuel_required)


def calc_fuel_required(fuel_mass):
    potential_requirement = (floor(fuel_mass / 3) - 2)
    if potential_requirement <= 0:
        return 0
    else:
        return potential_requirement + calc_fuel_required(potential_requirement)

if __name__ == "__main__":
    main()
