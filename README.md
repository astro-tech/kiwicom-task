# Solution candidate for Kiwi.com Python weekend entry task

### Description
This Python package is able to generate a JSON compatible structured list from a csv file supplied in examples and a 
few command line arguments. The paradigm involves modular programming, which I found faster in this case than OOP.

Pipeline:
- Parse command line arguments as inputs and validate them.
- Load and parse CSV file into memory while validating its contents.
- Create a  namedtuple Graph object from the database (Graph vertices=airports, Graph edges=routes).
- The `origin` and `destination` arguments are validated at this stage.
- Adjacency lists are generated from the Graph object. Outbound always, inbound only in case of return trip.
- Graph traversal is conducted by a depth-first search (DFS) algorithm. The `transfer` filter is applied here.
- If `return` trip is requested the inbound and outbound solutions are merged with all possible combinations.
- Based on all the combinations within each trip the possible flights are assigned to them with `bags` filter.
- Another combination search is commenced to discover all possibilities but only those are registered which satisfies the layover rule.
- The output is reordered by the total ticket + bag price.
- Finally, the output is converted to JSON compatible format if not otherwise requested by the `raw` argument.

During the process the user can diplay the currently discovered routing with the `progress` argument.

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

Optional arguments can be given in random order.

Written by: Csaba Bai