import pandas as pd
def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    df = pd.DataFrame(data, columns = ['code', 'date', 'maximum', 'remain'])
    df = (df[df[ext] <= val_ext])
    df = df.sort_values(by=[sort_by], ascending = True)
    answer = df.values.tolist()
    return answer