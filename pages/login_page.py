from playwright.sync_api import Page
from config.settings import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role(
            "button",
            name="Login"
        )

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()