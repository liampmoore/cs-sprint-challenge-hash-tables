Understand:

- We assume we don't need to handle dupkicates
- We are give na max weight
- We need a tuple of the indices of two items that equal the given max weight

Plan:

Step 1:
Create a table

Step 2:
Loop through items, add the item to the table weight as key index as value. Check if the table already has max minus weight and if so return those two values.

Step 3:
If we arrive at the end of the loop return None