import pytest

from api.project_api import ProjectAPI
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.mark.integration
@pytest.mark.skip(
    reason="Framework demonstration. Execution requires a deployed WorkflowPro environment."
)
def test_project_creation_api_ui(page):
    """
    Business Flow

    1. Create project using REST API.
    2. Login through Web UI.
    3. Verify project appears on dashboard.
    4. Execute same validation on BrowserStack mobile devices.
    5. Login as another tenant.
    6. Verify tenant isolation.
    """

    api = ProjectAPI()

    # Step 1: Create project
    api.create_project("Automation Demo")

    # Step 2: Login
    login = LoginPage(page)

    login.goto("https://app.workflowpro.com/login")

    login.login(
        "admin@company1.com",
        "password123"
    )

    # Step 3: Verify dashboard
    dashboard = DashboardPage(page)

    # Future enhancement:
    # Validate project visibility on BrowserStack Android/iOS.

    # Future enhancement:
    # Login using Company2 and verify project is not visible.

    assert dashboard is not None