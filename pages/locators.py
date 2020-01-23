from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TEXT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success.fade.in")
    NAME_BOOK_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    TEXT_INFO_ADD_BASKET = (By.CSS_SELECTOR, ".alert-info.fade.in")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
class BasketPageLocators():
	BASKET_FORMSET=(By.CSS_SELECTOR, '#basket_formset')
	BASKET_IS_EMPTY_TEXT=(By.CSS_SELECTOR, 'div[id="content_inner"]>p')

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION=(By.CSS_SELECTOR, "button[name='registration_submit']")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, "span .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

