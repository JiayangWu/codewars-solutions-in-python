def high(words):
    # Code here
    max_word, max_score = "", 0
    for word in words.split():
        score = getScore(word) 
        if score > max_score:
            max_score = score
            max_word = word
    return max_word
        

def getScore(word):
    score = 0
    for char in word:
        score += ord(char) - ord("a") + 1
    return score