#!/usr/bin/python3
"""
This module contains the function text_indentation()
"""
def text_indentation(text):
    """
    text_indentation adds 2 new lines after each of these characters '.', '?', ':'
    text (str) : The piece of text to be indented, must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_str = ""

    for element in text:
        if element == '.' or element == '?' or element == ':':
            new_str += element + '\n' + '\n' + '\n'.strip()
            continue
        new_str += "" + element
    print(new_str, end='')
        
    
text_indentation("""Hi. How are you? My name is: Zinhle Keswa.""")
