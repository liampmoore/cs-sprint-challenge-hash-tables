UNderstand:

We are given a list of paths.

We are given a list of filenames.

We need to return a list of all paths that contain that filename.

Plan:

We can iterate through each full path and get the filename and save it to a hash table with the filename as a key and index in the list of full paths as a value.

We can then iterate through the files to check for and see if they are keys in our table, and if so use the given index to save the full paths to another hash table.

We can then use .values on that hash table to make a list.


Step 1:
Create a hash table.

Step 2:
Start a for loop through all paths.

Step 3:
While loop backwards through the path until we hit a \ mark, saving the filename to a current_file
Then save the filename and index of the full path to the table.

Step 4:
For loop through the files we are trying to find. If file in table, add fullpath to result_table[]

Step 5:
Save results as list(result_table.values())