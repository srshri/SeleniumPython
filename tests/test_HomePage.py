import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        driver.find_element_by_name("name").send_keys(getData[0])
        dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_index(1)
        dropdown.select_by_visible_text("Male")
        driver.find_element_by_css_selector("input[value='Submit']").click()
        message = driver.find_element_by_css_selector("[class*='alert-success']").text
        assert "successfdfdf" in message
        print("New Line")
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
