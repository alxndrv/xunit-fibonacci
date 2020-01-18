import unittest
import os
from fib import fibonacci, get_fibonacci_seq, write_sequence_to_file


class TestFibonacciGenerator(unittest.TestCase):
    def test_sequence_length(self):
        start = 1
        N = 15
        sequence = get_fibonacci_seq(start, N)
        self.assertEqual(N, len(sequence))

    def test_start_value(self):
        start = 20
        N = 10
        sequence = get_fibonacci_seq(start, N)
        self.assertTrue(sequence[0] > N)


class TestUserInputs(unittest.TestCase):
    def test_correct_arguments(self):
        argv = ["10", "15"]
        fibonacci(argv)

    def test_missing_arguments(self):
        argv = []
        with self.assertRaises(RuntimeError):
            fibonacci(argv)


class TestFileOutput(unittest.TestCase):

    test_filename = ".fib_test.txt"

    def setUp(self):
        # If file exists from previous tests, we want to remove it
        if (os.path.exists(self.test_filename)):
            os.remove(self.test_filename)

        assert not os.path.exists(self.test_filename)

    def test_file_creation(self):
        sequence = [1, 1, 2, 3, 5, 8, 13]
        write_sequence_to_file(sequence, self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

    def tearDown(self):
        if (os.path.exists(self.test_filename)):
            os.remove(self.test_filename)
