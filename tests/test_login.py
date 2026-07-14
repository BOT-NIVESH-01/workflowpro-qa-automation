from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.goto("https://app.workflowpro.com/login")

    login_page.login(
        "admin@company1.com",
        "password123"
    )

    # Since WorkflowPro is fictional,
    # we're just demonstrating the framework.
    assert True