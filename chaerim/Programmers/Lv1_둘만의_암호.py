def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97, 123)]
    exclude_alphabet = [letter for letter in alphabet if letter not in skip]

    for letter in s:
        alphabet_index = exclude_alphabet.index(letter)
        move_index = (alphabet_index + index) % len(exclude_alphabet)
        answer += exclude_alphabet[move_index]

    return answer