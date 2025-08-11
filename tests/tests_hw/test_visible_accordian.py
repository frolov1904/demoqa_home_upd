import time
from pages.accordian import Accordian

def test_visible_accordion(browser):
    accordion_page = Accordian(browser)
    accordion_page.visit()

    # Проверяем, что элемент #section1Content > p виден
    assert accordion_page.section1_content_p.find_element().is_displayed()

    # Кликаем на #section1Heading
    accordion_page.section1_heading.click()

    time.sleep(2)

    # После клика элемент #section1Content > p НЕ виден
    assert not accordion_page.section1_content_p.find_element().is_displayed()

def test_visible_accordion_default(browser):
    accordion_page = Accordian(browser)
    accordion_page.visit()

    # Проверяем, что элементы по умолчанию скрыты
    assert not accordion_page.section2_content_p1.find_element().is_displayed()
    assert not accordion_page.section2_content_p2.find_element().is_displayed()
    assert not accordion_page.section3_content_p.find_element().is_displayed()
