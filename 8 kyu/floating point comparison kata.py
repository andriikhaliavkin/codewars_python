#floatin point comparison kata

def approx_equals(a, b):
    return abs(a-b) < 0.001


print(approx_equals(3.0, 2.5706))