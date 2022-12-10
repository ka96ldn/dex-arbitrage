import os
import json

def read_json(filepath):
    """Read and parse a JSON file.
    
    Args:
        filepath (str): The path to the JSON file.
        
    Returns:
        dict: The parsed JSON data.
    """
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json(data, filepath):
    """Write data to a JSON file.
    
    Args:
        data (dict): The data to be written to the file.
        filepath (str): The path to the JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(data, f)

def get_data_filepath(filename):
    """Get the full path to a data file.
    
    Args:
        filename (str): The name of the data file.
        
    Returns:
        str: The full path to the data file.
    """
    return os.path.join(os.path.dirname(__file__), '..', 'data', filename)
