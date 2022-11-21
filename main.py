import csv


def calculate_temperature(number): return float(number) * 0.45


def calculate_wind_speed(number): return float(number) * 0.05


def calculate_humidity(x): return float(x) * 0.5


def calculate_apples_yield(temperature, wind_speed, humidity):
    if temperature == '-' or wind_speed == '-' or humidity == '-':
        return '-'
    return calculate_temperature(temperature) + calculate_wind_speed(wind_speed) + calculate_humidity(humidity)


with open('Weather_Dataset_crop.csv', 'r') as source:
    reader = csv.DictReader(source)

    with open('result.csv', 'w', newline='') as result:
        with open('sum_yield.csv', 'w', newline='') as sum_yield:
            with open('max_yield.csv', 'w', newline='') as max_yield:
                result_writer = csv.writer(result)
                sum_yield_writer = csv.writer(sum_yield)
                max_yield_writer = csv.writer(max_yield)

                result_writer.writerow(['number', 'temperature', 'wind_speed', 'relative_humidity', 'yield_of_apples'])
                sum_yield_writer.writerow(['number', 'temperature', 'wind_speed',  'relative_humidity',
                                           'yield_of_apples', 'sum_yield'])
                max_yield_writer.writerow(['number', 'temperature', 'wind_speed',  'relative_humidity', 'rain_duration',
                                           'yield_of_apples', 'max_yield'])

                previous_sum_yield = 0.0
                max_yield = 0.0
                for row in reader:
                    apples_yield = calculate_apples_yield(row['avg_air_temp'], row['avg_wind_speed'],
                                                          row['relative_humidity'])

                    result_writer.writerow([row['number'], row['avg_air_temp'], row['avg_wind_speed'],
                                            row['relative_humidity'], apples_yield])

                    if apples_yield != '-' and apples_yield > 30:
                        sum_yield_writer.writerow([row['number'], row['avg_air_temp'], row['avg_wind_speed'],
                                                   row['relative_humidity'], apples_yield,
                                                   previous_sum_yield + apples_yield])
                        previous_sum_yield += apples_yield

                    if apples_yield != '-' and row['rain_duration'] != '-' and float(row['rain_duration']) > 0:
                        if apples_yield > max_yield:
                            max_yield = apples_yield
                        max_yield_writer.writerow([row['number'], row['avg_air_temp'], row['avg_wind_speed'],
                                                   row['relative_humidity'], row['rain_duration'], apples_yield,
                                                   max_yield])
