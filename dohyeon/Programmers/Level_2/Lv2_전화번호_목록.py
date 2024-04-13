# def solution(phone_book):
#     answer = True
#     phone_book = list(map(int, phone_book))
#     phone_book.sort()
#     phone_book = list(map(str, phone_book))
#     temp = phone_book[0]
#     for i in range(1, len(phone_book)) :
#         if (phone_book[i].find(temp)) == 0 :
#             return False
#     return answer

def solution(phone_book) :
    phone_book.sort()
    for i in range(1, len(phone_book)) :
        if phone_book[i - 1] == phone_book[i][:len(phone_book[i - 1])] :
            return False
    return True