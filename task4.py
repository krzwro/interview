# Task 4
# Write a function that will return True if in each day we can find temperature above 15 degrees, return False otherwise.

def check_temperatures(measurements):
    return False

test_1 = {
    'day_1': [10, 12, 14, 16],
    'day_2': [11, 12, 13, 14, 15, 16, 17],
    'day_3': [20, 25, 30],
    'day_4': [1, 2, 10, 15, 16],
}


test_2 = {
    'day_1': [10, 12, 14, 13],
    'day_2': [11, 12, 13, 14],
    'day_3': [1, 2, 3],
    'day_4': [1, 2, 10],
}

test_3 = {
    'day_1': [10, 12, 14, 13],
    'day_2': [11, 12, 13, 14],
    'day_3': [1, 2, 3, 17],
    'day_4': [1, 2, 10],
}


assert check_temperatures(test_1) == True
assert check_temperatures(test_2) == False
assert check_temperatures(test_3) == False
