from math import sqrt

def nearest_square(n):
    try:
        ans = int(sqrt(n))**2
        return ans
    except ValueError:
        return 0