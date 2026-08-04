# Bookstore API Automation Framework

This project contains automated test for the [DemoQA Bookstore API](https://demoqa.com/swagger) built with Python, Requests, Pytest, and Allure to demonstrates best practices for API automation testing.
The goal is to make the automation framework easy to maintain, reusable, and scalable. 

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Requests](https://img.shields.io/badge/Requests-2.34-green)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

---

## Project Architecture

- Built using the Page Object Model (POM) design pattern
- Maintains separation of concerns between tests, services, and test data
- Follows clean code principles and Python coding standards

---

## Continuous Integration (CI)

This project uses GitHub Actions to automatically run the automation test suite on every push and pull request.

The CI workflow performs the following steps:

- Checkout Repository
- Setup Python
- Install Allure CLI
- Install Dependencies
- Execute API Tests
- Generate Allure Report
- Upload Allure Result
- Upload API Logs
  
#### Latest Execution Status:
[![Bookstore API Automation](https://github.com/maolanahadiar/book-store-api-automation-framework/actions/workflows/api-test.yml/badge.svg)](https://github.com/maolanahadiar/book-store-api-automation-framework/actions/workflows/api-test.yml)
---

## Setup

1. Clone repository:

```bash
git clone https://github.com/maolanahadiar/bookstore-api-automation-framework.git
```

2. Move to project directory:

```bash
cd bookstore-api-automation-framework
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate virtual environment:

- macOS/Linux

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

To run the test suite, simply execute:

```bash
pytest
```

---

## Test Report

> Example of Allure Report

<p align="center">
<img src="https://github.com/user-attachments/assets/ee3cc714-aa33-44aa-8887-50f4d17cae11" width="900">
