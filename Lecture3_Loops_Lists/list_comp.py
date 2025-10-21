fruits = ["apple", "banana", "cherry"]

only_a_fruits = [fruit for fruit in fruits if "a" in fruit]

raw_sensor_readings = [1.23, -9.45, 10.22, 3.78, -5.92, 1.16]

cleaned_data = [reading for reading in raw_sensor_readings if reading > 0]

cleaned_data_2 = [abs(reading) for reading in raw_sensor_readings]

print(cleaned_data)
print(cleaned_data_2)