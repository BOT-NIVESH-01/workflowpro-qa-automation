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

## Author

K. Nivesh Chowdary