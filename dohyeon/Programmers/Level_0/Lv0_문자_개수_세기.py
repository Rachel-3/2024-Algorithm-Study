def solution(my_string):
    alphabet_dict = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = 0
        
    for i in my_string :
        alphabet_dict[i] += 1
    return list(alphabet_dict.values())
