#!/usr/bin/python3
def no_c(my_string):
  """
  Removes all characters "c" and "C" from a string.

  Args:
    my_string: The string to remove characters from.

  Returns:
    A new string with all "c" and "C" characters removed.
  """
  new_string = ""
  for char in my_string:
    if char.lower() != "c":
      new_string += char
  return new_string
