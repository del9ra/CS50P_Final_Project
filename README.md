# SUMMER VACATION

#### Video Demo:  <https://www.youtube.com/watch?v=z-zCxcnqSPw>
#### Description:
This program allows users to plan a budget for summer vacations.

All in all, it consists of 9 functions including the ‘main’ function. 3 libraries are installed to accomplish this project: tabulate, pyttsx3,  and inflect. 3 functions are implemented to test the code with the pytest framework.

The program calculates the sum you need to purchase tickets, to pay for lodging and tourist attractions.

The `main()` function starts with the `choose_country()` function, which is stored in the _country_ variable. _country_ as a parameter is passed to the following three functions, each of which is stored in three variables: `choose_tickets(country)` in _tickets_price_,
`choose_accommodation(country)` in _accommodation_price_, `choose_attractions(country)` in _attractions_price_. After being called, prices from each function are summed up and text with the total budget for summer vacations is printed. The total sum is passed to the inflect library, which converts numbers into words so that it could be easier to read correctly the text for a female voice in the pyttsx3 library.

***

#### Functions
+ `choose_country()` function prompts a user to pick a country with a key from the dictionary. A Try Except statement in a while loop is used to catch a Key Error, if users enter a wrong key.
+ `get_table()` function displays data extracted from CSV files in tables with the tabulate library. List comprehension was applied here.
+ `choose_tickets()` function generates the name of the CSV file with the ‘chosen_country’ variable and ‘_tickets.csv’. In the while loop the user is prompted to choose a flight and checks whether the chosen key is in the file. If it is not, it notifies users of invalid input and reprompts them. The function calls `get_table()`, which prints the CSV file in a table.
+ If the key does exist, the program calls the `tickets_csv()` function, which reads the file with csv.DictReader. It searches for a field with the ticket price, converts it into an integer, and returns to the `choose_tickets()`, which returns this to the `main()`.
+ `choose_accommodation()` function prompts users to choose accommodation. It opens a table with accommodation options by calling the `get_table()`. If the chosen key is in the list of represented numbers, the `accommodation_csv` function is called. Else the program reprompts the user to try again. The structure of this function is pretty similar to the previous one.
+ `accommodation_csv()` function searches for an accommodation price in a row with the csv.reader, where the key, chosen before that, matches the key of the lodging choice. At last, it returns int(row) to the latter function, which itself returns it to the main.
+ in  the `choose_attractions()` function the _attractions_sum_ variable is declared. It counts the sum of all the chosen attractions prices. It comprises two while loops. The user is prompted to choose between tourist attractions with paid and free entrance. A CSV file name is made up here: country+’free’/‘paid’+’.csv’. If there is no such file, the program catches File Not Found error due to the try-except statement. Then it opens the file in the `get_table()`, and the user picks a key for a place to visit. If the key is not an integer, the except block informs the user of the  Value Error and reprompts them.
+ Otherwise, it calls the `attractions_csv()` function and stores this call as a value in the _my_sum_ variable. This function searches for an attraction price in a CSV file and returns it in a float to the latter function, which prints the total cost of attractions and prompts to type a letter to continue and choose the next attraction, or to return to the previous options, where you choose between ‘free’ or ‘paid’, or to quit. As long as we go through every phase of these two attractions functions, we store the price of each attraction in the _attractions_sum_ by adding a numerical value from _my_sum_ to it. After the user picks ‘quit’, the function returns _attractions_sum_ to the main function.

***

#### Files
- **project.py** contains the program
- **test_project.py** contains test functions for ‘project.py’
- **requirements.txt** contains pip-installable libraries
- **italy_accommodation.csv**, **turkey_accommodation.csv**, and **thailand_accommodation.csv** contain data(names, prices, and keys) in CSV format about accommodations in Italy, Turkey, and Thailand respectively.
- **italy_tickets.csv**, **turkey_tickets.csv** and **thailand_tickets.csv** contain CSV data about flights(airline companies, flight length, prices and keys) to/from Italy, Turkey and Thailand respectively.
- **italy_free.csv**, **italy_paid.csv**, **turkey_free.csv**, **turkey_paid.csv**  and **thailand_free.csv** and **thailand_paid.csv** contain CSV data about tourist attractions you can visit for free, and those for which you have to pay in Italy, Turkey, and Thailand respectively.
