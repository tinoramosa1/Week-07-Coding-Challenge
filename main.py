def swap_pairs(num):
    new_num = 0
    i = 0
    while num > 9:
        # taking the last two digits
        two_digits = num % 100
        # extracting the left and right
        left = two_digits // 10
        right = two_digits % 10
        # swapping the left and right
        temp = left
        left = right
        right = temp
        # merging and appending to the new_num
        two_digits = left * 10 + right
        new_num = two_digits * (100 ** i) + new_num
        i = i + 1
        # reducing the num by two digits right
        num = num // 100
    # return the new_num
    return num * (100 ** i) + new_num


# calling code
print(swap_pairs(482596))
print(swap_pairs(1234567))
