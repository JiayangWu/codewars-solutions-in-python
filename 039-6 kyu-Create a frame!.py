def frame(text, char):
    max_l = 0
    for item in text:
        if len(item) > max_l:
            max_l = len(item)
            
    frame_l = max_l + 4
    frame = char * frame_l + "\n"

    temp_frame = ""
    for i in range(len(text)):
        temp_frame = char + " " + text[i] + " " * (max_l - len(text[i])) + " " + char + "\n"
        frame = frame + temp_frame
        
    frame += char * frame_l
    return frame
