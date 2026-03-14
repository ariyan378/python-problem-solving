''' 
Import statements: 
    1. Import the built-in json python package
    2. From employee.py, import the details function and the employee_name, age, title variables
'''

# Import json module (used to convert Python dictionary to JSON format)
import json

# Import specific items from employee.py
from employee import details, employee_name, age, title


def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    [IMPLEMENTATION]
        1. Return a dictionary that maps:
            "first_name" -> name
            "age" -> age
            "title" -> title

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title"
               to the name, age, and title arguments respectively.
               Values must be correctly typecasted:
                    name -> string
                    age -> int
                    title -> string
    """

    # Create dictionary with correct data types
    employee_dictionary = {
        "first_name": str(name),  # Ensure name is stored as string
        "age": int(age),          # Convert age to integer
        "title": str(title)       # Ensure title is stored as string
    }

    # Return the dictionary
    return employee_dictionary


def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    [IMPLEMENTATION]
        1. Open the employee.json file
        2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
    """

    # Open the output file in write mode
    # "w" means write (it will create the file if it doesn't exist)
    with open(output_file, "w") as file:

        # Write the JSON string into the file
        file.write(json_obj)


def main():

    # Print the contents of details()
    # This prints employee information from employee.py
    details()

    # Create employee dictionary using imported variables
    employee_dict = create_dict(employee_name, age, title)

    # Print dictionary to check if it was created correctly
    print("employee_dict: " + str(employee_dict))

    ''' 
    Use json.dumps() to convert employee_dict into a JSON string.
    dumps = dictionary → JSON string
    '''

    # Convert dictionary to JSON string
    json_object = json.dumps(employee_dict)

    # Print the JSON string
    print("json_object: " + str(json_object))

    # Write the JSON string to employee.json file
    write_json_to_file(json_object, "employee.json")


# This ensures main() runs only when the file is executed directly
if __name__ == "__main__":
    main()