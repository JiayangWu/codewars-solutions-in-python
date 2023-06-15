def in_array(array1, array2):
    # your code
    s = set(array2)
    res = []
    for word in array1:
        for w in array2:
            if word in w and word not in res:
                res.append(word)
                break
    return sorted(res)