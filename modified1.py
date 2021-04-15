def sum_all(str_i):
    sum_n = 0
    n = 0
    for c in str_i:
        if c == '\n' or c == ',':
            sum_n += n
            n = 0
        else:
            n = n*10 + ord(c) - ord('0')
    sum_n += n
    return sum_n

def groceries(dict_i, k, v):
    if dict_i.has_key(k):
        k = 0
    dict_i[k] = v
    return dict_i

if __name__ == "__main__":
    string1 = "4,7,2"
    string2 = "\n\n12,11,10,2,100\n\n\n"

    print(sum_all(string1))
    print(sum_all(string2))

    dictionary1 = {192: 'apples', 453: 'bananas', 12: 'tomatoes'}
    new_ID1 = 249
    new_name1 = 'oranges'
    print(groceries(dictionary1, new_ID1, new_name1))

    dictionary2 = {17: 'cookies', 124: 'chips'}
    new_ID2 = 124
    new_name2 = 'bread'
    print(groceries(dictionary2, new_ID2, new_name2))
