def past(h, m, s):
    '''
    1 second = 1000 millisecond
    1 minute = 60000 milliseconds
    1 hour = 60 * 60000
    '''

    return (h*60*60000)+(m*60000)+(s*1000)

print((past(0,1,1)))