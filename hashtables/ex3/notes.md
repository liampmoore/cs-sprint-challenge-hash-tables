Understand:

A list of lists.

We need to return a list of the numbers that occur on all lists.

Therefore we have the length of the list of lists, which tells us the number of times a number should be occuring.


Plan:

Create a list of tables which is the same length of the list of lists.

For the first list add all numbers.

For all subsequent lists of numbers, only add the number to the corresponding table if the number exists in the previous corresponding table.


Step 1:
Create a list the length of the list of lists.

Step 2:
Start a for loop for the list of lists.

If index = 0 on the list of lists, add every number to the hash table.

Else:
    if the number exists on the previous index hash table, add it to the current index hash table

Step 3:
Make a list from the final hash table in the list of hash tables.