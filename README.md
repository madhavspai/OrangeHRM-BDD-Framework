# OrangeHRM BDD Automation Framework

## Overview
A production-grade BDD automation framework built with Python, Selenium, and Behave targeting the OrangeHRM demo application.

## Technology Stack
- Python 3.x
- Selenium WebDriver
- Behave (BDD Framework)
- Allure Reporting
- Python Logging

## Project Structure
OrangeHRM-BDD-Framework/
├── features/
│   ├── login.feature
│   ├── employee.feature
│   ├── myinfo.feature
│   ├── search.feature
│   ├── environment.py
│   └── steps/
├── pages/
├── logs/
├── reports/
├── test_data.py
├── logger.py
└── README.md

## Setup Instructions
1. Clone the repository
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install selenium behave allure-behave webdriver-manager`
5. Install Allure: `brew install allure`

## Run Tests
```bash
behave features/
```

## Run with Allure Report
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
allure serve reports/
```

## Features Covered
- Login Functionality (5 scenarios)
- Add Employee (4 scenarios)
- My Info / Personal Details (4 scenarios)
- Employee Search (4 scenarios)

## Assumptions
- OrangeHRM demo site is accessible
- Chrome browser is installed
- Tests run sequentially

## Limitations
- Demo site occasionally slow causing intermittent failures
- Shared demo environment — test data may vary