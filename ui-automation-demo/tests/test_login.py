from pages.login_page import LoginPage

def test_negative_login(driver):
    page = LoginPage(driver)
    page.open("https://www.saucedemo.com/")

    page.login("wrong_user", "wrong_password")

    assert "Epic sadface" in page.get_error_message()

    def test_positive_login(driver):
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")

        assert page.is_login_successful()