#checking the structural similarity in nested lists in Python

def same_structure_as(a, b):
    if isinstance(a, list) != isinstance(b, list):
        return False
    if not isinstance(a, list):
        return True
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if not same_structure_as(x, y):
            return False
    return True
