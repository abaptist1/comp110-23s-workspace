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
