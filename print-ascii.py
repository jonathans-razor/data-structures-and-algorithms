def printAscii():
    print('hi')
    i = 0
    while i < 255:
      i += 1
      print(i, " ", chr(i))
    return

printAscii()