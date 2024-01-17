#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements in alist.

    Args:
    my_list(list) : list to print elements
    x(int): number of elements to print

    Returns:
    number of elements printed.
    """

    real_elements_printed = 0
    try:
        for i in range(len(my_list)):
            print(my_list[i], end=" ")
            real_elements_printed += 1
            if real_elements_printed == x:
                break
        print()
    except TypeError:
        print("Error: List must contain only printable elements")
    except Exception as e:
        print("Error: ", str(e))

    return real_elements_printed
