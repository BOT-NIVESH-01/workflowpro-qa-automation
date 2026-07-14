# WorkflowPro QA Automation Framework

## Overview

This repository contains a sample QA Automation Framework designed for a fictional B2B SaaS application called **WorkflowPro**.

The framework demonstrates industry-standard automation practices using **Python**, **Pytest**, **Playwright**, and the **Page Object Model (POM)**.

---

> **Assessment Note**
>
> This repository demonstrates the design of a production-ready QA Automation framework for the fictional **WorkflowPro** SaaS platform described in the assessment.
>
> Only the smoke test executes against a public website (`https://example.com`) to validate the framework configuration. Other tests illustrate the framework design and require a deployed WorkflowPro environment.

> **Note**
>
> WorkflowPro is a fictional SaaS application used as part of a QA Automation design assessment.
> The automation framework demonstrates how UI, API, and integration tests would be structured in a production environment.
> Only the smoke test executes against a real public website (`https://example.com`) to verify the framework setup.


## Features

- UI Automation using Playwright
- API Testing using Requests
- Page Object Model (POM)
- Pytest Fixtures
- HTML Test Reports
- JSON Test Data
- Multi-environment Configuration
- GitHub Actions Ready

---

## Project Structure

```text
workflowpro-qa-automation/

api/
config/
data/
docs/
pages/
reports/
tests/
utils/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<username>/workflowpro-qa-automation.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
python -m playwright install
```

---

## Run Tests

Run all tests

```bash
pytest
```

Run a specific test

```bash
pytest tests/test_smoke.py
```

---

## Reports

HTML reports are generated inside

```
reports/html/
```

---

## Technologies

- Python
- Playwright
- Pytest
- Requests
- pytest-html

---

## Design Pattern

The framework follows the **Page Object Model (POM)** to improve maintainability, readability, and scalability.

---

## Future Enhancements

The framework is designed to support additional capabilities such as:

- BrowserStack integration for cross-browser and mobile execution
- Parallel test execution
- Automatic screenshot capture on failures
- Playwright tracing
- Allure reporting
- Docker-based execution

## Author

K. Nivesh Chowdary