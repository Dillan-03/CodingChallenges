def are_you_playing_banjo(name):
    name = list(name)
    if (name[0] == "R" or name[0] == 'r'):
        return "{} plays banjo".format(''.join(name))
    return "{} does not play banjo".format(''.join(name))

print(are_you_playing_banjo("Rob"))