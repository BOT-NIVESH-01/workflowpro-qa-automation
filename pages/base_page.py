from pathlib import Path

from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        expect(self.page.locator(locator)).to_be_visible()
        self.page.locator(locator).click()

    def fill(self, locator, value):
        expect(self.page.locator(locator)).to_be_visible()
        self.page.locator(locator).fill(value)

    def type(self, locator, value):
        self.page.locator(locator).type(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_url(self, url):
        expect(self.page).to_have_url(url)

    def get_title(self):
        return self.page.title()

    def reload(self):
        self.page.reload()

    def screenshot(self, name):
        Path("reports/screenshots").mkdir(
            parents=True,
            exist_ok=True
        )

        self.page.screenshot(
            path=f"reports/screenshots/{name}.png"
        )
    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")