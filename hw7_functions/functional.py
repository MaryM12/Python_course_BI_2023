# Functional programming
def sequential_map(*args):
    """
    Sequentially applies functions to container values
    :param args: functions, a container
    :return: result of sequential application of functions to container values
    """
    *functions, container = args
    for function in functions:
        container = list(map(function, container))
    return container

def consensus_filter(*args):
    """
    :param args: functions with boolean output (filtering), a container
    :return: container with objects, which passed all the filters
    """
    *functions, container = args
    for function in functions:
        container = list(filter(function, container))
    return container

def conditional_reduce(func1, func2, container):
    """
    takes a container with values which are filtered with func1
    and applies reducing func2 to the values, which passed the filter
    :param func1: filtering function
    :param func2: reducing function
    :param container: container of values
    :return: result of sequential application of func2 to container values which are filtered with func1
    """
    container = list(filter(func1, container))
    result = container[0]
    for element in container[1:]:
        result = func2(result, element)
    return result

def func_chain(*args):
    """
    Takes any number of functions and returns
    a concatenated function which represents their sequential execution
    :param args: functions
    :return: single function
    """
    def concat(val):
        res = val
        for func in args:
            res = func(res)
        return res
    return concat

import sys
def print_analogue(*args, sep=' ', end='\n'):
    """
    Complete print analogue
    :param args: objects to print
    :param sep: separator
    :param end: end character
    :return: print objects in stdout
    """
    string = list(map(str, args))
    output = sep.join(string) + end
    sys.stdout.write(output)
    
