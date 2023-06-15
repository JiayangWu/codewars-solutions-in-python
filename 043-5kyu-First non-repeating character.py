def first_non_repeating_letter(s):
    from collections import defaultdict
    char2freq = defaultdict(int)
    
    for char in s:
        char2freq[char.lower()] += 1
    
    for char in s:
        if char2freq[char.lower()] == 1:
            return char
    return ""