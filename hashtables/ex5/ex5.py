# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Build up a table of files from the paths
    table = {}
    for pathindex, fullpath in enumerate(files):
        filename = ''
        current = -1
        while fullpath[current] != "/":
            filename = fullpath[current] + filename
            current -= 1
        if filename in table:
            table[filename].append(pathindex)
        else:
            table[filename] = [pathindex]

    # Loop through queries
    result = []
    for query in queries:
        if query in table:
            for pathindex in table[query]:
                result.append(files[pathindex])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
