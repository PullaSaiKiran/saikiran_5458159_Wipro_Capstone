BIGBASKET AUTOMATION TESTING FRAMEWORK
Project Overview

This project is a Hybrid Automation Testing Framework developed for the BigBasket web application using:

Selenium WebDriver
Pytest Framework
BDD Framework using Behave
Python Programming Language

The framework automates multiple functionalities of the BigBasket application including:

Login Validation
Product Search
Product Filtering
Add To Cart Functionality
Cart Validation
Checkout Flow
Payment Validation
End-To-End Shopping Flow

The framework follows the Page Object Model (POM) architecture for better maintainability, scalability, and reusable automation scripts.

Technologies Used
Technology	Purpose
Python	Programming Language
Selenium WebDriver	Web Automation
Pytest	Functional Test Execution
Behave	BDD Framework
Allure Reports	HTML Reporting
OpenPyXL	Excel Data Handling
WebDriver Manager	Driver Management
PyCharm	IDE
GitHub	Version Control
Framework Architecture

The project follows:

Hybrid Automation Framework
Data-Driven Framework
Page Object Model (POM)
BDD Framework Architecture
Main Framework Components
Feature Files
Step Definition Files
Page Classes
Locator Classes
Utility Files
Reports
Logs
Test Data Files
Selenium With Pytest

The Selenium Functional Testing framework automates major functionalities of the application using Pytest.

Functional Test Cases Automated
Valid Login
Tea Product Flow
Ghee Product Flow
Checkout Flow
Invalid Mobile Number Validation
Invalid OTP Validation
Features
Assertions
Screenshot Capturing
Logging
Excel Data-Driven Testing
Allure Reporting
BDD With Behave

Behavior Driven Development (BDD) is implemented using Behave framework with Gherkin syntax.

BDD Scenarios Automated
Login Validation
Tea Product Search
Product Filtering
Add Product To Cart
Delete Product From Cart
Cart Validation
Checkout Validation
Invalid Card Validation
End-To-End Shopping Flow
Gherkin Example
Scenario: Add Tea Product To Cart

Given user is logged into BigBasket
When the user clicks on Tea from the homepage
And the user adds Tea product to cart
Then the Tea product should be added successfully
Page Object Model (POM)

The framework follows the Page Object Model design pattern.

In POM:
Locators are maintained separately
Reusable methods are maintained in page classes
Test scripts are maintained separately
Advantages
Better code reusability
Easy maintenance
Reduced code duplication
Improved scalability
Assertions Implemented

The framework contains assertion validations for:

Login validation
Product visibility
Brand filter validation
Product addition validation
Cart validation
Checkout validation
Invalid mobile number validation
Invalid OTP validation
Invalid card validation
Reporting And Logging

The framework integrates:

Allure Reports
Screenshot Attachments
Execution Logs
Allure Reports Include
Passed Test Cases
Failed Test Cases
Screenshots
Logs
Execution Summary
Failure Analysis
Data-Driven Testing

The framework supports Excel-based data handling using OpenPyXL.

Test Data Includes
Mobile Numbers
Product Names
Brand Names
Invalid Credentials
Invalid Payment Details
End-To-End Testing Flow

The framework automates the complete user workflow:

Login To Application
Add Tea Product
Add Ghee Product
Navigate To Cart
Proceed To Checkout
Validate Invalid Card Flow

This validates complete application behavior and integration between modules.

Project Structure
Project_BigBasket
│
├── data
├── features
├── locators
├── logs
├── pages
├── reports
├── tests
├── utils
├── requirements.txt
├── run_tests.py
└── README.md
Installation

Clone the repository:

git clone <repository_url>

Install dependencies:

pip install -r requirements.txt
Running Selenium Pytest Tests
pytest -v
Running BDD Behave Tests
behave features/
Running Complete Framework
python run_tests.py

This command:

Executes tests
Captures screenshots
Generates logs
Generates Allure Reports
Opens Allure HTML Report
Generating Allure Reports
allure serve reports/allure-results
Test Execution Summary
Selenium With Pytest
Total Tests Executed : 6
Passed : 6
Failed : 0
Accuracy : 100%
BDD With Behave
Total Scenarios Executed : 9
Passed : 9
Failed : 0
Accuracy : 100%
Features Of The Framework
Reusable Automation Scripts
Hybrid Framework Design
Page Object Model Architecture
Data-Driven Testing
Assertion Validation
End-To-End Testing
Allure HTML Reporting
Screenshot Capturing
Logging Support
Easy Maintenance
Conclusion

The BigBasket Automation Testing Framework successfully automates functional and End-To-End testing using Selenium WebDriver with Pytest and BDD using Behave. The framework provides scalable architecture, reusable automation scripts, professional reporting, and robust validation mechanisms suitable for real-time automation testing projects.