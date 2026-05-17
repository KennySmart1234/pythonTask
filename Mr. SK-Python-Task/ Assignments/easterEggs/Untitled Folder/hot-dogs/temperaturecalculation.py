



water_kilogram = int(input(print("Enter amount of water in kilogram: ")))

initial_temperature = int(input(print("Enter initial Temperatures: ")))

final_temperature = int(input(print("Enter final Temperatures: ")))

final_initial_temperature = final_temperature - initial_temperature
energy_needed = water_kilogram * final_initial_temperature * 4186

print("energyNeeded: ", energy_needed, "\n");

        

