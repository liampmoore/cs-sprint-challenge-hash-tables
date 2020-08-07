def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    result_table = {}
    for num in a:
        if (num * -1) in table:
            result_table[abs(num)] = abs(num)
        table[num] = True

    result = list(result_table.values())
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
