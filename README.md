# Candidate solution for Kiwi.com Python weekend entry task

### Description
This Python package is written as a candidate solution to Kiwi.com entry task. 

Link to original task page: https://github.com/kiwicom/python-weekend-entry-task

The package is able to generate a JSON compatible structured list from a CSV file supplied in examples and a 
few command line arguments. The paradigm involves modular programming, which I found faster in this case than OOP.

Pipeline:
- Parse command line arguments as inputs and validate them.
- Parse and load CSV file into memory while validating its contents. Each line of flight gets a unique ID number for later use*.
- Create a  namedtuple Graph object from the database (Graph vertices=airports, Graph edges=routes).
- The `origin` and `destination` arguments are validated at this stage.
- Adjacency lists are generated from the Graph object. Outbound always, inbound only in case of `return` trip.
- Graph traversal is conducted by a depth-first search (DFS) algorithm. The `max_transfer` filter is applied here. The result is a list of all valid airport-pair combinations.
- Another graph is created within each combination of flights. *Here the flights themselves are substituted with their ID's (The dictionaries are non-hashable). This graph is represented with an adjacency list taking into consideration the transfer rules and `requested_bags` filter.
- This 'journey' graph is also traversed by a DFS algorithm to build the list of valid flights (IDs) within each combination.
- If `return_requested` the above journey graph traversal is conducted for the return flights combinations as well. The inbound and outbound solutions are merged with the layover rule.
- The ID numbers are replaced with the actual flights data.
- The ID numbers are cleared from the output.
- The output is reordered by the total ticket + bag price.
- Finally, the output is converted to JSON compatible format if not otherwise requested by the `raw_format_requested` argument.

During the process the user can diplay the currently discovered routing with the `print_progress` argument.
To measure performance the `timing_requested` argument can be used.

The following table describes how to use the arguments:

| Argument name         | type     | Description              | Notes                        | Example               |
|-----------------------|----------|--------------------------|------------------------------|-----------------------|
| `input_file`          | string   | CSV file location        | Mandatory                    | example/example0.csv  |
| `origin`              | string   | Origin airport code      | Mandatory                    | WIW                   |
| `destination`         | string   | Destination airport code | Mandatory                    | RFZ                   |
| `requested_bags`      | integer  | Number of requested bags | Optional (defaults to 0)     | --bags=1              |
| `max_transfer`        | int/none | Max number of transfers  | Optional (defaults to None)  | --transfer=1          |
| `return_requested`    | boolean  | Is it a return flight?   | Optional (defaults to False) | --return              |
| `print_progress`      | boolean  | Display progress bar?    | Optional (defaults to False) | --progress            |
| `raw_format_requested`| boolean  | Get output as dictionary?| Optional (defaults to False) | --raw                 |
| `timing_requested`    | boolean  | To measure performance   | Optional (defaults to False) | --timer               |

To display the argparse package's built-in command line interface help screen use: -h or --help.
Optional arguments can be given in random order.

**The main file is solution.py.**
### Example usage:
####python -m solution example/example3.csv ZRW BPZ --bags=2 --transfer=4 --return --progress --raw --timer

### Additional notes

In case of return trip search the layover rule is changed to the following: the departing flight from the destination can only be 1 hour after the inbound flight's arrival time.
The total trip time in this case doesn't include the layover time.

As the number of transfers are increasing (with increasing the `max_transfer` limit) the possibilities are also increasing exponentially.
This means that the program starts to lag, due to the number of iterations it has to carry out.
The following table shows measured performance results:

Input used: python -m solution example/example3.csv ZRW BPZ --timer

|`max_transfer`|`timing_requested`|Number of possibilities|
|--------------|------------------|-----------------------|
|0             |0.06 sec          |1                      |
|1             |0.1 sec           |6                      |
|2             |0.4 sec           |31                     |
|3             |2.2 sec           |131                    |
|4             |9.7 sec           |431                    |
|5             |27.1 sec          |1031                   |
|6             |49.2 sec          |1631                   |

In case of `return_requested` the above times roughly increase twofold.
For large CSV tables and/or high `max_transfer` numbers the use of `print_progress` is recommended.

Written by: Csaba Bai