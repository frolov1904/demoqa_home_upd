from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test1(browser):
    """Проверка текста подвала на главной странице"""
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()

    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test2(browser):
    """Проверка текста по центру на странице Elements"""
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.button_elements.click() #переход на страницу Elements по клику

    assert elements_page.text2.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page=ElementsPage(browser)
    el_page.visit()
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()