#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    takes two lists and creates a new list with result of divison
    operation

    handles errors and prints them to stdout
    """
    new_list = []
    result = 0
    for elem in range(0, list_length):
        try:
            result = (my_list_1[elem] / my_list_2[elem])
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
