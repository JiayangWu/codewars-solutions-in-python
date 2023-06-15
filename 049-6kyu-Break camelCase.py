def solution(s):
    last_upper_index = 0
    res = []
    for i, char in enumerate(s):
        if char.isupper():
            res.append(s[last_upper_index:i])
            last_upper_index = i
    res.append(s[last_upper_index:])
    return " ".join(res)