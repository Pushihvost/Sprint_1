string_of_time = '1h 45m,360s,25m,30m 120s,2h 60s'

def count_minuts(string_time):

    hours = 0
    minuts = 0
    secunds = 0

    string_split = string_time.split(',')

    for t in string_split:
        time = t.split(' ')

        for piece_of_time in time:
            if 'h' in piece_of_time:
                h = piece_of_time.replace('h','')
                hours += int(h)
            elif 'm' in piece_of_time:
                m = piece_of_time.replace('m','')
                minuts += int(m)
            elif 's' in piece_of_time:
                s = piece_of_time.replace('s','')
                secunds += int(s)

    total_time = hours*60 + minuts + secunds//60

    print(f'Total time in minuts = {total_time}')

count_minuts(string_of_time)
