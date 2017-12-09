import json
from nltk import ngrams


def extract_word_n_grams(word_sequence: str, number_of_words_max: int) -> list:
    words = word_sequence.lower().split()
    word_n_grams = []
    for number_of_words in range(1, number_of_words_max + 1):
        for n_gram in ngrams(words, number_of_words):
            word_n_grams.append(' '.join(n_gram))
    return word_n_grams


def company_lookup_api(word_n_grams: list) -> dict:
    with open('companies.json') as companies_file:
        known_companies = json.load(companies_file)
    company_information = {}
    for word_n_gram in word_n_grams:
        if word_n_gram in known_companies:
            company_information[word_n_gram] = known_companies[word_n_gram]
    return company_information


def identify_company(transaction: str) -> dict:
    return company_lookup_api(extract_word_n_grams(transaction, 2))
