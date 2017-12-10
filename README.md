# aquila

## Development scripts
To run a common development script, execute one of the following commands:
- `sudo pip3 install -r requirements.txt`: Installs dependencies.
- `python3 -m unittest discover -s .`: Launches the test runner running all tests.

## Question 1
Below are some of my open source projects.

### elephant
- project URL: https://github.com/yuchenhou/elephant
- feature description: https://github.com/yuchenhou/elephant/blob/master/predict_link_weight.feature
- project type: deep learning

### rat
- project URL: https://github.com/yuchenhou/rat
- feature description: https://github.com/yuchenhou/rat/blob/master/classify_dna.feature
- project type: deep learning

### ajobpool
- project URL: https://gitlab.com/alanhou/ajobpool
- demo site URL: https://gitlab.com/alanhou/ajobpool
- project type: progressive web application

## Question 2
The solution to this problem consists of the following steps:
- Extract the company name
- Lookup the company industry

#### Extract the company name
In this stage, the program extracts the name of the company from the transaction text description.
A few possible extraction approaches are shown below
- Extract all word n-grams from the transaction,
where n is any possible number of words in a company name.
The drawback of this approach is
that it produces many word n-grams that are not the real company name,
This drawback does not have a very negative consequence
because these word n-grams will be regarded as unknown companies and ignored
in the next company industry lookup step.
- Reduce this problem to the Name Entity Recognition problem,
and apply a Named Entity Recognizer(NER).
A popular implementation of NER is the Stanford NER: https://nlp.stanford.edu/software/CRF-NER.shtml .
Stanford NER has a Python interface in python package NLTK: http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford .
NERs perform very well written English text data.
Unfortunately, they don't perform well in informal, short, incomplete sentences, such as transaction description:
https://www.quora.com/How-can-I-find-city-country-company-name-from-a-tweet-text-using-Java/answer/Jasneet-Sabharwal
because transaction descriptions lack of the structures in complete sentences.
- Apply a part-of-speech tagger trained on informal and short sentences such as
Tweet NLP: http://www.cs.cmu.edu/~ark/TweetNLP/ .
- Train dedicated recognizer or tagger on transaction text description data,
using a RNN or CNN model as shown in project https://github.com/yuchenhou/rat

#### Lookup the company industry
In this stage, the program looks up the company industry
by calling a company information lookup API with the company name.
This API can be provided by a third party or in house.
To build a in house service for this task,
we can collect company information from a data source,
and store the data in a database demonstrated by file `companies.json`.
A few possible data sources are shown below

| website | number of companies (million) | company industry information accuracy |
| --- | --- | --- |
| Wikipedia | much less than 5 | high |
| Linkedin | 19 | high | 
| Facebook | 65 | low |
| Google maps | unknow | high |
| Opencorporates | 137 | high |

The most promissing data source so far is Opencorporates.
It claims to be the largest open database of companies in the world,
and it provides the complete company data set for download.

## Question 3
To add a test case for a new transaction,
locate the list `transactions`
in `test_question3.TestQuestion3.test_has_word_aquila()`,
add a new dictionary for the new transaction in it
including the `text` field and the `expected_label` field.
