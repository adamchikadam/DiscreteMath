import unittest
from powerset_interactive import powerset

class TestPowerset(unittest.TestCase):
# Проверка на правильную обработку пустых множеств
    def test_empty_set(self):
        self.assertEqual(powerset([]), [[]])
# Проверка множеств с числами
    def test_small_set_numbers(self):
        my_set = [1, 2]
        expected_powerset = [[], [1], [2], [1, 2]]
        self.assertEqual(sorted(map(sorted, powerset(my_set))), sorted(map(sorted, expected_powerset)))
# Проверка множеств со строками
    def test_small_set_strings(self):
        my_set = ["a", "b"]
        expected_powerset = [[], ["a"], ["b"], ["a", "b"]]
        self.assertEqual(sorted(map(sorted, powerset(my_set))), sorted(map(sorted, expected_powerset)))

if __name__ == '__main__':
    unittest.main()
#Все три теста завершены успешно