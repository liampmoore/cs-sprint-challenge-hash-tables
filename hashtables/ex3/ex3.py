def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    tables = [None] * len(arrays)

    for index, array in enumerate(arrays):
        tables[index] = {}
        if index == 0:
            for number in array:
                tables[index][number] = number
        else:
            for number in array:
                if number in tables[index - 1]:
                    tables[index][number] = number

    result = list(tables[-1].values())
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))