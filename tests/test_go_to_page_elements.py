from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.button_elements.click()
    assert elements_page.equal_url()
