# Bookstore API Automation Framework

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Requests](https://img.shields.io/badge/Requests-2.34-green)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

This project contains automated test for the [DemoQA Bookstore API](https://demoqa.com/swagger) built with Python, Pytest, and Requests for REST API automation testing with request/response logging, CI/CD integration, and Allure reporting.

---

## Project Features

- REST API automation testing
- Reusable API client
- Service layer architecture
- Separated test data and configurations
- Request and response logging
- Allure test reporting
- GitHub Actions CI/CD integration

---

## API Testing Coverage

| Module | Test Scenario | Status |
|-|-|-|
| Account | Create new user account | 🚧 |
| | Generate authentication token | 🚧 |
| | Login with valid credentials | 🚧 |
| | Get user account details | 🚧 |
| | Delete user account | 🚧 |
| BookStore | Get all books | ✅ |
| | Get a specific book by ISBN | ✅ |
| | Add book to collection | ✅ |
| | Update book in collection | ✅ |
| | Delete book from collection | ✅ |

---

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

---

## Installation

Clone repository:

```bash
git clone https://github.com/maolanahadiar/bookstore-api-automation-framework.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Test

Run all tests:

```bash
pytest
```

Run & generate Allure report:

```bash
pytest --alluredir=reports/allure-results
```

Open Allure report:

```bash
allure serve reports/allure-results
```

---

## CI/CD

GitHub Actions pipeline automatically runs API tests on:

- Push
- Pull Request
- Manual Trigger

Pipeline flow:

```
Checkout Repository
   |
Setup Python
   |
Install Dependencies
   |
Install Allure CLI
   |
Execute API Tests
   |
Generate Allure Report
   |
Deploy Allure Report to GitHub Pages
   |
Upload Test Artifacts & Logs
```
#### Latest Execution Status:
[![Bookstore API Automation](https://github.com/maolanahadiar/book-store-api-automation-framework/actions/workflows/api-test.yml/badge.svg)](https://github.com/maolanahadiar/bookstore-api-automation-framework/actions/workflows/api-test.yml)

---

## Test Reports

The framework generates:

- **Allure Report**
  - Test execution summary
  - Passed/failed test results

- **API Logs**
  - Request and response details
  - Execution debugging support

➡️ [Click here to see the Live Allure Report](https://maolanahadiar.github.io/bookstore-api-automation-framework/)
