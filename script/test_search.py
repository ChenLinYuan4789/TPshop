import pytest,os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import list_yml_file

def yml_key(key):
    return list_yml_file(key)

class TestSearch():

    def setup(self):
        self.driver = init_driver()
        self.SearchPage = SearchPage(self.driver)

    @pytest.mark.parametrize("keys", yml_key("search"))
    def test_search(self,keys):
        # 点击搜索框
        self.SearchPage.click_search_box()
        # 输入搜索内容
        self.SearchPage.send_search_text(keys)
        # 点击搜索
        self.SearchPage.click_search()