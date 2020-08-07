#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # Build up a table of sources to destinations
    table = {}
    for ticket in tickets:
        if ticket.source == "NONE":
            table["START"] = ticket.destination
        elif ticket.destination == "NONE":
            table[ticket.source] = "END"
        else:
            table[ticket.source] = ticket.destination

    # Create a list with a length equaling all destinations
    route = [None] * (length)
    
    # Create pointers for our while loop
    current = "START"
    destination = table[current]
    index = 0

    while destination in table:
        route[index] = destination
        index += 1
        current = destination
        destination = table[current]
    route[index] = "NONE"
    return route
