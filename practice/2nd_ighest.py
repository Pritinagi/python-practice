# Find 2nd highest number in a list
number=[321,324,534,21,4231,432,431,352]
highest=second_highest=float("-inf")
        #both values are defined as -inf that means a value smaller than every possible number.
        # Why use it?
        # Because initially:
        # we don’t know the highest number
        # we don’t know the second highest number
        # So we start with the smallest possible value.
for num in number:
    if num>highest:
        second_highest=highest
        highest=num


    elif num > second_highest and num != highest:
                    # num != highest - This prevents duplicate highest numbers from becoming second highest
        second_highest=num
print(second_highest)