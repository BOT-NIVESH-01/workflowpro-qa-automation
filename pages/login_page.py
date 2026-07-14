from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-btn"
    ERROR_MESSAGE = ".error-message"

    def __init__(self, page):
        super().__init__(page)

    def enter_email(self, email):
        self.fill(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)