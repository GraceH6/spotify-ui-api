from playwright.sync_api import sync_playwright


class SingletonPage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonPage, cls).__new__(cls)
            cls._instance._init_playwright()
        return cls._instance

    def _init_playwright(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def get_page(self):
        return self.page
