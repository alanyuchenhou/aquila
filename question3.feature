Feature: company name extraction
  As a data analyst
  I want a program that can identify if a transaction text description contains word Aquila
  so that I can use it to do something cool

  Scenario Outline: company name and industry prediction
    When the program reads a <transaction text description>
    Then the program should answer <whether the text description contains word Aquila>

    Examples:
      | transaction text description                    | whether the text description contains word Aquila |
      | AQUILA FIRST ACH 5766804 BRUCE WAYNE  to AQUILA | true                                              |
      | AUTOMATIC WITHDRAWAL, AQUILA FIR                | true                                              |
      | PEARLBETA 8392 Daily Debi 5038822 BRUCE WAYNE   | false                                             |
      | 7-Eleven                                        | false                                             |
