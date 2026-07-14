from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def type(self, locator, text):
        self.page.locator(locator).type(text)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def wait_for(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def screenshot(self, name):
        self.page.screenshot(path=f"reports/screenshots/{name}.png")