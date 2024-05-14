def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return answer

'''통과 코드! 
But Python에는 문자열 메서드로 'startswith'가 존재함 -> 특정 문자열이 접두사(prefix)로 시작하는지 확인하는 데 사용함.

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        number = phone_book[i]
        next_number = phone_book[i + 1]

        if number == next_number[:len(number)]:
            return False

    return answer
'''

''' 시간 초과
def solution(phone_book):
    answer = True

    for i, book_1 in enumerate(phone_book):
        for j, book_2 in enumerate(phone_book):
            if i != j and book_1 in book_2:
                book_len = len(book_1)
                if book_1 == book_2[:book_len]:
                    answer = False
                    break

    return answer
    '''