def convert_temperature(temperature, to_unit):
    if to_unit == "F":
        return (temperature * 9/5) + 32
    elif to_unit == "C":
        return (temperature - 32) * 5/9

temperature = float(input("Enter the temperature: "))
unit = input("Enter the temperature unit (C/F): ")
to_unit = input("Convert to (C/F): ")

converted_temperature = convert_temperature(temperature, to_unit)
print("Temperature in", to_unit, ":", converted_temperature)
