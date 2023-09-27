Feature: Adding items to the cart on a shopping website

  Scenario: User adds items to the cart
    Given User is on the shopping website homepage
    When User searches and adds 5 mushrooms, 4 potatoes, 2 corns, 2 bananas, and 1 watermelon to the cart
    Then The cart should contain the selected items
    And The total number of items in the cart should be 12

  Scenario: User proceeds to checkout
    Given User is on the shopping cart page
    When User proceeds to checkout
    Then The checkout page should be displayed

  Scenario: User proceeds to checkout
    Given User has added items to the cart
    When User proceeds to checkout
    Then The checkout page should be displayed
    And The total number of items in the cart should be 12

### Negative Cases:

  Scenario: User adds an invalid quantity of items
    Given User is on the shopping website homepage
    When User attempts to add -5 mushrooms to the cart
    Then the it should fail to reduce the amount of product

  Scenario: User attempts to checkout without adding items
    Given User is on the shopping cart page
    When User proceeds to checkout without adding any items
    Then A message indicating an empty cart should be displayed

  Scenario: User removes items from an empty cart
    Given User is on the shopping cart page
    When User attempts to remove items from an empty cart
    Then A message indicating an empty cart should be displayed

  Scenario: User attempts to remove more items than in the cart
    Given User has added 2 bananas to the cart
    When User attempts to remove 3 bananas from the cart
    Then the it should fail to reduce the amount of product
