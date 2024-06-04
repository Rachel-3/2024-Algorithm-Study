def solution(plans):
    answer = []

    for plan in plans:
        hour, minute = map(int, plan[1].split(':'))
        plan.append(hour * 60 + minute)

    plans.sort(key=lambda x: x[3])

    stack = []
    current_time = 0
    for name, _, study_time, start_time in plans:
        study_time = int(study_time)
        
        while stack and current_time <= start_time:
            prev_name, prev_study_time, prev_start_time = stack.pop()
            end_time = current_time + prev_study_time

            if end_time <= start_time:
                answer.append(prev_name)
                current_time = end_time
            else:
                stack.append((prev_name, end_time - start_time, prev_start_time))
                current_time = start_time
                break

        stack.append((name, study_time, start_time))
        current_time = start_time

    while stack:
        name, _, _ = stack.pop()
        answer.append(name)
    
    return answer