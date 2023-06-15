def generate_hashtag(s):
    #your code here
    if not s:
        return False
    res = "#" + "".join([word.capitalize() for word in s.split()])
    return res if len(res) < 140 else False