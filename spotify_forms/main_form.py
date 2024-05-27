from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm
from selenium.webdriver.common.by import By


class MainContentForm(BaseForm):
    __search_input = PyQualityServices.element_factory.get_text_box((By.XPATH, "//form[@role='search']//input"),
                                                                    "Search input")

    def __init__(self):
        super(MainContentForm, self).__init__((By.XPATH, "//div[@class='main-view-container']"),
                                              name="Main form")

    def search_singer(self, name):
        self.__search_input.send_keys(name)

    def get_song_by_name(self, name):
        return PyQualityServices.element_factory.get_text_box((By.XPATH, f"//div[contains(text(), \"{name}\")]"),
                                                              f"A song named '{name}'")
