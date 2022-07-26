def xo(s):
    s = list(s)
    return (s.count("x") == s.count("o"))


print(xo("xxooxo"))