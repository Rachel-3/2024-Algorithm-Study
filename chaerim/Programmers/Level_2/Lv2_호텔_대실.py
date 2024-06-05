def solution(book_time):
    answer = 0

    for room_time in book_time:
        start_hour, start_minute = map(int, room_time[0].split(':'))
        room_time.append(start_hour * 60 + start_minute)
        end_hour, end_minute = map(int, room_time[1].split(':'))
        room_time.append(end_hour * 60 + end_minute + 10)

    book_time.sort(key=lambda x: x[2])

    end_rooms = []

    for room_time in book_time:
        start_time = room_time[2]
        end_time = room_time[3]

        room = False
        for i in range(len(end_rooms)):
            if end_rooms[i] <= start_time:
                end_rooms[i] = end_time
                room = True
                break
        
        if not room:
            end_rooms.append(end_time)

    answer = len(end_rooms)

    return answer