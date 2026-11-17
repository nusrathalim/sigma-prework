def high_and_low(numbers):
    lowest = numbers[0]
    highest = numbers[0]
    # Loops through every number in list to check if it is lower than lowest or higher than highest and updates if so
    for num in numbers:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num

    return [lowest, highest]


# Example lists
print(high_and_low([2, 4, 1, 0, 2, -1]))
print(high_and_low([20, 50, 12, 6, 14, 8]))
