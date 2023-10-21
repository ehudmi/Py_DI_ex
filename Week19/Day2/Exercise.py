def highest_even(li):
    sorted_li = sorted(li, reverse=True)
    for item in sorted_li:
        if item % 2 == 0:
            return item
        else:
            continue


print(highest_even([10, 2, 3, 4, 8, 11]))
