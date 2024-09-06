def sort_array_by_parity(nums):
    output = []
    for num in nums:
        if num % 2 == 0:
            output.append(num)
    for num in nums:
        if num % 2 != 0:
            output.append(num)
    return output
