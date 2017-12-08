import unittest
from question3 import has_word_aquila


class TestQuestion3(unittest.TestCase):
    def test_has_word_aquila(self):
        transactions = [
            {'text': 'AQUILA FIRST ACH 5766804 BRUCE WAYNE  to AQUILA', 'expected_label': True},
            {'text': 'AUTOMATIC WITHDRAWAL, AQUILA FIR', 'expected_label': True},
            {'text': 'PEARLBETA 8392 Daily Debi 5038822 BRUCE WAYNE', 'expected_label': False},
            {'text': '7-Eleven', 'expected_label': False},
        ]
        for transaction in transactions:
            self.assertEqual(transaction['expected_label'], has_word_aquila(transaction['text']))


if __name__ == '__main__':
    unittest.main()
