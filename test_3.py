"""
the below function sums all the numbers at the current time e.g. 01:02:03 should return 6 - it does not work correctly. 
fix the function and write a unit test for it. Use any testing framework you're familiar
with.

"""

# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """
    expects data in the format HH:MM:SS
    """
    list_of_nums = time_str.split(":")
    return sum(list_of_nums)

# [TODO]: write a unittest test below
