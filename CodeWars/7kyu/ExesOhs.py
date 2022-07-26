def xo(s):
    s = list(s.lower())
    return (s.count("x") == s.count("o"))


print(xo("xxooxo"))
