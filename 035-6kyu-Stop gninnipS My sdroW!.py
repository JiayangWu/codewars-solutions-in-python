def spin_words(sentence):
    # Your code goes here
    if len(sentence) == 0:
        return None
    words = sentence.split(" ")
    for wordindex,word in enumerate(words):
        if len(word)>=5:
            words[wordindex] = reverse(word)
#     print words
    return " ".join(word for word in words)
          
    
def reverse(word):
    rev=word[::-1]
    return rev
