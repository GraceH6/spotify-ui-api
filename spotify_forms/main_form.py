from playwright.sync_api import Page


class MainContentForm:

    __search_input_xpath = "xpath=//form[@role='search']//input"

    def search_singer(self, page: Page, name):
        page.locator(self.__search_input_xpath).fill(name)

    def get_song_by_name(self, page: Page, name):
        return page.locator(f"xpath=//div[contains(text(), \"{name}\")]")
