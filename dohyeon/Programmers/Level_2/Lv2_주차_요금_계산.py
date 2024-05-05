from datetime import datetime
import math
def calculate_parking_time(logs):
    total_parking_time = 0
    in_time = None
    in_count, out_count = 0, 0
    for log in logs:
        log_time = datetime.strptime(log[0], '%H:%M')
        if log[1] == 'IN':
            in_time = log_time
            in_count += 1
        elif log[1] == 'OUT' and in_time is not None:
            out_time = log_time
            parking_time = out_time - in_time
            total_parking_time += parking_time.total_seconds() / 60
            in_time = None
            out_count += 1
    if in_count > out_count :
        final_time = datetime.strptime("23:59", "%H:%M")
        last_fee = ((final_time - in_time).total_seconds() / 60)
        total_parking_time += int(last_fee)
    
    return total_parking_time

def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    
    cars = {}
    total_times_cars = {}
    car_fees = {}
    for i in records :
        time, car_number, park_type = i.split(" ")
        if str(car_number) in cars :
            cars[str(car_number)].append([time, park_type])
        else :
            cars[str(car_number)] = []
            cars[str(car_number)].append([time, park_type])
    for key, value in cars.items() :
        total_times = calculate_parking_time(value)
        if total_times <= basic_time :
            car_fees[key] = basic_fee
        elif total_times > basic_time :
            car_fee = basic_fee + math.ceil((total_times - basic_time) / per_time) * per_fee
            car_fees[key] = car_fee
    answer = [car_fees[key] for key in sorted(car_fees.keys())]
    return answer