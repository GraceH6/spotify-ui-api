from utils.page_instance import SingletonPage


class LeftNavigationForm:

    __page = SingletonPage().get_page()
    __search_button_xpath = "xpath=//div[@id='Desktop_LeftSidebar_Id']//a[@href='/search']"

    def click_search_btn(self):
        self.__page.locator(self.__search_button_xpath).click()
