def solution(data, ext, val_ext, sort_by):
    answer = []
    
    data_name = ['code', 'date', 'maximum', 'remain']
    ext_index = data_name.index(ext)
    
    answer = [i for i in data if i[ext_index] < val_ext]

    sort_index = data_name.index(sort_by)
    answer.sort(key=lambda x: x[sort_index])

    return answer