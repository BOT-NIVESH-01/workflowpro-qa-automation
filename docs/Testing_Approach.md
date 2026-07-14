# Testing Approach

## Framework Architecture

The automation framework follows the Page Object Model (POM) to separate test logic from UI interactions. This improves maintainability and reduces code duplication.

## UI Testing

UI automation is implemented using Playwright. Browser interactions are encapsulated in reusable page objects while Pytest fixtures manage browser lifecycle.

## API Testing

API tests use a reusable client built on the Requests library. The client supports GET, POST, PUT, and DELETE operations and can be extended with authentication.

## Test Data Management

Test data is stored in JSON files under the `data/` directory to avoid hardcoding values inside test scripts.

## Reporting

HTML reports are generated using `pytest-html`. Logs are written to the `reports/logs` directory.

## Continuous Integration

The framework is configured to run automatically through GitHub Actions on every push and pull request.

## Assumptions

WorkflowPro is a fictional application used to demonstrate framework design. Only the smoke test executes against a public website.