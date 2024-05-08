def solution(fees, records):
    answer = []

    car_time = {}
    in_car_time = {}

    for record in records:
        time, car_num, status = record.split()
        time = int(time[:2]) * 60 + int(time[3:])

        if status == "IN":
            in_car_time[car_num] = time
        elif status == "OUT":
            in_time = in_car_time.pop(car_num)
            total_parking_time = time - in_time
            if car_num in car_time:
                car_time[car_num] += total_parking_time
            else:
                car_time[car_num] = total_parking_time

    end_of_day = 23 * 60 + 59
    for car_num, in_time in in_car_time.items():
        total_parking_time = end_of_day - in_time
        if car_num in car_time:
            car_time[car_num] += total_parking_time
        else:
            car_time[car_num] = total_parking_time

    car_time_sorted = sorted(car_time.keys())

    basic_time, basic_rate, unit_time, unit_rate = fees
    for car_num in car_time_sorted:
        total_time = car_time[car_num]
        if total_time <= basic_time:
            answer.append(basic_rate)
        else:
            overtime = total_time - basic_time
            over_unit = (overtime + unit_time - 1) // unit_time
            price = basic_rate + over_unit * unit_rate
            answer.append(price)

    return answer