def add(*args):
    response = 0
    for arg in args:
        response += (int)(arg)
    return response

print(add(1,2,3,4,5,6,100))