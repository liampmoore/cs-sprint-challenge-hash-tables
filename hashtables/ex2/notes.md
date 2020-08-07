Understand:

- Our tickets are made into classes with a source string and a destination string
- Our first flight has a source of NONE
- Our last flight has a destination of NONE
- We want to output an ordered list of strings


Plan:
- Two loops
- A for loop through the list of flight/ticket objects to build our hash table. key: source, value: destination
- A while loop through the hash table to build our list of strings

Step 1:
Create a table

Step 2:
Loop through the list of flight objects.
Add the source as a key and the destination as a value.
If an object has a NONE start make it's key START.
If an object has a NONE destination make it's value END.

Step 3:
Create a list the length of the hash table - 1.
Create a current pointer set to the START entry.
Create an index counter.
Start a while loop.
While the destination is not END, add the destination to the current index of the list, then increment index and set current to the destination.

Step 4:
Return the list.