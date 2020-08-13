from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from Utilities.BaseClass import BaseClass
from pageObjects import CheckoutPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)

        checkOutPage = homepage.shopItems()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()
        cards = checkOutPage.getCardTitles()

        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            if productname == "Blackberry":
                product.find_element_by_xpath("div/button").click()
                break
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmpage = checkOutPage.CheckOutItem()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLink("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        msg = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank" in msg

        self.driver.get_screenshot_as_file("screen.png")
