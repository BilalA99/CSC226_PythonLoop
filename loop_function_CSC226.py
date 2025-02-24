import unittest



def print_numbers():

    for i in range(1, 6):  # Loop runs 5 times
        print(f"Iteration number: {i}")

# Calling the function to run it
print_numbers()



def countdown(n):
    while n > 0:  # Loop runs until n reaches 0
        print(f"Countdown: {n}")
        n -= 1

# Calling the function
countdown(5)

def print_numbers():
    return [i for i in range(1, 6)]  # Returns list instead of print

class TestLoopFunction(unittest.TestCase):
    def test_print_numbers(self):
        self.assertEqual(print_numbers(), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
