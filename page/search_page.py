from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):

    search_box = By.ID, "com.ss.android.article.news:id/bpb"
    search_box2 = By.ID, "com.ss.android.article.news:id/w3"
    search_button = By.XPATH, ["text,搜索,1", "resource-id,com.ss.android.article.news:id/w0,1"]

    def click_search_box(self):
        self.click(self.search_box)

    def send_search_text(self, text):
        self.send_keys(self.search_box2, text)

    def click_search(self):
        self.click(self.search_button)