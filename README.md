# aquila

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

###### notes
- I did not include any Ruby project because I haven't used Ruby in 5 years.
But I am happy to get better at Ruby if your team uses Ruby for your projects.
- I included a Javascript project because I assume your team uses Javascript
for frontend web development and I think it is relevant skill.


## Question 3

#### Run the test
To launch the test runner, run this command in project root directory:

`python3 -m unittest discover -s .`.

#### Add a test case
To add a test case for a new transaction,
locate the list `transactions`
in `test_question3.TestQuestion3.test_has_word_aquila()`,
add a new dictionary for the new transaction in it
including the `text` field and the `expected_label` field.
