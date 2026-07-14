from pages.base_page import BasePage


class ProjectPage(BasePage):

    PROJECT_NAME = "#project-name"
    CREATE_BUTTON = "#create-project"
    DELETE_BUTTON = "#delete-project"

    def __init__(self, page):
        super().__init__(page)

    def create_project(self, name):
        self.fill(self.PROJECT_NAME, name)
        self.click(self.CREATE_BUTTON)

    def delete_project(self):
        self.click(self.DELETE_BUTTON)