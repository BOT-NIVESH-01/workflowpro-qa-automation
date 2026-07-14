import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.skip(
    reason="Framework demonstration. Execution requires a deployed WorkflowPro environment."
)
def test_valid_login(page):
    """
    Demonstrates login automation using
    the Page Object Model.
    """

    login_page = LoginPage(page)

    login_page.goto(
        "https://app.workflowpro.com/login"
    )

    login_page.login(
        "admin@company1.com",
        "password123"
    )

    assert login_page is not None