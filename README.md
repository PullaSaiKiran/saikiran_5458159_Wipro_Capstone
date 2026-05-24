# BigBasket Automation Testing Framework

> **Selenium WebDriver · Pytest · Behave BDD · Page Object Model · Allure Reports**

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Technologies Used](#2-technologies-used)
3. [Framework Architecture](#3-framework-architecture)
4. [Project Structure](#4-project-structure)
5. [Selenium with Pytest](#5-selenium-with-pytest)
6. [BDD with Behave](#6-bdd-with-behave)
7. [Page Object Model](#7-page-object-model)
8. [Assertions Summary](#8-assertions-summary)
9. [Data-Driven Testing](#9-data-driven-testing)
10. [Reporting and Logging](#10-reporting-and-logging)
11. [Installation and Usage](#11-installation-and-usage)
12. [Test Execution Summary](#12-test-execution-summary)
13. [End-to-End Flow](#13-end-to-end-flow)
14. [Conclusion](#14-conclusion)

---

## 1. Project Overview

This project is a **Hybrid Automation Testing Framework** developed for the BigBasket web application. It combines functional testing using **Selenium + Pytest** and behavior-driven testing using **Behave BDD**, following the **Page Object Model (POM)** architecture for maintainability and scalability.

**Functionalities Automated:**

- Login validation (valid and invalid)
- Tea product category flow with brand and price filtering
- Ghee product category flow with brand and price filtering
- Cart validation
- Checkout flow
- Invalid card payment validation
- Unknown brand search (negative)
- Invalid OTP and mobile number validation (negative)

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Primary programming language |
| Selenium WebDriver | Browser automation and UI interaction |
| Pytest | Functional test execution and assertions |
| Behave | BDD framework with Gherkin syntax |
| Allure Reports | HTML reporting with screenshots and logs |
| OpenPyXL | Excel-based data-driven test handling |
| WebDriver Manager | Automatic browser driver management |
| PyCharm | Integrated Development Environment |
| GitHub | Version control and repository hosting |

---

## 3. Framework Architecture

The project follows a **Hybrid Framework** combining three design patterns:

- **Page Object Model (POM)** — locators and page methods encapsulated per page class
- **Data-Driven Framework** — test data managed via Excel files (OpenPyXL)
- **BDD with Behave** — Gherkin feature files drive human-readable scenario execution

---

## 4. Project Structure

```
Project_BigBasket/
│
├── data/                        # Excel test data files (OpenPyXL)
│   ├── login_data.xlsx
│   ├── product_data.xlsx
│   ├── brand_data.xlsx
│   └── payment_data.xlsx
│
├── features/                    # Gherkin BDD feature files
│   ├── bigbasket.feature
│   ├── environment.py           # Behave hooks (setup / teardown)
│   └── steps/
│       └── bigbasket_steps.py   # Step definitions
│
├── locators/                    # Element locator classes
│   ├── login_locators.py
│   ├── home_locators.py
│   ├── product_locators.py
│   ├── cart_locators.py
│   └── checkout_locators.py
│
├── logs/                        # Timestamped execution log files
│
├── pages/                       # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/                     # Allure results and screenshots
│   ├── allure-results/
│   └── screenshots/
│
├── tests/                       # Pytest functional test modules
│   ├── test_login.py
│   ├── test_tea_flow.py
│   ├── test_ghee_flow.py
│   └── test_checkout.py
│
├── utils/                       # Shared utility helpers
│   ├── driver_factory.py
│   ├── logger.py
│   ├── screenshot.py
│   └── excel_reader.py
│
├── config/
│   └── config.ini               # Browser, URL, credentials config
│
├── requirements.txt             # Python dependency list
├── run_tests.py                 # Master runner (Pytest + Behave + Allure)
└── README.md
```

---

## 5. Selenium with Pytest

The Pytest module automates core functional tests with explicit assertions, logging, and Allure reporting on every test.

### 5.1 Test Cases

| Test ID | Test Case | Type | Status |
|---|---|---|---|
| TC_POS_01 | Valid login with correct mobile number and OTP | Positive | PASS |
| TC_POS_02 | Tea product flow — filter brand + price, add to cart | Positive | PASS |
| TC_POS_03 | Ghee product flow — filter brand + price, add to cart | Positive | PASS |
| TC_POS_04 | Cart validation — both Tea and Ghee products visible | Positive | PASS |
| TC_NEG_01 | Login fails with invalid mobile number (less than 10 digits) | Negative | PASS |
| TC_NEG_02 | Login fails with invalid OTP (wrong 4-digit code) | Negative | PASS |

### 5.2 Framework Features

- Screenshot capture on every failed test case
- Timestamped execution logs per session
- Excel-based data-driven testing via OpenPyXL
- Allure report generation with test step details
- Explicit `WebDriverWait` — no hard sleeps
- JS click fallback for React/SPA intercepted elements
- Stale element retry mechanism (3 attempts)
- Scroll-to-element before every interaction

---

## 6. BDD with Behave

Behavior Driven Development is implemented using the **Behave** framework. Scenarios are written in Gherkin and cover both positive and negative user journeys.

### 6.1 BDD Scenarios

| Scenario ID | Scenario | Type | Status |
|---|---|---|---|
| SC_01 | Valid login, Tea + Ghee full E2E flow with checkout | Positive | PASS |
| SC_02 | Search known brand "Tata Tea" in Tea page — results displayed | Positive | PASS |
| SC_03 | Search known brand "Amul" in Ghee page — results displayed | Positive | PASS |
| SC_04 | Add Tea product — cart count increments to 1 | Positive | PASS |
| SC_05 | Login fails with invalid mobile number "12345" | Negative | PASS |
| SC_06 | Login fails with invalid OTP "0000" | Negative | PASS |
| SC_07 | Unknown brand "XYZUnknownBrand999" in Tea — no results shown | Negative | PASS |
| SC_08 | Unknown brand "XYZUnknownBrand999" in Ghee — no results shown | Negative | PASS |
| SC_09 | Checkout with invalid card details — payment error displayed | Negative | PASS |

### 6.2 Gherkin Examples

**Positive — End-to-End shopping flow:**

```gherkin
Scenario: Valid login, Tea + Ghee full flow with checkout
  Given the user is on the BigBasket homepage
  When  the user clicks on the login button
  And   the user enters a valid mobile number "9876543210"
  And   the user enters the OTP
  Then  the user should be logged in successfully

  When  the user clicks on Tea from the homepage
  And   the user applies brand filter on Tea page
  And   the user applies price filter on Tea page
  And   the user adds the first Tea product to cart
  Then  the Tea product should be added successfully

  When  the user goes back to the homepage
  And   the user clicks on Ghee from the homepage
  And   the user applies brand filter on Ghee page
  And   the user applies price filter on Ghee page
  And   the user adds the first Ghee product to cart
  Then  the Ghee product should be added successfully

  When  the user navigates to the cart page
  Then  the cart should have items
  When  the user clicks on Proceed to Checkout
  Then  the checkout page should be displayed
```

**Positive — Known brand search:**

```gherkin
Scenario: Search for a known brand in Tea page and verify results
  Given the user is on the BigBasket homepage
  When  the user clicks on Tea from the homepage
  And   the user searches for brand "Tata Tea" in the brand filter
  Then  the brand "Tata Tea" results should be displayed in the listing
  And   the product count should be greater than zero
```

**Negative — Invalid mobile number:**

```gherkin
Scenario: Login fails with invalid mobile number
  Given the user is on the BigBasket homepage
  When  the user clicks on the login button
  And   the user enters an invalid mobile number "12345"
  Then  an error message should be displayed for invalid mobile number
  And   the user should remain on the login page
```

**Negative — Invalid OTP:**

```gherkin
Scenario: Login fails with invalid OTP
  Given the user is on the BigBasket homepage
  When  the user clicks on the login button
  And   the user enters a valid mobile number "9876543210"
  And   the user enters an invalid OTP "0000"
  Then  an OTP error message should be displayed
  And   the user should not be logged in
```

**Negative — Unknown brand search:**

```gherkin
Scenario: Search for unknown brand in Tea page shows no results
  Given the user is on the BigBasket homepage
  When  the user clicks on Tea from the homepage
  And   the user searches for brand "XYZUnknownBrand999" in the brand filter
  Then  no brand results should be found for "XYZUnknownBrand999"
  And   the listing should show no matching products or a no-results message
```

**Negative — Invalid card details at checkout:**

```gherkin
Scenario: Checkout fails with invalid card details
  Given the user is on the BigBasket homepage
  When  the user clicks on the login button
  And   the user enters a valid mobile number "9876543210"
  And   the user enters the OTP
  Then  the user should be logged in successfully

  When  the user clicks on Tea from the homepage
  And   the user adds the first Tea product to cart
  Then  the Tea product should be added successfully

  When  the user navigates to the cart page
  Then  the cart should have items
  When  the user clicks on Proceed to Checkout
  Then  the checkout page should be displayed

  When  the user selects card payment option
  And   the user enters invalid card number "1234567890123456"
  And   the user enters invalid card expiry "01/20"
  And   the user enters invalid CVV "00"
  And   the user clicks Pay Now
  Then  a card validation error should be displayed
  And   the payment should not be processed
```

---

## 7. Page Object Model

Each screen has a dedicated page class. Locators are stored separately from page logic.

| Page Class | Responsibilities |
|---|---|
| `BasePage` | Explicit waits, JS click, scroll, stale element retry, dynamic locators |
| `LoginPage` | Valid/invalid mobile entry, OTP handling, login success/failure assertions |
| `HomePage` | Click Tea/Ghee category cards, navigate back to homepage |
| `ProductPage` | Brand filter search (known and unknown), price filter, add first product to cart |
| `CartPage` | Navigate to cart, item count assertion, proceed to checkout |
| `CheckoutPage` | Card payment entry, invalid card validation, payment error assertion |

---

## 8. Assertions Summary

### Login — Positive
- Sign In button is present before clicking
- Mobile input appears after opening login modal
- Mobile number is exactly 10 numeric digits
- Field value matches the typed mobile number
- OTP input field appears after mobile submission
- User icon is visible after successful OTP
- URL does not contain "login" after successful login

### Login — Negative (Invalid Mobile)
- Error message visible for invalid mobile input
- OTP screen is not shown after invalid mobile
- User icon is absent (user not logged in)
- User remains on the login page

### Login — Negative (Invalid OTP)
- OTP error message is visible after wrong OTP submission
- User icon is absent after invalid OTP
- Login should not succeed with wrong OTP

### Tea Page — Positive
- URL contains "tea" after category click
- Brand filter section is present on the listing page
- Brand options exist inside the filter panel
- Products count > 0 after brand filter applied
- Price filter section is present
- Products count > 0 after price filter applied
- Product card count > 0 before adding to cart
- Product name text is not empty
- Add button is visible on the product card
- Cart badge count > 0 after adding product

### Ghee Page — Positive
- URL contains "ghee" after category click
- Same filter and cart assertions as Tea page
- Ghee product name differs from Tea product name

### Brand Search — Positive
- Brand input field is present inside filter
- Results are shown for known brand name
- Product count is greater than zero

### Brand Search — Negative
- No brand labels match the unknown brand name
- Product listing is empty or no-results message is shown

### Cart Page
- Cart icon is visible in the header
- URL contains "basket" or "cart" after navigation
- Cart contains at least 1 item
- Cart item count is greater than or equal to 2 (Tea + Ghee)
- Proceed to Checkout button is present
- Proceed to Checkout button is enabled (not disabled)

### Checkout Page — Positive
- Checkout URL or heading confirmed after clicking proceed

### Checkout — Negative (Invalid Card)
- Card number field, expiry field, and CVV field are present
- Validation error shown for expired date
- Validation error shown for invalid card number
- Validation error shown for invalid CVV
- Order success element is absent (payment not processed)
- Page remains on checkout (not redirected to confirmation)

---

## 9. Data-Driven Testing

Test data is managed in Excel files using **OpenPyXL**, allowing parameterised execution without code changes.

| Excel Sheet | Data Stored |
|---|---|
| `login_data.xlsx` | Valid mobile numbers, invalid mobiles, invalid OTPs |
| `product_data.xlsx` | Product names (Tea, Ghee), known brand names |
| `brand_data.xlsx` | Valid brands (Tata Tea, Amul), invalid brand strings |
| `payment_data.xlsx` | Invalid card numbers, expired dates, invalid CVVs |

---

## 10. Reporting and Logging

### Allure Reports
- Passed and failed test summary with counts
- Per-step execution details
- Automatic screenshot attachment on failures
- Execution timeline and duration per scenario
- Environment metadata (browser, base URL)

### Logging
- Timestamped log file created per execution session
- `INFO` — every page action logged with element detail
- `WARNING` — fallback strategies (JS click, stale retry)
- `ERROR` — element not found, timeout, assertion failure

---

## 11. Installation and Usage

### Prerequisites
- Python 3.8 or higher
- Google Chrome or Firefox browser
- Allure CLI (for HTML report generation)

### Install Dependencies

```bash
git clone <repository_url>
cd Project_BigBasket
pip install -r requirements.txt
```

### Run Tests

| Command | Description |
|---|---|
| `pytest -v` | Run all Pytest functional tests |
| `pytest -v --alluredir=reports/allure-results` | Run Pytest with Allure output |
| `behave features/` | Run all BDD Behave scenarios |
| `behave features/bigbasket.feature` | Run specific feature file |
| `python run_tests.py` | Run full framework (Pytest + Behave + Allure) |
| `allure serve reports/allure-results` | Open Allure HTML report in browser |

### Configuration

Edit `config/config.ini`:

```ini
[browser]
browser       = chrome       ; chrome | firefox
headless      = False        ; True for CI/CD pipelines
implicit_wait = 10
explicit_wait = 20

[app]
base_url      = https://www.bigbasket.com
mobile_number = 9876543210

[paths]
screenshot_dir = reports/screenshots
log_dir        = logs
allure_results = reports/allure-results
```

### Requirements

```
selenium>=4.15.0
behave>=1.2.6
pytest>=7.4.0
webdriver-manager>=4.0.1
allure-behave>=2.13.2
allure-pytest>=2.13.2
openpyxl>=3.1.2
```

---

## 12. Test Execution Summary

### Selenium with Pytest

| Metric | Value |
|---|---|
| Total Tests Executed | 6 |
| Passed | 6 |
| Failed | 0 |
| Pass Rate | 100% |

### BDD with Behave

| Metric | Value |
|---|---|
| Total Scenarios Executed | 9 |
| Passed | 9 |
| Failed | 0 |
| Pass Rate | 100% |

---

## 13. End-to-End Flow

The complete user journey automated by the framework:

1. Open BigBasket homepage and verify URL contains "bigbasket"
2. Click Sign In — verify login modal opens and mobile input appears
3. Enter valid mobile number — verify 10-digit format and field value match
4. Enter OTP (manual or automated) — verify OTP input field appeared
5. Verify login success — user icon visible, URL does not contain "login"
6. Click Tea category card — verify URL contains "tea"
7. Apply brand filter — verify brand options exist and products > 0
8. Apply price filter — verify products still visible after filter
9. Add first Tea product — verify Add button visible, cart badge increments
10. Navigate back to homepage — verify BigBasket home URL
11. Click Ghee category card — verify URL contains "ghee"
12. Apply brand and price filters — same assertions as Tea page
13. Add first Ghee product — verify cart badge increments, Ghee name differs from Tea
14. Navigate to cart — verify URL contains "basket", item count >= 2
15. Click Proceed to Checkout — verify button is present and enabled
16. Verify checkout page — URL or page heading confirmed

---

## 14. Conclusion

The BigBasket Automation Testing Framework successfully automates **6 Pytest functional tests** and **9 BDD Behave scenarios** with a **100% pass rate**.

**Framework highlights:**

- Scalable hybrid architecture combining POM, BDD, and Data-Driven design
- Robust assertions at every major user action across all pages
- Automatic screenshot capture and Allure HTML reporting
- Full positive and negative coverage including invalid login, unknown brand search, and invalid card validation
- Reusable page objects with centralized locator management
- Config-driven execution for easy environment switching
- Production-ready structure suitable for CI/CD pipeline integration

---

*BigBasket QA Framework — Automation Testing Documentation*