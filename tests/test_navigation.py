from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page=Demoqa(browser)
    elements_page=ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.button_elements.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()