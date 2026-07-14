import pytest

from api.project_api import ProjectAPI
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.mark.integration
@pytest.mark.skip(
    reason="WorkflowPro is a fictional application. This test demonstrates API + UI integration design."
)
def test_project_creation_api_ui(page):
    api = ProjectAPI()

    # Example API setup
    api.create_project("Automation Demo")

    login = LoginPage(page)

    login.goto("https://app.workflowpro.com/login")

    login.login(
        "admin@company1.com",
        "password123"
    )

    dashboard = DashboardPage(page)

    assert dashboard is not None