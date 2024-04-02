def solution(want, number, discount):
    answer = 0
    
    want_dict = {item: cnt for item, cnt in zip(want, number)}
    
    for day in range(len(discount) - 9):
        discounted_items = {}
        for i in range(day, day + 10):
            if discount[i] in discounted_items:
                discounted_items[discount[i]] += 1
            else:
                discounted_items[discount[i]] = 1
        print(want_dict, discounted_items)
        if want_dict == discounted_items:
            answer += 1

    return answer

want1 = ["banana", "apple", "rice", "pork", "pot"]
number1 = [3, 2, 2, 2, 1]
discount1 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want1, number1, discount1))
want2 = ["apple"]
number2 = [10]
discount2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
print(solution(want2, number2, discount2))