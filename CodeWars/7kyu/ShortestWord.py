def find_short(s):

    s = list(s.split(' '))
    l = len(s[0])
    for i in s:
        if (len(i) < l):
            l = len(i)
  
    return l # l: shortest word length

print(find_short("bitcoin take over the world maybe who knows perhaps"))
