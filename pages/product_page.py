from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self): 
        add_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_link.click()
        
    def should_be_text_add_to_basket(self): #проверка, что появляется сообщение об успешном добавлении товара в корзину
        assert self.is_element_present(*ProductPageLocators.TEXT_ADD_TO_BASKET), 'text about adding to basket is not appeared'
    def text_coincides(self): #проверка, что название продукта совпадает с названием в сообщении
    	assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_ADDED_TO_BASKET).text == self.browser.find_element(*ProductPageLocators.NAME_BOOK).text, "text is not coincides"
    def should_be_text_price_of_basket(self): #проверка, что появляеться сообщение об цене корзины
    	assert self.is_element_present(*ProductPageLocators.TEXT_INFO_ADD_BASKET), 'text with basket info is not appeared'
    def price_coincides(self): #проверка, что цена корзины совпадает с ценой добавленого товара
    	assert self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text == self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text, 'price is not coincides'
    def should_not_be_success_message(self):#проверка, что нет сообщения об успешном добавлении 
    	assert self.is_not_element_present(*ProductPageLocators.TEXT_ADD_TO_BASKET), "Success message is presented, but should not be"
        
    def should_disappear_success_message(self):
    	assert self.is_disappeared(*ProductPageLocators.TEXT_ADD_TO_BASKET), "Success message is presented, but should not be"


        

        

