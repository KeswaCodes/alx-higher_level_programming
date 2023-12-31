
#!/usr/bin/python3
"""
This module contains the function print_square()
"""
def print_square(size):
    """
    This function prints a square using the character '#'
    size (int): the size length of the square
    """
    if size is None:
        raise TypeError("size must be an integer")
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('\n', end='')

            

