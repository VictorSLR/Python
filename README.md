The scrip compares two .csv files and generate a .txt file with the required information: department and position changes, missing employees and new ones.

It is required for the .csv files to be properly named, so the script can read them.
The Employees System Data file must be named as "employees_data", and the Web Auth Data file must be named as "web_data". 
You can also edit the code and change the filenames there if it's necessary. If the filenames matches, just run the script and it will generate the report.

About the algorithm, it uses nested loops to compare each line and necessary elements in the files and find the differences between them and missing data. 
I take in consideration that the data might not be ordered. I made a few tests and it worked as i expected. I tested on Windows and placed the csv files in
the python's directory, otherwise the path to the files should be added in the code.

