from pages.base_page import BasePage


class DashboardPage(BasePage):

    WELCOME_MESSAGE = ".welcome-message"
    PROJECT_CARDS = ".project-card"
    LOGOUT_BUTTON = "#logout-btn"

    def __init__(self, page):
        super().__init__(page)

    def is_dashboard_loaded(self):
        return self.is_visible(self.WELCOME_MESSAGE)

    def get_project_count(self):
        return self.page.locator(self.PROJECT_CARDS).count()

    def is_project_visible(self, project_name):
        return self.page.locator(
            f".project-card:has-text('{project_name}')"
        ).is_visible()

    def logout(self):
        self.click(self.LOGOUT_BUTTON)