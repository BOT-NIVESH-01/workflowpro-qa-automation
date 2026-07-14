# WorkflowPro QA Automation Framework

## Overview

This repository contains a sample QA Automation Framework designed for a fictional B2B SaaS application called **WorkflowPro**.

The framework demonstrates industry-standard automation practices using **Python**, **Pytest**, **Playwright**, and the **Page Object Model (POM)**.

---

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

> **Note**
>
> WorkflowPro is a fictional SaaS application used as part of a QA Automation design assessment.
> The automation framework demonstrates how UI, API, and integration tests would be structured in a production environment.
> Only the smoke test executes against a real public website (`https://example.com`) to verify the framework setup.

## Author

K. Nivesh Chowdary