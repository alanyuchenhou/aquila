import unittest
from question2 import extract_word_n_grams, company_lookup_api, identify_company


class TestQuestion3(unittest.TestCase):

    def test_extract_word_n_grams(self):
        word_sequence_test_cases = [{
            'sequence': 'AQUILA FIRST ACH 5766804',
            'number_of_words_max': 1,
            'word_n_grams': ['aquila', 'first', 'ach', '5766804'],
        }, {
            'sequence': 'AQUILA FIRST ACH 5766804',
            'number_of_words_max': 2,
            'word_n_grams': ['aquila', 'first', 'ach', '5766804', 'aquila first', 'first ach', 'ach 5766804'],
        }]
        for test_case in word_sequence_test_cases:
            self.assertEqual(
                test_case['word_n_grams'], extract_word_n_grams(test_case['sequence'], test_case['number_of_words_max'])
            )

    def test_company_lookup_api(self):
        company_lookup_test_cases = [{
            'word_n_grams': ['aquila', 'first', 'ach', '5766804', 'aquila first', 'first ach', 'ach 5766804'],
            'company_information': {'aquila': 'technology'}
        }, {
            'word_n_grams': ['home', 'depot', 'home depot'],
            'company_information': {'home depot': 'home improvement store'}
        }]
        for test_case in company_lookup_test_cases:
            self.assertEqual(test_case['company_information'], company_lookup_api(test_case['word_n_grams']))

    def test_identify_company(self):
        transactions = [{
            'text': 'AQUILA FIRST ACH 5766804 BRUCE WAYNE  to AQUILA',
            'company_information': {'aquila': 'technology'}
        }, {
            'text': '7-Eleven',
            'company_information': {'7-eleven': 'convenience store'}
        }, {
            'text': 'PEARLBETA 8392 Daily Debi 5038822 BRUCE WAYNE',
            'company_information': {'pearlbeta': 'technology'}
        }, {
            'text': 'TRANSACTION OF A UNKNOWN COMPANY HERE: ALAN FOODS Daily Debi',
            'company_information': {}
        }, {
            'text': "Mary had dinner at Macy's after shopping at Trader Joe's",
            'company_information': {"macy's": 'department store', "trader joe's": 'department store'}
        }]
        for transaction in transactions:
            self.assertEqual(transaction['company_information'], identify_company(transaction['text']))


if __name__ == '__main__':
    unittest.main()
