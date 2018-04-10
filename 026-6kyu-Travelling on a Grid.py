def travel_chessboard(s):
    s=s.replace(')(',',')
    s=s.replace(' ',',')
    s=s.replace(')','')
    s=s.replace('(','')
    string = s.split(',')
    x1 = s[0]
    y1 = s[2]
    x2 = s[4]
    y2 = s[6]
    a = [[0] * 8 for i in range(8)]
    for i in range(8):
      for j in range(8):
          if i == 0:
            a[i][j] = 1
          elif j == 0:
            a[i][j] = 1
          else:
             a[i][j] = a[i-1][j] + a[i][j-1]
    print a
    return a[int(x2)-int(x1)][int(y2)-int(y1)]
