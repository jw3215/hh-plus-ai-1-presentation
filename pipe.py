from pipe_helper import pipe_decorator

@pipe_decorator
def inc(x):
    return x + 1

@pipe_decorator
def square(x):
    return x**2


print((1 | inc | square))  # 4