Feature: company classification
  As a data analyst
  I want a program that can extract the company name out of a sentence and predict the industry of the company
  so that I can use it to aggregate transactions by company names or industry

  Scenario Outline: company name and industry prediction
    When the program reads a <transaction text description>
    Then the program should predict the <company name> and the <company industry>

    Examples:
      | transaction text description                             | company name        | company industry  |
      | AQUILA FIRST ACH 5766804 BRUCE WAYNE                     | AQUILA              | Technology        |
      | PEARLBETA 8392 Daily Debi 5038822 BRUCE WAYNE            | PEARLBETA           | Technology        |
      | 7-Eleven                                                 | 7-Eleven            | Convenience store |
      | QuikTrip                                                 | QuikTrip            | Convenience store |
      | FRYS FOOD & DRUG 445 S                                   | Fry's Food and Drug | Supermarket       |
      | Mary goes to work out at Joe's Garage                    | Joe's Garage        | Fitness           |
      | Mary went to Macy's with Joe's wife                      | Macy's              | Department store  |
      | Mary had dinner at Macy's after shopping at Trader Joe's | Trader Joe's        | Grocery store     |
