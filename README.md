# BigBasket Automation Testing Framework

## Project Overview
This project is an automation testing framework developed for testing the BigBasket web application using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

The framework supports scalable and maintainable automated UI testing.

---

# Project Structure

```text
Project_Bigbasket/
│
├── config/
│   └── config.properties
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   ├── config_reader.py
│   └── logger.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Selenium
- Pytest
- Page Object Model (POM)
- Allure Reports

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd Project_Bigbasket
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration Setup

Create file:

```text
config/config.properties
```

Add:

```properties
browser=chrome
url=https://www.bigbasket.com/
```

---

# Running Tests

## Run Complete Test Suite

```bash
pytest
```

## Run Specific Test File

```bash
pytest tests\test_login.py
```

## Run Specific Test Case

```bash
pytest -v -s tests\test_login.py::test_login
```

---

# Generate Allure Report

Run tests with:

```bash
pytest --alluredir=reports/
```

Generate report:

```bash
allure serve reports/
```

---

# Features

- Selenium-based UI automation
- Pytest framework integration
- Reusable utility functions
- Configurable browser support
- Scalable Page Object Model design
- Allure reporting support

---

# Sample Test Scenario

## Login Test

- Open browser
- Navigate to BigBasket website
- Perform login action
- Validate successful login

---

# Author

Sai Kiran

---

# Future Enhancements

- Cross-browser testing
- Data-driven testing
- CI/CD integration
- Screenshot capture on failure
- Parallel test execution
