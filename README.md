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

#Windows
1. Clone the repository
2. Create virtual environment: python -m venv venv
3. Activate the environment: venv\Scripts\activate
4. Install dependencies: pip install selenium behave allure-behave webdriver-manager
5. Install Allure (choose one of the following methods):
6. Using Scoop (closest to Homebrew): scoop install allure
    Using NPM (requires Node.js): npm install -g allure-commandline
    Using Winget: winget install qameta.allure
    Note on Activation: If you are using PowerShell and get an "Execution_Policies" error on Step 3, you may need to run Set-ExecutionPolicy Unrestricted -Scope CurrentUser as an administrator first.

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