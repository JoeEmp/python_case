from poium import Page, Element

class BaiduIndexPage(Page):
    search_input = Element(name='wd')
    search_button = Element(id_='su')
