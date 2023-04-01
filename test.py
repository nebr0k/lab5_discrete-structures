import unittest

from main import generate_result_set


class TestGenerateResultSet(unittest.TestCase):

    def test_generate_result_set(self):
        A = {'a', 'b'}
        B = {'x', 'y'}
        C = {0, 1}
        expected_result = {('x', 'a', 0), ('y', 'a', 0), ('x', 'b', 0), ('y', 'b', 0), ('x', 'a', 1), ('y', 'a', 1), ('x', 'b', 1), ('y', 'b', 1)}
        result_set = generate_result_set(A, B, C)
        self.assertEqual(result_set, expected_result)

    def test_multiple_element_sets(self):
        A = {'a', 'b', 'c'}
        B = {'x', 'y', 'z'}
        C = {0, 1}
        result_set = generate_result_set(A, B, C)
        expected = {
            ('x', 'a', 0), ('x', 'a', 1), ('x', 'b', 0), ('x', 'b', 1), ('x', 'c', 0), ('x', 'c', 1),
            ('y', 'a', 0), ('y', 'a', 1), ('y', 'b', 0), ('y', 'b', 1), ('y', 'c', 0), ('y', 'c', 1),
            ('z', 'a', 0), ('z', 'a', 1), ('z', 'b', 0), ('z', 'b', 1), ('z', 'c', 0), ('z', 'c', 1)
        }
        self.assertEqual(result_set, expected)


if __name__ == '__main__':
    unittest.main()
