# OrangeHRM BDD Automation Framework

## Overview
A production-grade BDD automation framework built with Python, Selenium, and Behave targeting the OrangeHRM demo application.

## Technology Stack
- Python 3.x
- Selenium WebDriver
- Behave (BDD Framework)
- Allure Reporting
- Python Logging
- WebDriver Manager

## Project Structure
```text
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
├── requirements.txt
└── README.md 

Setup Instructions (Mac/Linux)
    Clone the repository
    Create virtual environment: python3 -m venv .venv
    Activate: source .venv/bin/activate
    Install dependencies: pip install -r requirements.txt
    Install Allure: brew install allure

Setup Instructions (Windows)
    Clone the repository
    Create virtual environment:python -m venv .venv
    Activate the environment: .venv\Scripts\activate
    Note: If using PowerShell and you get an "Execution_Policies" error, run Set-ExecutionPolicy Unrestricted -Scope CurrentUser as administrator first.
    Install dependencies: pip install -r requirements.txt
    Install Allure (choose one):
    NPM (Requires Node.js): npm install -g allure-commandline
    Scoop: scoop install allure
    Winget: winget install qameta.allure

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