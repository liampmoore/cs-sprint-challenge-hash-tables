def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    items = []

    for i, weight in enumerate(weights):
        if limit - weight in table:
            items = [[weight, i], [limit - weight, table[limit - weight]]]
            items = sorted(items, key=lambda x: x[1], reverse=True)
            items = [item[1] for item in items]
            items = tuple(items)
            return items
        table[weight] = i
    return None


