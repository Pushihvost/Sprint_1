def count_digital_root(num):
    list_of_ranks = []
    sum = 0

    while num>9:
        last_number = num % 10
        num = num // 10
        list_of_ranks.append(last_number)
        if num < 10:
            list_of_ranks.append(num)

    for idx in range(len(list_of_ranks)):
        sum += list_of_ranks[idx]
        
    if sum > 9:
        return count_digital_root(sum)
    else:
        return sum


print(count_digital_root(4851))
print(count_digital_root(97569))
print(count_digital_root(889987))

