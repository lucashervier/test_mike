"""
This will be the module description. It will be automatically generated properly
with mkdocs.
Do not forget to follow
[Google docstrings convention](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) format.
"""
import numpy as np

# def hello_world():
#     """
#     A method that print "Hello World!".

#     Note:
#         This method do not requires any parameters.
#     """
#     print("Hello World!")

# def addition(a: float, b: float):
#     """
#     A method that performs the following math:

#     $$
#     c = a + b
#     $$

#     Args:
#         a (float): A float number
#         b (float): Another float number
    
#     Returns:
#         float: The sum of a and b
#     """
#     c = np.sum([a, b])

#     return c

# def bye_world():
#     """
#     A method that print "Bye World!".

#     Note:
#         This method do not requires any parameters.
#     """

#     print("Bye World")

def hello_world():
    """
    A method that print "Hello World!".

    Note:
        This method do not requires any parameters.
    """
    print("Hello World!")

def addition(a: float, b: float) -> float:
    """
    A method that performs the following math:

    $$
    c = a + b
    $$

    Parameters
    ----------
    a
        A float number
    b
        Another float number
    
    Returns
    -------
    c
        The sum of a and b
    """
    c = np.sum([a, b])

    return c

def bye_world():
    """
    A method that print "Bye World!".

    Note:
        This method do not requires any parameters.
    """

    print("Bye World")
