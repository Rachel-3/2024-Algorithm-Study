def sort_by_price(data):
    sorted_data = {}
    for genre, items in data.items():
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        sorted_data[genre] = [item[0] for item in sorted_items]
    return sorted_data

def solution(genres, plays):
    answer = []
    
    genres_original_code = {}
    genres_total_count = {}
    for i in range(len(genres)) :
        if genres[i] in genres_total_count :
            genres_total_count[genres[i]] += plays[i]
            genres_original_code[genres[i]].append([i, plays[i]])
        else :
            genres_total_count[genres[i]] = plays[i]
            genres_original_code[genres[i]] = [[i, plays[i]]]
    
    genres_orders = sorted(genres_total_count, key = genres_total_count.get, reverse = True)
    genres_original_code = (sort_by_price(genres_original_code))
    
    count = 0
    genre_number = 0
    for i in range(len(genres_original_code) * 2) :
        if count == 2 :
            genre_number += 1
            count = 0
        try :
            genre = genres_orders[genre_number]
            answer.append(genres_original_code[genre][count])
        except :
            pass
        count += 1
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))