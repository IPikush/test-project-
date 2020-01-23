from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products(self):#проверка, что нет товаров в корзине 
    	assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Products are presented, but should not be"
    def should_be_text_basket_is_empty(self):
    	assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Basket is empty' text is not present"
    