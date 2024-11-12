def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    lst = [x**2 for x in range(1,12) if x % 2 == 0]
    return lst

def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    # new_dict = dict(students)
    new_dict = {}
    for x in students:
        new_dict[x[0]] = x[1]
    return new_dict

def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
    return nested['c']['x']

def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}
    nested['a'].append(6)
    return nested

def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    nested['b'] = list(nested['b'])
    nested['b'].append(6)
    return nested
