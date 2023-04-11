from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV File and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    # Open File
    file_handle = open(filename, "r", encoding="utf8") # The "r" means read the file, encoding="utf8" tells python how to read the csv file and read and format the data, always include it at the end
    csv_reader = DictReader(file_handle)
    for row in csv_reader: #Each row is a dict of the data
       result.append(row) 
    file_handle.close() # Closes the file
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns Values in a a table under a certain header."""
    result: list[str] = []
    # Step through table
    for row in table:
        # Save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # Loop through keys of oen row of table
    first_row: dict[str, str] = table[0]
    for key in first_row: #Loops through each key in the dict
        # For each key, make a dict entry with all column values
        result[key] = column_vals(table, key)
    return result

def column_values(table: list[dict[str, str]], column: str ) -> list[str]:
    """Generate a list of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column based table, with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {} # Establish empty dict for result
    for column in table: #Loop through each of the columns in the first row of the fable
        n_value: list[str] = [] #establish empty list to store each of the first N values in column
        n = 0
        while n < rows:
            if n < len(table[column]):
                n_value.append(table[column][n])
            n += 1
        result[column] = n_value
    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {} # Establish empty dict to serve as return of function
    for column in column_names: # Loop through each of the columns in olumn_names
        #Assign to the column key of the result dict the list of values stored in the input dict at that column
        result[column] = table[column]
    return result # Return produced dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column based table with two column based- tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            for value in table_2[column]:
                result[column].append(value)
        else:
            result[column] = table_2[column]
    return result