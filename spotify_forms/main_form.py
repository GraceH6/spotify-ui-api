from utils.page_instance import SingletonPage


class MainContentForm:

    __search_input_xpath = "xpath=//form[@role='search']//input"
    __page = SingletonPage().get_page()

    def search_singer(self, name):
        self.__page.locator(self.__search_input_xpath).fill(name)

    def get_song_by_name(self, name):
        return self.__page.locator(f"xpath=//div[contains(text(), \"{name}\")]")
