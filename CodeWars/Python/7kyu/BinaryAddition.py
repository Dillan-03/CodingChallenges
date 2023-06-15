from audioop import add


def add_binary(a,b):
    return format(a+b, "b")

print(add_binary(51,12))