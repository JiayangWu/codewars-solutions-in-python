def is_valid_walk(walk):
    #determine if walk is valid
    i, j = 0, 0
    if len(walk) != 10:
        return False
    
    for w in walk:
        if w == "n":
            j += 1
        elif w == "s":
            j -= 1
        elif w == "w":
            i -= 1
        else:
            i += 1
    return i == 0 and j == 0