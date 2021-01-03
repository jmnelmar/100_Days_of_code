def add(*args):
    response = 0
    for arg in args:
        response += (int)(arg)
    return response

print(add(1,2,3,4,5,6,100))

def calculate(**kwargs):
    print(kwargs)

    for key,value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)