def sum_of_numbers_with_last_digit(start, end, digit):
    total = 0
    for i in range(start, end+1):
        if i % 10 == digit:
            total += i
    return total

start_of_range = 1384
end_of_range = 4069
digit = 9
result = sum_of_numbers_with_last_digit(start_of_range, end_of_range, digit)
print(result)

