# Testing Approach

## Framework Architecture

The automation framework follows the **Page Object Model (POM)** design pattern to separate UI interactions from test logic. Common browser operations are implemented in a reusable `BasePage`, while application-specific functionality is encapsulated within individual page objects. This improves maintainability, readability, and scalability as the application grows.

---

## UI Testing Strategy

UI automation is implemented using **Playwright** with **Pytest**. Browser lifecycle management is handled through reusable fixtures defined in `conftest.py`. Explicit waits and Playwright's web-first assertions are used to reduce flaky test failures caused by dynamic loading.

---

## API Testing Strategy

The framework includes a reusable API client built using the `requests` library. API calls are used for test setup and cleanup whenever possible to reduce execution time and improve reliability. Business operations such as project creation are encapsulated in dedicated API wrapper classes.

---

## API + UI Integration Strategy

The preferred testing strategy is:

1. Create required data through REST APIs.
2. Validate business functionality through the Web UI.
3. Execute the same validation on supported mobile platforms using BrowserStack.
4. Verify tenant isolation by logging into another tenant and confirming that resources are inaccessible.

Using APIs for setup significantly reduces execution time compared to creating data through the UI.

---

## Test Data Management

Test data is stored separately from test scripts using JSON files under the `data/` directory. Different users, roles, and tenant information can be maintained independently without modifying automation code.

Dynamic data such as project names should be generated using UUIDs to avoid collisions during parallel execution.

---

## Cross-Platform Testing

The framework is designed to support:

- Chromium
- Firefox
- WebKit (Safari)
- Android devices
- iOS devices

Cross-browser and mobile execution can be performed through BrowserStack without modifying the test scripts.

---

## Reporting

The framework generates HTML reports using `pytest-html`. Execution logs are stored under the `reports/logs` directory. Screenshots can be captured automatically for failed tests to simplify debugging.

---

## Continuous Integration

GitHub Actions is used to execute the automation suite automatically on every push and pull request. This enables continuous validation and early defect detection.

---

## Assumptions

Since WorkflowPro is a fictional application used for this assessment:

- URLs are illustrative.
- Authentication is assumed.
- BrowserStack execution is represented conceptually.
- API endpoints follow the specification provided in the assessment.