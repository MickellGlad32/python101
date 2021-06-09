from typing import ValuesView


try:
    C = int(input('Temperature in C?'))
    F = (C * 9/5) + 32

    print(str(F) + " F")
except ValueError:
    print('thats not a number. ')
