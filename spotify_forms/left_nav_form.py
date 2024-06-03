from playwright.sync_api import Page


class LeftNavigationForm:

    __search_button_xpath = "xpath=//div[@id='Desktop_LeftSidebar_Id']//a[@href='/search']"

    def click_search_btn(self, page: Page):
        page.locator(self.__search_button_xpath).click()
