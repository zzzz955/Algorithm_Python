def reverse_word(string):
    print('단어 뒤집기')
    if not isinstance(string, str):
        print('문자열을 입력해 주세요')
        return
    temp = string.split(' ')
    reversed_list = []
    for i in temp:
        new_list = "".join(list(reversed(i)))
        reversed_list.append(new_list)
    reversed_str = " ".join(reversed_list)
    return reversed_str

