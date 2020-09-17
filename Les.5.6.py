some_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
def remove_empty(some_dict: dict) -> dict:

    some_dict = {key: value for key, value in some_dict.items() if value is not None}

    return some_dict

print(remove_empty(some_dict))