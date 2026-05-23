Feature: BigBasket E2E Shopping Flow


  Background:

    Given the user is on the BigBasket homepage


  @endtoend
  Scenario: User logs in, adds Tea and Ghee products, and proceeds to checkout

    When the user clicks on the login button
    And the user enters the mobile number
    And the user enters the OTP
    Then the user should be logged in successfully

    When the user clicks on Tea from the homepage
    And the user applies brand filter on Tea page
    And the user adds the first Tea product to cart
    Then the Tea product should be added successfully

    When the user goes back to the homepage
    And the user clicks on Ghee from the homepage
    And the user applies brand filter on Ghee page
    And the user adds the first Ghee product to cart
    Then the Ghee product should be added successfully

    When the user navigates to the cart page
    Then the cart should contain added products

    When the user clicks on Proceed to Checkout
    Then the checkout page should be displayed

    When the user enters invalid card number
    Then invalid card error should be displayed