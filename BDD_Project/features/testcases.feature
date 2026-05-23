Feature: BigBasket Functional Test Cases


  @positive
  Scenario: Search And Select Tea Product

    Given user is logged into BigBasket
    When the user clicks on Tea from the homepage
    And the user searches for Tea product
    And the user selects Tea checkbox
    Then filtered Tea products should be displayed


  @positive
  Scenario: Add Tea Product To Cart

    Given user is logged into BigBasket
    When the user clicks on Tea from the homepage
    And the user applies brand filter on Tea page
    And the user adds the first Tea product to cart


  @positive
  Scenario: Add And Delete Tea Product

    Given user is logged into BigBasket
    When the user clicks on Tea from the homepage
    And the user searches for Tea product
    And the user selects Tea checkbox
    And the user adds Tea product to cart
    And the user navigates to the cart page
    And the user deletes the Tea product
    Then the Tea product should be removed successfully


  @positive
  Scenario: Sort Ghee Products By Price Low To High

    Given user is logged into BigBasket
    When the user clicks on Ghee from the homepage
    And the user clicks on Relevance dropdown
    And the user selects Price Low To High
    Then sorted Ghee products should be displayed


  @negative
  Scenario: Login With Invalid Mobile Number

    Given the user is on the BigBasket homepage
    When the user clicks on the login button
    And the user enters invalid mobile number
    Then invalid mobile error should be displayed


  @negative
  Scenario: Login With Invalid OTP

    Given the user is on the BigBasket homepage
    When the user clicks on the login button
    And the user enters the mobile number
    And the user enters invalid OTP
    Then invalid OTP error should be displayed


  @negative
  Scenario: Search Invalid Tea Product

    Given user is logged into BigBasket
    When the user clicks on Tea from the homepage
    And the user searches invalid Tea product
    Then no results should be displayed

@negative
  Scenario: Enter Invalid Card Details

    Given user is logged into BigBasket
    When the user clicks on Tea from the homepage
    And the user applies brand filter on Tea page
    And the user adds the first Tea product to cart
    And the user navigates to the cart page
    And the user clicks on Proceed to Checkout
    And the user enters invalid card number
    Then invalid card error should be displayed
