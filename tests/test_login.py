from pages.login_page import LoginPage
from playwright.sync_api import expect
import re


def test_user_can_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
