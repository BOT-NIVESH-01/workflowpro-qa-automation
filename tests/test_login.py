import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.skip(
    reason="WorkflowPro is a fictional application. This test demonstrates framework design only."
)
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.goto("https://app.workflowpro.com/login")

    login_page.login(
        "admin@company1.com",
        "password123"
    )

    assert login_page is not None