def DFS(current, depth, word_dict) :
    alphabet = ['A', 'E', 'I', 'O', 'U']
    if depth <= 5 :
        word_dict.append(current)
        for i in range(len(alphabet)) :
            DFS(current + alphabet[i], depth + 1, word_dict);
        
def solution(word):
    word_dict = []
    DFS('', 0, word_dict);
    return (word_dict.index(word))