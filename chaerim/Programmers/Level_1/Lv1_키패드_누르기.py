def solution(numbers, hand):
    answer = ''

    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_hand = keypad['*']
    right_hand = keypad['#']

    for number in numbers:
        target = keypad[number]
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = target
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = target
        else:
            left_distance = abs(left_hand[0] - target[0]) + abs(left_hand[1] - target[1])
            right_distance = abs(right_hand[0] - target[0]) + abs(right_hand[1] - target[1])

            if left_distance < right_distance:
                answer += 'L'
                left_hand = target
            elif right_distance < left_distance:
                answer += 'R'
                right_hand = target
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = target
                else:
                    answer += 'R'
                    right_hand = target

    return answer