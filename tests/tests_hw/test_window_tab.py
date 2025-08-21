import time

from pages.links import Links

def test_window_tab(browser):
    link_page=Links(browser)
    link_page.visit()
    assert link_page.btn_home.get_text()=='Home'
    assert link_page.btn_home.get_dom_attribute('href')=='https://demoqa.com'
    link_page.btn_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2