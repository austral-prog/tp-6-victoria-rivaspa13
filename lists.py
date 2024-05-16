def remove_elements(list_to_remove_elements):
    return list_to_remove_elements[1 : 4]

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    elif len(list_to_check) != 0:
        return False
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3:
        return False
    elif len(list_to_compare2) < 3:
        return False
    elif (list_to_compare1[2] == list_to_compare2[2]):
        return True
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    if (len(list_of_lists_to_modify [0]) >= 2) and (len(list_of_lists_to_modify [1]) >= 5) and (len(list_of_lists_to_modify [2]) >= 2):
        return [list_of_lists_to_modify [0] [0 : 2], list_of_lists_to_modify [1] [1 : 4], list_of_lists_to_modify [2] [-2 : ]]
    elif len(list_of_lists_to_modify [0]) < 2:
        return [list_of_lists_to_modify [0], list_of_lists_to_modify [1] [1 : 4], list_of_lists_to_modify [2] [-2 : ]]
    elif len(list_of_lists_to_modify [1]) < 5 and len(list_of_lists_to_modify [2]) < 2:
        return [list_of_lists_to_modify [0] [0: 2], list_of_lists_to_modify [1], list_of_lists_to_modify [2]]
    elif len(list_of_lists_to_modify [1]) < 5:
        return [list_of_lists_to_modify [0] [0 : 2], list_of_lists_to_modify [1], list_of_lists_to_modify [2] [-2 : ]]
    elif len(list_of_lists_to_modify [2]) < 2:
        return [list_of_lists_to_modify [0] [0 : 2], list_of_lists_to_modify [1] [1 : 4], list_of_lists_to_modify [2]]
