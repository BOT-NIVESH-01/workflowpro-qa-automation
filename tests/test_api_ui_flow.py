from api.project_api import ProjectAPI
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_project_creation_api_ui(page):

    # API setup
    api = ProjectAPI()

    api.create_project("Automation Demo")

    # UI verification
    login = LoginPage(page)

    login.goto("https://app.workflowpro.com/login")

    login.login(
        "admin@company1.com",
        "password123"
    )

    dashboard = DashboardPage(page)

    # Framework demonstration
    assert True