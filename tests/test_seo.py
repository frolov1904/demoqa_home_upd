from pages.demoqa import Demoqa

def test_check_title(browser):
    demo_qa_page=Demoqa(browser)
    demo_qa_page.visit()
    assert browser.title=='DEMOQA'
