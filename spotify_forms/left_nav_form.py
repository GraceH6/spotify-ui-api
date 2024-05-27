from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm
from selenium.webdriver.common.by import By


class LeftNavigationForm(BaseForm):
    __search_button = PyQualityServices.element_factory.get_button((By.XPATH, "//div[@id='Desktop_LeftSidebar_Id']"
                                                                              "//a[@href='/search']"), "Search button")

    def __init__(self):
        super(LeftNavigationForm, self).__init__((By.XPATH, "//div[@id='Desktop_LeftSidebar_Id']"),
                                                 name="Left Navigation")

    def click_search_btn(self):
        self.__search_button.click()
