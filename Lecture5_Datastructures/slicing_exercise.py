sensor = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]

half_index = (len(sensor) // 2) + 1

subsampled_sensor_slice = sensor[:half_index:2]
print(subsampled_sensor_slice)